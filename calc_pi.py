import PySimpleGUI as sg
import os.path
from app import app


app = app()
app.genWindow()
app.drawGridandPoints()
while True:
    event, values = app.Window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Amount_Enter":
        try:
            app.iAmount = int(values["Amount"])
        except Exception as e:
            pass
        #  sg.Print(f'An error happened.  Here is the info:', e)
    elif event == "Accur_Enter":
        try:
            app.iAccur = int(values["Accur"])
        except Exception as e:
            pass
        #  sg.Print(f'An error happened.  Here is the info:', e)

    elif event == "Start":
        app.Clear()
        app.Start()
        app.calcCPi()
        # x = np.linspace(0, 2 * np.pi)
        # y = np.sin(x)
        pass
    elif event == "Evaluation":
        app.drawHistogram()


app.Window.close()
