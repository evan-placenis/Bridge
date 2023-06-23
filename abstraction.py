from abc import ABC
from implementation import WindowImp
from test import View, Point

class Window(ABC):
    #Private
    imp = WindowImp()
    contents = View()

    def __init__(self, contents: View):
        pass

    #requests handled by window
    def DrawContents():
        pass

    def Open():
        pass

    def Close():
        pass

    def Iconify():
        pass

    def Deiconify():
        pass

    #Requests forwarded to implementation

    def SetOrigin(at: Point):
        pass

    def SetExtent(extent: Point):
        pass

    def Raise():
        pass

    def Lower():
        pass

    def DrawLine():
        pass

    def DrawRect():
        pass

    def DrawText():
        pass

    #protected 
    def GetWindowImp() -> WindowImp:
        pass

    def GetView() -> View:
        pass

    

class ApplicationWindow(Window):
    
    def DrawContents():
        print("draw contents")

class IconWindow(Window):
    def DrawContents():
        print("draw icon window")