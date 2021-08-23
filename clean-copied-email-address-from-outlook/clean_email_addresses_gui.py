from PySimpleGUI.PySimpleGUI import CalendarButton
import clean_email_addresses as cea
import PySimpleGUI as sg
import webbrowser



input_col = [
    [sg.Text("Paste emails")],
    [sg.Input(size=(20, 200), key='-TEXTBOX-')],
    [sg.Button('Submit')],
]

out_col_name = [
    [sg.Text("Names")],
    [sg.Listbox(values=[], enable_events=True, size=(20, 20), key="-EMAIL-NAME-LIST-")],
]

out_col_adres = [
    [sg.Text("Adresses")],
    [sg.Listbox(values=[], enable_events=True, size=(20, 20), select_mode='extended', key="-EMAIL-ADRES-LIST-")],
]

out_col_no_email = [
    [sg.Text("Names without email")],
    [sg.Listbox(values=[], enable_events=True, size=(20, 20), key="-EMAIL-NO-LIST-")],
]


# ----- Full layout -----
layout = [
    [
        sg.Column(input_col),
        sg.VSeperator(),
        sg.Column(out_col_name),
        sg.VSeperator(),
        sg.Column(out_col_adres),
        sg.VSeperator(),
        sg.Column(out_col_no_email),
    ]
]

window = sg.Window("Clean mails", layout,)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        input = values["-TEXTBOX-"]
        if input != "":
            data = cea.get_emails(input)
            window["-EMAIL-NAME-LIST-"].update(data[0])
            window["-EMAIL-ADRES-LIST-"].update(data[1])
            window["-EMAIL-NO-LIST-"].update(data[2])
            sg.Popup(f'Emails: {len(data[0])}, People without email: {len(data[2])}')
            webbrowser.open(cea.file)
        else:
            sg.Popup('Please paste some emails')
   

window.close()