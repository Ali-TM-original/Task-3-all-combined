"""
  Still under development not ready for external use
  Visually: 90% Done
  Backend: 20%
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
    dialog2 = False

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
        self.user_time = ''
        self.user_ticket = 0

    def show_dialog(self, jrny: int, tickets: int, freetick: int):

        """Create group creation popup"""

        close = MDFlatButton(text="No", on_release=self.close_dialog)
        proceed = MDFlatButton(text="Yes", on_release=self.yes_button_dialog)
        if not self.dialog:
            self.dialog = MDDialog(
                text=f"You are about to buy Tickets for journey# {jrny}",
                title=f"Are you sure you want to buy {tickets} Tickets? You will recieve {freetick} Free Tickets",
                # type="custom",
                size_hint=(0.5, 1),
                auto_dismiss=False,  # needed to allow Buttons to operate
                buttons=[proceed, close]
            )
        self.dialog.open()

    def about_dialog(self):
        close = MDFlatButton(text="Close", on_release=self.close_dialog)
        if not self.dialog2:
            self.dialog_ = MDDialog(
                text=f"Just took inspirations form my previous script of the same problem but it was done on a cli"
                     f"This took real hardwork and time as i had 0 knowledge about Kivy in general, saw alot of times "
                     f"when i thought to end this project",
                title=f"Created by: Shahzaib Ali aka Ali™",
                # type="custom",
                size_hint=(0.5, 1),
                auto_dismiss=False,
                buttons=[close]
            )
        self.dialog_.open()

    def close_dialog(self, xobj):
        try:
            self.dialog.dismiss()
            self.ids.time_check.text = ''
            self.ids.ticket_check.text = ''
            self.dialog = True
        except AttributeError:
            self.dialog_.dismiss()
            self.dialog2 = True

    def logout(self):
        self.manager.current = "first"
        self.manager.transition.direction = 'right'

    @staticmethod
    def free_ticket(num):
        if 10 <= num <= 80:
            ticket = round(num / 10)
            return int(ticket)
        else:
            return int(0)

    def check_time_and_ticket(self, widget):
        self.user_time = str(self.ids.time_check.text)
        self.user_ticket = str(self.ids.ticket_check.text)
        if self.user_time in self.UP_TIME and self.user_ticket.isnumeric():
            self.dialog = False
            INDEX = self.UP_TIME.index(self.user_time)
            INDEX = INDEX + 1
            free_ticket = self.free_ticket(int(self.user_ticket))
            self.show_dialog(tickets=int(self.user_ticket), jrny=int(INDEX), freetick=int(free_ticket))

        elif self.user_time in self.DOWN_TIME and self.user_ticket.isnumeric():
            self.dialog = False
            INDEX = self.DOWN_TIME.index(self.user_time)
            INDEX = INDEX + 1
            free_ticket = self.free_ticket(int(self.user_ticket))
            self.show_dialog(tickets=int(self.user_ticket), jrny=int(INDEX), freetick=int(free_ticket))

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

    def yes_button_dialog(self, obj):
        """BRAIN OF THE SCRIPT FINISH THIS FAST NOW BRO"""
        user_input_ticket = self.user_ticket
        user_input_time = self.user_time
        if user_input_time in self.UP_TIME:
            INDEX = self.UP_TIME.index(self.user_time)
            free_ticket = self.free_ticket(int(user_input_ticket))
            "Do SOMETHING"
        elif user_input_time in self.DOWN_TIME:
            INDEX = self.DOWN_TIME.index(self.user_time)
            free_ticket = self.free_ticket(int(user_input_ticket))
            "DO SOMETHING"


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

"""
    To Ignore debugging message use os
    import os
    os.environ["KIVY_NO_CONSOLELOG"] = "1"
    
    This works the best
    
"""
