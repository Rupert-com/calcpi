import PySimpleGUI as sg
import os.path


def layout(graph):

    display = [
        [sg.Canvas(key="controls_cv")],
        [graph],
        [sg.Text("π", key="pi", size=(60, 1), justification="center")],
        [sg.Text("", size=(60, 1), justification="center")],
    ]
    controller = [
        [
            sg.Text("Anzahl Zufallszahlen", size=(30, 1), justification="center"),
            sg.InputText(key="Amount"),
        ],
        [sg.Text("oder", size=(30, 1), justification="center")],
        [
            sg.Text("Genauigkeit", size=(30, 1), justification="center"),
            sg.InputText(key="Accur"),
        ],
        [sg.Button("Start", key="Start"), sg.Button("Beenden", key="Exit")],
        [sg.Button("Datenauswertung starten", key="Evaluation")],
    ]
    layout = [
        [
            sg.Column(display),
            sg.VSeperator(),
            sg.Column(controller),
        ]
    ]

    return layout
