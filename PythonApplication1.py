from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty

KV = """
<Screen_1>:
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen1'
            text: 'урок'
            icon: 'book'
            
          
        
            MDLabel:
                text: 'Урок'
                pos_hint: {"center_y": 0.9 ,"center_x" : 0.7 }
                bold: True
                font_size:"50sp"

            MDRaisedButton:
                pos_hint: {"center_x": .22, "center_y": .7}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_3'
                

            MDRaisedButton:
                pos_hint: {"center_x": .7, "center_y": .7}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_3'
                

            MDRaisedButton:
                pos_hint: {"center_x": .22, "center_y": .5}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_4'
                

            MDRaisedButton:
                pos_hint: {"center_x": .7, "center_y": .5}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_5'
                

            MDRaisedButton:
                pos_hint: {"center_x": .22, "center_y": .3}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_6'
                

            MDRaisedButton:
                pos_hint: {"center_x": .7, "center_y": .3}
                theme_text_color:"Custom"
                md_bg_color:1, 1, 1, 1  
                text_color:0, 0, 0, 1
                elevation_normal:10 
                font_size:"30sp"
                size: 180, 180
                text: "текст"
                on_release: app.root.current = 'screen_7'
                


                

                
                
        MDBottomNavigationItem:
            name: 'screen2'
            text: 'тести'
            icon: 'border-color'
            MDLabel:
                text: 'Тести'
                pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
                bold: True
                font_size:"50sp"

            MDCard :
                size_hint: (.7, .7)
                pos_hint: {'center_x': .5, 'center_y': .5}
                elevation : 2
                text: "текст"

                



        MDBottomNavigationItem:
            name: 'screen3'
            text: 'прогрес'
            icon: 'check'
            MDLabel:
                text: 'Прогрес'
                pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
                bold: True
                font_size:"50sp"

            Image:
                source: "C:/Users/Mishania/Desktop/mobile_application_2024/mobile_application_2024/temp/img/diogram.png"

        
<Screen_2>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"
        
    

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
<Screen_3>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}                
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
<Screen_4>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
<Screen_5>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
<Screen_6>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
<Screen_7>:
    MDLabel:
        text: 'Урок'
        pos_hint: {"center_y": 0.9 ,"center_x" : 0.6 }
        bold: True
        font_size:"50sp"

    MDCard :
        size_hint: (.7, .7)
        pos_hint: {'center_x': .5, 'center_y': .5}
        elevation : 2
        text: "текст"
        
    MDRaisedButton:
        pos_hint: {"center_x": .2, "center_y": .1}
        theme_text_color:"Custom"
        md_bg_color:1, 1, 1, 1  
        text_color:0, 0, 0, 1
        elevation_normal:10 
        font_size:"30sp"
        size: 180, 180
        text: "Назад"
        on_release: app.root.current = 'screen_1'
        
"""

class Screen_1(Screen):
    def switch(self):
        self.parent.current = 'screen_2'

class Screen_2(Screen):
    def switch(self):
        self.parent.current = 'screen_1'
        
class Screen_3(Screen):
    def switch(self):
        self.parent.current = 'screen_1'
        
class Screen_4(Screen):
    def switch(self):
        self.parent.current = 'screen_1'

class Screen_5(Screen):
    def switch(self):
        self.parent.current = 'screen_1'
        
class Screen_6(Screen):
    def switch(self):
        self.parent.current = 'screen_1'
       
class Screen_7(Screen):
    def switch(self):
        self.parent.current = 'screen_1'

class Manager(ScreenManager):
    # screen_1 = ObjectProperty(None)
    # screen_2 = ObjectProperty(None)
    pass

class MainApp(MDApp):
    # dialog = None

    def build(self):
        Builder.load_string(KV)
        sm = Manager()
        sm.add_widget(Screen_1(name='screen_1'))
        sm.add_widget(Screen_2(name='screen_2'))
        sm.add_widget(Screen_3(name='screen_3'))
        sm.add_widget(Screen_4(name='screen_4'))
        sm.add_widget(Screen_5(name='screen_5'))
        sm.add_widget(Screen_6(name='screen_6'))
        sm.add_widget(Screen_7(name='screen_7'))
        
        
        return sm

MainApp().run()