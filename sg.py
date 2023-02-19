import PySimpleGUI as sg

feet_label = sg.Text("Enter the feet")
inputbox1 = sg.Input(key="feet_input")

inches_label = sg.Text("Enter the inches")
inptputbox2 = sg.Input(key="inches input")

converter_button = sg.Button("Convert",key=("converted value button "))
output_box = sg.Output(key="output",text_color="green")

window = sg.Window("converter", layout=[
    [feet_label, inputbox1],
    [inches_label, inptputbox2],
    [converter_button]])
while True:

    event,values=window.read()
    print(event, value)



window.close()
