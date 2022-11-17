from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.uix.floatlayout import FloatLayout

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar: 
            title: 'Login'
            right_action_item: [["menu", lambda x : x]]
        TelaLogin:

<SenhaCard>: 
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint:{'center_x': .5, 'center_y': .5}
    MDBoxLayout: 
        size_hint_y: .2
        padding: [25,0,25,0]
        md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: 'Mudar Senha'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
        
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1,1,1,1
            pos_hint: {'center_x': .5, 'center_y': .1 }
            on_release: root.fechar()

        MDFloatLayout:
            MDTextField:
                size_hint_x: .9
                hint_text: 'Código enviado por email'
                pos_hint: {'center_x': .5, 'center_y': .8 }

            MDTextField:
                size_hint_x: .9
                hint_text: 'Nova senha'
                pos_hint: {'center_x': .5, 'center_y': .6 }

            MDTextField:
                size_hint_x: .9
                hint_text: 'Confirmar senha'
                pos_hint: {'center_x': .5, 'center_y': .4 }
            
            MDRectangleFlatButton:
                text: "Enviar"
                theme_text_color: "Custom"
                text_color: "black"
                line_color: "black"
                pos_hint: {'center_x': .5, 'center_y': .2 }
                on_release: root.fechar()
    

<TelaLogin>:
    MDTextField:
        size_hint_x: .6
        hint_text: 'Email'
        pos_hint: {'center_x': .5, 'center_y': .6 }

    MDTextField:
        size_hint_x: .6
        hint_text: 'Senha'
        pos_hint: {'center_x': .5, 'center_y': .5}

    MDRaisedButton:
        size_hint_x: .6
        pos_hint: {'center_x': .5, 'center_y': .3}
        text: 'Logar'

    MDLabel: 
        pos_hint: {'center_y': .2}
        halign: 'center'
        text: 'Esqueceu sua senha?'

    MDTextButton:
        pos_hint: {'center_x': .5, 'center_y': .1}
        text: 'Clique Aqui!'
        on_release: root.abrir_card()
'''

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())

class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_string(KV)
    
Login().run()