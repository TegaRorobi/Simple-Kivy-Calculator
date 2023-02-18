# how to xcreate a virtual environment
# step1 - mkdir folder_name
# step2 - cd folder_name
# step3 - python -m venv environment_name
# step4 - environment_name\Scripts\activate.bat
# the environment should now have the environment name in brackets before the regular path



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.config import Config
from tkinter import messagebox

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '560')

class CalculatorApp(App):
    
    def build(self):
        self.operators=['+','-','*','/','**','**0.5']
        self.last_button=None
        self.last_was_operator=None
        main_layout=BoxLayout(orientation='vertical',spacing=5,padding=5)
        self.solution = TextInput(multiline = False,halign = 'right',readonly = True,font_size = 55,size_hint=(1,None),height=75)
        main_layout.add_widget(self.solution)
        buttons = [ ['CE','**','**0.5'],
                    ['7','8','9','/'],
                    ['4','5','6','*'],
                    ['1','2','3','-'],
                    ['.','0','<','+']    ]
        for row in buttons:
            h_layout=BoxLayout(spacing=5)
            for button in row:
                if button in ['7','8','9','4','5','6','1','2','3','0']:                  
                    btn=Button(text=button,background_color=(1,.6,0,1),font_size=32) #this gives orange buttons
                else:
                    btn=Button(text=button,background_color=(1,0,1,1),font_size=32) #this gives purple buttons

                btn.bind(on_press = self.on_button_press)
                h_layout.add_widget(btn)
            main_layout.add_widget(h_layout)
        equals_button = Button(text='=', background_color=(0,1,0,1),font_size=self.solution.width/3) #this is to create a long, green button
        equals_button.bind(on_press=self.get_solution)
        main_layout.add_widget(equals_button)
        return main_layout

    def on_button_press(self,instance):
        
        current=self.solution.text
        button_text=instance.text
        if button_text == '<':
            self.solution.text=self.solution.text[:-1]
        elif button_text.upper() == 'CE':
            self.solution.text=''
        
        else:
            #you cannot evaluate two or more operators side by side
            if current and(self.last_was_operator and button_text in self.operators):
                return
            #an operator cannot be the first character
            elif not current and button_text in self.operators:
                return
            #you cannot put two dots together
            elif self.last_button =='.' and button_text=='.':
                return
            #you cannot put more than one dot in the same
            elif '.' in self.solution.text and button_text == '.' and '+' not in self.solution.text and '-' not in self.solution.text and '*' not in self.solution.text and '/' not in self.solution.text:
                return
            else:
                new_text=current + button_text
                self.solution.text=new_text
        #ater using the button_text, set it to be the last button preparing it for the next occurence of the loop of the build function
        self.last_button=button_text
        self.last_was_operator = self.last_button in self.operators

    def get_solution(self,instance):
        if self.solution.text=='':
            return
        ind=0
        solution =  f"{eval(self.solution.text)}"
        if '.' in solution:
            ind=solution.index('.')
        #str(eval(self.solution.text))
            if len(solution)>=ind+3:
                self.solution.text=f"{eval(self.solution.text):0.3f}"
            else:
                self.solution.text=f"{eval(self.solution.text)}"
        else:
            self.solution.text = solution
        self.last_was_operator=False


        
if __name__ == '__main__':
    def recursion_loop():
        try:
            CalculatorApp().run()
        except :
            messagebox.showwarning('Invalid Operation', 'The calculator does not support that operation')
            recursion_loop()
    recursion_loop()