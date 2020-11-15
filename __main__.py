#from kivy.core.window import Window
from kivy.app import App
from kivy.core.audio import SoundLoader
import winsound
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import Image

Config.set('graphics', 'width', '520')
Config.set('graphics', 'height', '980')

from kivy.core.window import Window

Window.clearcolor = (0.8, 0.96, 1, 1)

#Window.fullscreen = False #TODO: поставить TRUE  ..CCFFD4

class EarTestApp(App):
    bl = list()
    gl = list()
    s = 0
    hzlist = [250,500,750,1000,1500,2000,3000,6000,8000]
    layout = GridLayout(rows=4, padding=[100], spacing=100)

    def do0(self,a):
        self.s = 0
        #self.layout.clear_widgets()
        #return self.layout
        #winsound.Beep(250,1000)
        #self.lay1.clear_widgets()
        #self.layout = GridLayout(rows=4, padding=[100, 200, 100, 100], spacing=50)
        self.build()
    def add_bl1(self,a):
        self.test1 = 'BAD'
        self.do2(a)
    def add_gl1(self,a):
        self.test1 = 'OK'
        self.do2(a)
    def add_bl2(self,a):
        self.test2 = 'BAD'
        self.do3(a)
    def add_gl2(self,a):
        self.test2 = 'OK'
        self.do3(a)
    def add_bl3(self,a):
        self.test3 = 'BAD'
        self.do4(a)
    def add_gl3(self,a):
        self.test3 = 'OK'
        self.do4(a)
    def add_bl4(self,a):
        self.test4 = 'BAD'
        self.do5(a)
    def add_gl4(self,a):
        self.test4 = 'OK'
        self.do5(a)
    def add_bl5(self,a):
        self.test5 = 'BAD'
        self.do6(a)
    def add_gl5(self,a):
        self.test5 = 'OK'
        self.do6(a)
    def add_bl6(self,a):
        self.test6 = 'BAD'
        self.do7(a)
    def add_gl6(self,a):
        self.test6 = 'OK'
        self.do7(a)
    def add_bl7(self,a):
        self.test7 = 'BAD'
        self.do8(a)
    def add_gl7(self,a):
        self.test7 = 'OK'
        self.do8(a)
    def add_bl8(self,a):
        self.test8 = 'BAD'
        self.do9(a)
    def add_gl8(self,a):
        self.test8 = 'OK'
        self.do9(a)
    def add_bl9(self,a):
        self.test9 = 'BAD'
        self.dof()
    def add_gl9(self,a):
        self.test9 = 'OK'
        self.dof()
    def build(self):
        self.layout.clear_widgets()
        button = Button(
            text="START!", font_size = 40, on_press = self.do1,
            background_normal = 'unactive.png' ,background_down = 'active.png',
            size_hint = (0.5, 0.5), pos = (0,0), font_name = 'Arial' )

        wimg = Image(source='ear2.png')
        self.layout.add_widget(wimg)

        #for i in range(0):
            #self.layout.add_widget(Label(text = ''))

        self.layout.add_widget(button)

        return self.layout

    def do1(self, instance):

        self.layout.clear_widgets()
        #winsound.Beep(250, 1000)

        self.s+=1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s-1])+' Hz'
        lb = Label(text = n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl1,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl1,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)

        sound = SoundLoader.load('250.wav')
        sound.play()

        return self.layout

    def do2(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl2,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl2,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('500.wav')
        sound.play()

        return self.layout

    def do3(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl3,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl3,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('750.wav')
        sound.play()

        return self.layout

    def do4(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl4,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl4,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('1000.wav')
        sound.play()

        return self.layout

    def do5(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl5,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl5,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('1500.wav')
        sound.play()

        return self.layout
    def do6(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl6,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl6,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('2000.wav')
        sound.play()

        return self.layout
    def do7(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl7,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl7,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('3000.wav')
        sound.play()

        return self.layout
    def do7(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl7,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl7,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('6000.wav')
        sound.play()

        return self.layout

    def do8(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl8,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl8,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('8000.wav')
        sound.play()

        return self.layout
    def do9(self, instance):
        self.layout.clear_widgets()

        self.s += 1
        n = 'Тест номер ' + str(self.s) + '\n' + ' Частота ' + str(self.hzlist[self.s - 1]) + ' Hz'
        lb = Label(text=n, font_size=50, font_name='Arial')

        button = Button(
            text="OK", font_size=40, on_press=self.add_gl9,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        button1 = Button(
            text="BAD", font_size=40, on_press=self.add_bl9,
            background_normal='unactive.png', background_down='active.png',
            size_hint=(0.5, 0.5), pos=(0, 0), font_name='Arial')
        self.layout.add_widget(lb)
        self.layout.add_widget(button)
        self.layout.add_widget(button1)
        sound = SoundLoader.load('8000.wav')
        sound.play()

        return self.layout

    def dof(self):
        self.layout.clear_widgets()

        #self.layout = GridLayout(rows=10, padding=[50], spacing=50)
        lb1 = Label(text='Частота 250: ' +'\n'+ self.test1, font_size=18, font_name='Arial')
        lb2 = Label(text='Частота 500: ' + '\n'+self.test2, font_size=18, font_name='Arial')
        lb3 = Label(text='Частота 750: ' + '\n'+self.test3, font_size=18, font_name='Arial')
        lb4 = Label(text='Частота 1000: ' + '\n'+self.test4, font_size=18, font_name='Arial')
        lb5 = Label(text='Частота 1500: ' +'\n'+ self.test5, font_size=18, font_name='Arial')
        lb6 = Label(text='Частота 2000: ' + '\n'+self.test6, font_size=18, font_name='Arial')
        lb7 = Label(text='Частота 3000: ' + '\n'+self.test7, font_size=18, font_name='Arial')
        lb8 = Label(text='Частота 6000: ' + '\n'+self.test8, font_size=18, font_name='Arial')
        lb9 = Label(text='Частота 8000: ' + '\n'+self.test9, font_size=18, font_name='Arial')
        lbf = ''

        self.layout.add_widget(lb1)
        self.layout.add_widget(lb2)
        self.layout.add_widget(lb3)
        self.layout.add_widget(lb4)
        self.layout.add_widget(lb5)
        self.layout.add_widget(lb6)
        self.layout.add_widget(lb7)
        self.layout.add_widget(lb8)
        self.layout.add_widget(lb9)

        bt = Button(text = 'MAIN MENU', on_press = self.do0, background_normal='unactive.png', background_down='active.png',size_hint=(5, 0.4))
        self.layout.add_widget(bt)
        return self.layout
        #print(self.gl, self.bl)

EarTestApp().run()

EarTestApp.run()