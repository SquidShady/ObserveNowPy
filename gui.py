import tkinter as tk
import customtkinter as ctk

# =====================================================================================
# Global Variables
# =====================================================================================


startupWindowWidth = 800
startupWindowHeight = 600

searchFrameWidth = 300
searchFrameHeight = 500

searchResultFrameWidth = 100
searchResultFrameHeight = 100

searchOutputFrameHeight = 100
searchOutputFrameWidth = 100

darkStyling = {
    "padX": 15,
    "padY": 20,
    "borderWidth": 9,
    "borderColor": "#242424",
    "frameColor": "#171717",
    "bgColor": "#0a0a0a",
    "fgColor": "#1f1f1f",
    "entryColor": "#332a20",
    "buttonColor": "#9c4e00",
    "buttonColorPressed": "#703901",
    "buttonColorHighlight": "#ff8c17",

}

lightStyling = {
    "padX": 15,
    "padY": 20,
    "borderWidth": 9,
    "borderColor": "#242424",
    "frameColor": "#171717",
    "bgColor": "#0a0a0a",
    "fgColor": "#1f1f1f",
    "entryColor": "#332a20",
    "buttonColor": "#9c4e00",
    "buttonColorPressed": "#703901",
    "buttonColorHighlight": "#ff8c17",

}

debugWindowFormat = {
    "windowWidth": 400, 
    "windowHeight": 200,
    "padX" : 15,
    "padY" : 20
}




#   This class will be in control of the entire gui; it will hold all of the windows and other objects within itself.
class Gui:
    def __init__ (self):

        self.windows = {}

    def add_window(self, windowName, windowObject):
        self.windows[windowName] = windowObject
    
    def destroy_window(self, windowName):
        if windowName in self.windows:
            window = self.windows[window_id]
            window.destroy()
            del self.windows[windowName]

    def update_windows(self):
        for window in self.windows:
            windowObject = self.windows[window]
            windowObject.updateWindow()



#A window holds frames within itself
class Window(ctk.CTk):
    def __init__(self, windowTitle):
        super().__init__()
        self.geometry(f"{startupWindowWidth}x{startupWindowHeight}")
        self.title(windowTitle)
        self.frameList = dict()

    def add_frame(self, frameName, frameObject):
        self.frameList[frameName] = frameObject

    
    
    #Left off Here 8/1/23
    def updateWindow(self):
        #update window code here
        return True
    


#This is the frame that holds the search button, and searchQuery
class SearchFrame(ctk.CTkFrame):

    def populateFrame(self):
        self.configure(
        width = searchFrameWidth,
        height = searchFrameHeight,
        fg_color = (lightStyling["fgColor"],darkStyling["fgColor"]),
        bg_color = (lightStyling["bgColor"], darkStyling["bgColor"]) 
        )
    
        frameLabel = ctk.CTkLabel(
            master = self,
            text = "Search Frame",
            width = 15,
            height = 15,
            text_color = ("black","white"),
            anchor = 'w'
        )

        searchEntry = ctk.CTkEntry(
            master = self,
            width = 190, 
            height = 30, 
            corner_radius = 2,
            fg_color = darkStyling["entryColor"],
            border_color = darkStyling["borderColor"],
            placeholder_text_color = ("black", "white"),
            placeholder_text = "Comet name or Keyword Here!"
            )
        
        
        searchButton = ctk.CTkButton(
            master = self,
            width = 60,
            height = 20,
            text = "Search",
            corner_radius = 3,
            border_width = 2,
            text_color = ("black","white"),
            hover_color = (lightStyling["buttonColorHighlight"], darkStyling["buttonColorHighlight"]),
            fg_color = (lightStyling["buttonColor"], darkStyling["buttonColor"])
            )

    #   Position Elements on frame.
        self.pack(
            side = 'left',
            anchor = 'n',
            ipady = 3,
            ipadx = 4
            )
        
        frameLabel.grid(
            row = 0,
            column = 0,
            pady = 5,
            padx = 8,
            sticky = 'w'
            )
        searchEntry.grid(
            row = 1,
            column = 0,
            sticky = 'we'
            )
        
        searchButton.grid(

            row = 2,
            column = 0,
            sticky = 'e',
            )
            

class ResultFrame(ctk.CTkFrame):
    
    def populateFrame(self):
