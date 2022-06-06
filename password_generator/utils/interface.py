import PySimpleGUI as sg


def main_menu():
    sg.theme("DarkAmber")

    layout = [

        [sg.Button("LETTERS ONLY", pad=(90, 20))],

        [sg.Button("LETTERS AND NUMBERS", pad=(65, 20))],

        [sg.Button("LETTERS, NUMBERS AND SYMBOLS", pad=(30, 20))],

        [sg.Button("HEXADECIMAL", pad=(90, 20))],

        [sg.Button("UUID", pad=(115, 20))],

        [sg.Button("Close", button_color="white")]

    ]

    return sg.Window("Main menu", layout=layout, finalize=True)


def letters_only():
    sg.theme("DarkAmber")

    layout = [

        [sg.Text("Choose the amount of characters for the password"), sg.Button("5", button_color="white"),
         sg.Button("8", button_color="white"), sg.Button("10", button_color="white")],

        [sg.Text("PASSWORD:"), sg.Text(key="onlyletters", size=40)],

        [sg.Button("Back", button_color="white"), sg.Button("Ok", button_color="white")]

    ]

    return sg.Window("LETTERS ONLY", layout=layout, finalize=True)


def letters_nums():
    sg.theme("DarkAmber")

    layout = [

        [sg.Text("Choose the amount of characters for the password"), sg.Button("5", button_color="white"),
         sg.Button("8", button_color="white"), sg.Button("10", button_color="white")],

        [sg.Text("PASSWORD:"), sg.Text(key="lettersandnums", size=40)],

        [sg.Button("Back", button_color="white"), sg.Button("Ok", button_color="white")]

    ]

    return sg.Window("LETTERS AND NUMBERS", layout=layout, finalize=True)


def letters_nums_symbs():
    sg.theme("DarkAmber")

    layout = [

        [sg.Text("Choose the amount of characters for the password"), sg.Button("5", button_color="white"),
         sg.Button("8", button_color="white"), sg.Button("10", button_color="white")],

        [sg.Text("PASSWORD"), sg.Text(key="lettersnumsymbs")],

        [sg.Button("Back", button_color="white"), sg.Button("Ok", button_color="white")]

    ]

    return sg.Window("LETTERS, NUMBERS AND SYMBOLS", layout=layout, finalize=True)


def hexadecimal():
    sg.theme("DarkAmber")

    layout = [

        [sg.Text("Choose the amount of characters for the password"), sg.Button("SMALL", button_color="white"),
         sg.Button("MEDIUM", button_color="white"), sg.Button("LARGE", button_color="white")],

        [sg.Text("PASSWORD"), sg.Text(key="hexadecimal")],

        [sg.Button("Back", button_color="white"), sg.Button("Ok", button_color="white")]

    ]

    return sg.Window("HEXADECIMAL", layout=layout, finalize=True)


def uuid_ui():
    sg.theme("DarkAmber")

    layout = [

        [sg.Text("PASSWORD"), sg.Text(key="uuid", size=35)],

        [sg.Button("Display", button_color="white"), sg.Button("Back", button_color="white"),
         sg.Button("Ok", button_color="white")]

    ]

    return sg.Window("UUID", layout=layout, finalize=True)
