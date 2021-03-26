"""
  Still under development not ready for external use
  Visually: 90% Done
  Backend: 10%
"""


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout


class DialogContent(BoxLayout):
    pass


class FirstWindow(Screen):
    def login(self):
        if self.ids.user.text and self.ids.password.text != '':
            self.ids.welcome_label.text = f'Sup {self.ids.user.text}!'
            if self.manager.current == 'first':
                self.manager.current = "second"
                self.manager.transition.direction = 'left'

    def logout(self):
        if self.ids.welcome_label.text != "WELCOME":
            self.ids.welcome_label.text = "WELCOME"

    def clear(self):
        self.ids.welcome_label.text = "WELCOME"
        self.ids.user.text = ""
        self.ids.password.text = ""

    def chg(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        elif self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"

    def animated_login_button(self, widget, *args):
        animate = Animation(
            background_color=(0, 1, 1, 0),
            duration=.1,
            opacity=1,
            pos_hint={"center_x": .6}

        )

        animate += Animation(duration=.1, opacity=1, pos_hint={"center_x": 0.5})
        animate += Animation(duration=.1, pos_hint={"center_x": 0.4})
        animate += Animation(duration=.1, opacity=1, pos_hint={"center_x": 0.5})

        animate.start(widget)


class SecondWindow(Screen):
    dialog = False

    def __init__(self, **kw):
        super().__init__(**kw)
        """Declaring all the variables for the final product :) """
        self.UP_TIME = ["9:00", "11:00", "13:00", "15:00"]
        self.DOWN_TIME = ['10:00', '12:00', '14:00', '16:00']
        self.UP_TICKET = [480, 480, 480, 480]
        self.DOWN_TICKET = [480, 480, 480, 640]
        self.TOTAL_MONEY = [0, 0, 0, 0]
        self.TOTAL_PASSENGERS_ = [0, 0, 0, 0]
        self.TEXT_TO_DISPLAY = ''

    def show_dialog(self, Jrny: int, tickets: int):

        """Create group creation popup"""

        close = MDFlatButton(text="No", on_release=self.close_dialog)
        proceed = MDFlatButton(text="Yes")
        if not self.dialog:
            self.dialog = MDDialog(
                text=f"You are about to buy Tickets for journey# {Jrny}",
                title=f"Are you sure you want to buy {tickets} Tickets?",
                #type="custom",
                size_hint=(0.5, 1),
                auto_dismiss=False,  # needed to allow Buttons to operate
                buttons=[proceed, close]
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.ids.time_check.text = ''
        self.ids.ticket_check.text = ''
        self.dialog = True

    def logout(self):
        self.manager.current = "first"
        self.manager.transition.direction = 'right'

    def check_time_and_ticket(self, widget):
        user_time = str(self.ids.time_check.text)
        user_ticket = str(self.ids.ticket_check.text)
        if user_time in self.UP_TIME and user_ticket.isnumeric():
            self.dialog = False
            INDEX = self.UP_TIME.index(user_time)
            INDEX = INDEX+1
            self.show_dialog(tickets=int(user_ticket), Jrny=int(INDEX))

        elif user_time in self.DOWN_TIME and user_ticket.isnumeric():
            INDEX = self.DOWN_TIME.index(self.ids.time_check.text)
            print(INDEX)

        else:
            self.animated_ticket_button(widget)

    def animated_ticket_button(self, widget):
        user_time = str(self.ids.time_check.text)
        user_ticket = str(self.ids.ticket_check.text)
        animate = Animation(
            background_color=(0, 1, 1, 0),
            duration=.1,
            opacity=1,
            pos_hint={"center_x": .6}

        )

        animate += Animation(duration=.1, opacity=1, pos_hint={"center_x": 0.5})
        animate += Animation(duration=.1, pos_hint={"center_x": 0.4})
        animate += Animation(duration=.1, opacity=1, pos_hint={"center_x": 0.5})
        if self.ids.ticket_check.text == '' and self.ids.time_check.text == '':
            animate.start(widget)
        elif user_time not in self.UP_TIME and user_time not in self.DOWN_TIME:
            animate.start(widget)
        elif not user_ticket.isdigit():
            animate.start(widget)


class WindowManager(ScreenManager):
    pass


class Awesomeapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.title = "Login Screen"
        return Builder.load_file("main.kv")

    def chg(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Red"
        elif self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Red"


if __name__ == "__main__":
    Awesomeapp().run()
