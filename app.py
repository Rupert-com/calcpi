import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import matplotlib.figure as figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
from layout import layout
from random import uniform
from time import sleep, time, time_ns
from random import seed, random

class Point:
    x: int
    y: int

    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:
        self.x = x
        self.y = y

    # satisfing (x - center_x)² + (y - center_y)² < radius².
    def isWithin(self) -> bool:
        return (self.x - 0.5)**2 + (self.y - 0.5)**2 < 0.5**2
class app:
    iAmount: int = 0
    iAccur: int = 0

    iCaledPi: str

    iPoints: any = []
    Graph: any
    Window: any
    timestamp = str(time())
    wasLastX = False

    def __init__(self) -> None:
        pass

    def calcCPi(self) -> None:
        iQ = 0
        iC = 0
        for cPo in self.iPoints:
            if cPo.isWithin():
                iC += 1
            else:
                iQ += 1

        if iQ != 0 and iC != 0:
            self.Window["pi"].update(f"π = {iC/iQ}")

    def genWindow(self, size=400) -> None:
        self.size = size

        self.Graph = sg.Canvas(key="fig_cv", size=(size, size))
        self.Window = sg.Window(
            "Mit Zufallszahlen Pi bestimmen", layout(self.Graph), finalize=True
        )
        self.Window["Accur"].bind("<Leave>", "_Enter")
        self.Window["Accur"].bind("<Return>", "_Enter")
        self.Window["Amount"].bind("<Return>", "_Enter")
        self.Window["Amount"].bind("<Leave>", "_Enter")

    def drawHistogram(self) -> None:
        fig = figure.Figure()
        ax = fig.add_subplot(1, 1, 1)
        # fig.subplots_adjust(bottom=0.1, left=0.1, top=0.9, right=0.9)
        DPI = fig.get_dpi()
        fig.set_size_inches(self.size / float(DPI), self.size / float(DPI))

        canvas = self.Window["fig_cv"].TKCanvas
        if canvas.children:
            for child in canvas.winfo_children():
                child.destroy()
        #
        cXSmaller_10 = 0
        cXSmaller_09 = 0
        cXSmaller_08 = 0
        cXSmaller_07 = 0
        cXSmaller_06 = 0
        cXSmaller_05 = 0
        cXSmaller_04 = 0
        cXSmaller_03 = 0
        cXSmaller_02 = 0
        cXSmaller_01 = 0

        for cPo in self.iPoints:
            x = cPo.x if self.wasLastX else cPo.y
            if x < 0:
                x = x * (-1)
            if x <= 0.1:
                cXSmaller_01 += 1
            elif x <= 0.2:
                cXSmaller_02 += 1
            elif x <= 0.3:
                cXSmaller_03 += 1
            elif x <= 0.4:
                cXSmaller_04 += 1
            elif x <= 0.5:
                cXSmaller_05 += 1
            elif x <= 0.6:
                cXSmaller_06 += 1
            elif x <= 0.7:
                cXSmaller_07 += 1
            elif x <= 0.8:
                cXSmaller_08 += 1
            elif x <= 0.9:
                cXSmaller_09 += 1
            elif x <= 1:
                cXSmaller_10 += 1

        # ax.set_xlim(0, 1)
        ax.bar(
            [".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", "1"],
            [
                cXSmaller_01,
                cXSmaller_02,
                cXSmaller_03,
                cXSmaller_04,
                cXSmaller_05,
                cXSmaller_06,
                cXSmaller_07,
                cXSmaller_08,
                cXSmaller_09,
                cXSmaller_10,
            ],
        )

        self.Window["Evaluation"].TKButton["text"] = (
            "Diagramm für X anzeigen" if self.wasLastX else "Diagramm für Y anzeigen"
        )

        fig.savefig(
            "Histogramm_" + ("x_" if self.wasLastX else "y_") + self.timestamp + ".png"
        )
        figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="right", fill="both", expand=1)

        self.wasLastX = False if self.wasLastX else True

    def drawGridandPoints(self) -> None:
        print("Drawing Graph")
        fig = figure.Figure()
        ax = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(bottom=0.1, left=0.1, top=0.9, right=0.9)
        DPI = fig.get_dpi()
        fig.set_size_inches(self.size / float(DPI), self.size / float(DPI))

        # Draw Grid and scope
        ax.plot([0, 0, 1, 1, 0], [1, 0, 0, 1, 1], linewidth=0.7, color="blue")
        ax.plot([0, 0], [1.1, -0.1], linewidth=0.7, color="black")
        ax.plot([-0.1, 1.1], [0, 0], linewidth=0.7, color="blue")

        # Draw circle
        t = np.linspace(0, np.pi * 2, 1000)
        ax.plot(np.cos(t)*(0.5)+0.5, np.sin(t)*(0.5)+0.5, color="green")

        # Delete current child elements
        canvas = self.Window["fig_cv"].TKCanvas
        if canvas.children:
            for child in canvas.winfo_children():
                child.destroy()
        #
        xArr = []
        yArr = []
        xArrWithin = []
        yArrWithin = []
        for cPo in self.iPoints:
            if cPo.isWithin():
                xArrWithin.append(cPo.x)
                yArrWithin.append(cPo.y)
            else:
                xArr.append(cPo.x)
                yArr.append(cPo.y)

        ax.plot(xArr, yArr, "ro")
        ax.plot(xArrWithin, yArrWithin, "bo")
        fig.savefig(
            "pi_" + self.timestamp + ".png"
        )
        figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="right", fill="both", expand=1)


    def genPoint(self) -> Point:
        ## seed(9876543457890987654345678987654345*time_ns())
        x= random()
        y= random()
        return Point(x, y)

    iCountRan = 0
    def random(self, seed:int, a=1664525,b=1013904223,m=1000003):
      # a = 1664525
      # b = 1013904223
      # m = 2**32
      cSeed = seed if(type(seed) == type(1)) else seed[0]
      for i in range(m):
          cSeed = (a*cSeed+b)%m
      cfl = float("0."+str(cSeed))
      cRVal = [cSeed, cfl, (cfl*2)-1]        
      self.iCountRan += 1
      print(f"generated random#{self.iCountRan}: {cRVal}")
      return cRVal

    
    def Clear(self) -> None:
        self.iPoints = []

    def Start(self) -> None:
        if self.iAmount > 0:
            for i in range(self.iAmount):
                self.iPoints.append(self.genPoint())

            self.drawGridandPoints()

        elif self.iAccur > 0:
            pass


