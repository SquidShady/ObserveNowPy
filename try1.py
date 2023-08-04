# TO DO Section
# 1. <COMPLETED> Replace Tk and tk class calls with the CustomTkinter calls
# 2. Make a Calculations class to have the necessary resultParameter calculations for the output graph. 
# 3. Format Frames on base Window

#




# =====================================================================================
# Import Dependencies
# =====================================================================================

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import argparse, sys
# import os, sys


# =====================================================================================
# Creating an Argument Parser  ---------- When you launch the script you can pass it parameters.
# =====================================================================================

def getStartupArgs():
    
    parser = argparse.ArgumentParser(description='Description of Script')

    # Add arguments to parser
    parser.add_argument('-c', '--comet', type=str, help='Name of Comet as a String')
    parser.add_argument('-n', '--number', type=int, help='Integer number of results you want to use')
    parser.add_argument('-f', '--file', type=str, help='Separate File per Result "Separate/Together"')

    # Parse the arguments
    userargs = parser.parse_args()
    
    # Access the argument values
    results = PossibleArguments()
    results.cometString = userargs.comet
    results.numberOfResults = userargs.number
    
    if userargs.file == "Separate":
        results.separateOrNot = True
    elif userargs.file == "Together":
        results.separateOrNot = False
    else:
        results.separateOrNot = None

#   Debug User Arguments Input and logical Output    
    # print(userargs.comet, " Name \n", userargs.number, " Num \n", userargs.file, " Sep \n")
    # print(results.cometString, " Name \n", results.numberOfResults, " Num \n", results.separateOrNot, " Sep ")
    
    return results

# Search frame needs:
#   1. SearchBar Query (CTkEntry)
#   2. Number of Search Results Query (CTkEntry) 
#   3. 

#LEFT OFF HERE 07/07
def searchFrameFormat(frame):

#   Create Elements of frame
    frame.configure(
        width = searchFrameWidth,
        height = searchFrameHeight,
        fg_color = (lightStyling["fgColor"],darkStyling["fgColor"]),
        bg_color = (lightStyling["bgColor"], darkStyling["bgColor"]) 
        )
    
    frameLabel = ctk.CTkLabel(
        master = frame,
        text = "Search Frame",
        width = 15,
        height = 15,
        text_color = ("black","white"),
        anchor = 'w'
    )

    searchEntry = ctk.CTkEntry(
        master = frame,
        width = 190, 
        height = 30, 
        corner_radius = 2,
        fg_color = darkStyling["entryColor"],
        border_color = darkStyling["borderColor"],
        placeholder_text_color = ("black", "white"),
        placeholder_text = "Comet name or Keyword Here!"
        )
    
    
    searchButton = ctk.CTkButton(
        master = frame,
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
    frame.pack(
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
    


def resultFrameFormat(frame):
    frame.configure(
        width = searchResultFrameWidth,
        height = searchResultFrameHeight
        )
    



  


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



# =====================================================================================
# Main block of code, runs on startup
# =====================================================================================

def main():

    passedArgs = PossibleArguments()
    passedArgs = getStartupArgs()

    #Checks if No Arguments passed, if True: makes gui
    if passedArgs.cometString == None or passedArgs.numberOfResults == None or passedArgs.separateOrNot == None:
        print("Why")
        rootWindow = Window("A P P L I C A T I O N")
        print(darkStyling["bgColor"])
        rootWindow.configure(fg_color = ( f"{lightStyling['bgColor']}" , f"{darkStyling['bgColor']}" ) )
        rootWindow.populateSearchWindow()

    #Tries to update window, and or calculate and either fails, or succeeds returning True/False then exits
    try:
        print("why2")
        rootWindow.mainloop()
        return True
    except not isinstance(passedArgs.separateOrNot,str):
        return False
    finally:
        sys.exit()




# =====================================================================================
# CLASSES
# =====================================================================================

class PossibleArguments:
    def __init__(self, cometString = "None", separateOrNot = False, numberOfResults = 1):
        self.cometString = cometString
        self.separateOrNot = separateOrNot
        self.numberOfResults = numberOfResults

# This class will hold all of the information about a search result that is necessary
#       I am still unsure about what parameters I will need... 07/06
class Comet:
    def __init__(self):
        self.cometName = None
        self.rightAscension = None
        self.declination = None
        self.cometMagnitude = None
        self.periHelionDistance = None
        self.apHelionDistance = None
        self.distanceToEarth = None
        self.cometPhase = None

    # def updateCometInfo(cometInfo):
        



class Window(ctk.CTk):
    def __init__(self, windowTitle):
        super().__init__()
        self.geometry(f"{startupWindowWidth}x{startupWindowHeight}")
        self.title(windowTitle)
        self.frameList = list()

    def populateSearchWindow(self):
        
        self.searchFrame = ctk.CTkFrame(master = self)
        self.searchResultFrame = ctk.CTkFrame(master = self)
        self.searchOutputFrame = ctk.CTkFrame(master = self)

        searchFrameFormat(self.searchFrame)

        self.frameList.append(self.searchFrame)
        self.frameList.append(self.searchResultFrame)
        self.frameList.append(self.searchOutputFrame)




#   SearchFrame is a child class of CTkFrame, with some added variables that will make it easier.
#   I feel that this as a class object will make it easier to have the data needed accessible and the ability to enact methods on it directly in one place.
class SearchFrame(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.searchQuery = str()

    #def formatFrame(self):
        

    

      













#This ensures that the script is not being run while imported anywhere, and only when the file is run directly.

if __name__ == "__main__":
    main()
