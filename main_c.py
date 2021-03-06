"""
Доработать калькулятор:
1) сделать историю вычислений +++
2) сделать проверку первого ноля (чтобы не было вроде 02 числа) +++
3) сделать невозможность деления на 0 +++
4) после очисткив поле ввода остается 0, но после начала ввода он исчезает +++
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

 
class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
                multiline=False, readonly=True, halign="right", font_size=55
        )
        self.hist = TextInput(
                multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        main_layout.add_widget(self.hist)
        buttons = [
            ["1", "2", "3", "/"],
            ["4", "5", "6", "*"],
            ["7", "8", "9", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
 
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
 
        return main_layout


    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = "0"
            self.hist.text= ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Не добавляйте два оператора подряд, рядом друг с другом
                return
            elif current == "" and button_text in self.operators:
                # Первый символ не может быть оператором
                return
            else:
                new_text = (current + button_text) if current != "0" else button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
 
    def on_solution(self, instance):
        text = self.solution.text
        if text :
        	try:
        		solution = str(eval(self.solution.text))
        	except ZeroDivisionError:
        		solution = "0"
        	finally:
        		self.solution.text = solution
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
            hist = str(text)+ "="+str(solution)
            self.hist.text = hist

 
if __name__ == "__main__":
    app = MainApp()
    app.run()