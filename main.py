from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

SCREEN_MANAGER = ScreenManager()


class nameOfApp(App):
    def build(self):
        SCREEN_MANAGER.current = 'main'
        return SCREEN_MANAGER


Window.clearcolor = (0, 0, 1, 1)

class Profile(BoxLayout):
    pass

class Profile2(BoxLayout):
    pass

class MainScreen(Screen):
    global yellowCounter
    yellowCounter = 1
    global blueCounter
    blueCounter = 1
    global total
    total = 2
    global profitPerBet
    profitPerBet = 2

    def countYellow(self, num):
        global yellowCounter
        self.updateOdds(num)
        yellowCounter += num
        self.ids.yellow_counter.text = "Yellows: " + str(yellowCounter)

    def countBlue(self, num):
        global blueCounter
        self.updateOdds(num)
        blueCounter += num
        self.ids.blue_counter.text = "Blues: " + str(blueCounter)

    def updateOdds(self, num):
        global profitPerBet
        global yellowCounter
        global blueCounter
        global total
        total += num
        yellow = round((total / yellowCounter) * (10 - profitPerBet), 2)
        blue = round((total / blueCounter) * (10 - profitPerBet), 2)
        if yellow < 10:
            yellow = 10.01
        elif blue < 10:
            blue = 10.01
        self.ids.yellow.text = "+$ " + str(round(yellow*10, 0))
        self.ids.blue.text = "+$ " + str(round(blue*10, 0))
        self.ids.yellow1.text = "$ " + str(yellow)
        self.ids.blue1.text = "$ " + str(blue)
        self.updateBottom(yellow, blue)

    def updateBottom(self, yellow, blue):
        global total
        global profitPerBet
        global yellowCounter
        global blueCounter
        self.ids.total.text = "Total Bets Placed: " + str(total)
        self.ids.profit.text = str(round((total * 10) - (yellowCounter * yellow),2)) + "  Vs  " + str(round((total * 10) - (blueCounter * blue),2))



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))

if __name__ == "__main__":
    nameOfApp().run()
