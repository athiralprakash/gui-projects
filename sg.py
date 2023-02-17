import PySimpleGUI as sg

feet_label = sg.Text("Enter the feet")
inputbox1 = sg.Input()

inches_label = sg.Text("Enter the inches")
inptputbox2 = sg.Input()

converter_button = sg.Button("Convert")
output_box = sg.Output(78)

window = sg.Window("converter", layout=[
    [feet_label, inputbox1],
    [inches_label, inptputbox2],
    [converter_button]])
window.read()
window.close()
