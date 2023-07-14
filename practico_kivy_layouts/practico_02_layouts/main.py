from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class PageLayoutScreen(Screen):
    pass

class GridLayoutScreen(Screen):
    '''
        organiza los widgets en una cuadricula,
        tiene dos propiedades que te permiten posicionar los widgets:
            cols: cantidad de columnas
            rows: cantidad de filas
    '''
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-bt" # right to left, bottom to top
        # add some padding 
        # create a grid widget with 4   columns 
        grid = GridLayout(cols=9,spacing=dp(10),padding=dp(10))
        for i in range(0,95): # can display all without a scrollview
            b = Button(text=str(i+1),size_hint=(None,None),size=(dp(40),dp(40)),background_color=(255/255, 208/255, 73/255, 1))
            grid.add_widget(b)
        # create a scroll view and add the grid widget to the scroll view
        scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height +100))
        scrollview.add_widget(grid)
        # add the scroll view to this layout
        self.add_widget(scrollview) 

class StackLayoutScreen(Screen):
    '''
        apila los widgets uno encima del otro,
        tiene dos propiedades que te permiten posicionar los widgets:
            orientation: lr-tb, rl-tb, lr-bt, rl-bt
            padding: espacio entre los widgets
    '''
    pass

class AnchorLayoutScreen(Screen):
    '''
        ocupa todo el espacio disponible y posiciona los widgets en el mismo lugar,
        tiene dos propiedades que te permiten posicionar los widgets:
            anchor_x: left, center, right
            anchor_y: top, center, bottom
    '''
    pass

class MainWindowManager(ScreenManager):
    pass

sm = Builder.load_file('widget.kv')

class MyMainApp(App):
    currentUser = 444
    def build(self):
        Window.clearcolor = (245/255, 245/255, 245/255, 1)
        Window.size = (450, 680)
        return sm       

MyMainApp().run()