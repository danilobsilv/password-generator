from utils.interface import *
from utils.functs.functs5 import *
from utils.functs.functs8 import *
from utils.functs.functs10 import *

window1, window2, window3, window4, window5, window6 = main_menu(), None, None, None, None, None

while True:
    window, events, values = sg.read_all_windows()

    # main menu
    if window == window1 and events == sg.WIN_CLOSED:
        break
    if window == window1 and events == "Close":
        break
    if window == window1 and events == "LETTERS ONLY":
        window2 = letters_only()
        window1.hide()
    if window == window1 and events == "LETTERS AND NUMBERS":
        window3 = letters_nums()
        window1.hide()
    if window == window1 and events == "LETTERS, NUMBERS AND SYMBOLS":
        window4 = letters_nums_symbs()
        window1.hide()
    if window == window1 and events == "HEXADECIMAL":
        window5 = hexadecimal()
        window1.hide()
    if window == window1 and events == "UUID":
        window6 = uuid_ui()
        window1.hide()

    # only letters window
    if window == window2 and events == sg.WIN_CLOSED:
        break
    if window == window2 and events == "Ok":
        break
    if window == window2 and events == "Back":
        window2.hide()
        window1.un_hide()
    if window == window2 and events == "5":
        window2["onlyletters"].update(five_generate_only_letter())
    if window == window2 and events == "8":
        window2["onlyletters"].update(eight_generate_only_letter())
    if window == window2 and events == "10":
        window2["onlyletters"].update(ten_generate_only_letter())

    # letters and numbers window
    if window == window3 and events == sg.WIN_CLOSED:
        break
    if window == window3 and events == "Ok":
        break
    if window == window3 and events == "Back":
        window3.hide()
        window1.un_hide()
    if window == window3 and events == "5":
        window3["lettersandnums"].update(five_generate_letters_nums())
    if window == window3 and events == "8":
        window3["lettersandnums"].update(eight_generate_letters_nums())
    if window == window3 and events == "10":
        window3["lettersandnums"].update(ten_generate_letters_nums())

    # letters, numbers and symbols window
    if window == window4 and events == sg.WIN_CLOSED:
        break
    if window == window4 and events == "Ok":
        break
    if window == window4 and events == "Back":
        window4.hide()
        window1.un_hide()
    if window == window4 and events == "5":
        window4["lettersnumsymbs"].update(five_generate_letters_nums_symbols())
    if window == window4 and events == "8":
        window["lettersnumsymbs"].update(eight_generate_letters_nums_symbols())
    if window == window4 and events == "10":
        window["lettersnumsymbs"].update(ten_generate_letters_nums_symbols())

    # hexadecimal window
    if window == window5 and events == sg.WIN_CLOSED:
        break
    if window == window5 and events == "Ok":
        break
    if window == window5 and events == "Back":
        window5.hide()
        window1.un_hide()
    if window == window5 and events == "SMALL":
        window5["hexadecimal"].update(five_generate_hexadecimal())
    if window == window5 and events == "MEDIUM":
        window5["hexadecimal"].update(eight_generate_hexadecimal())
    if window == window5 and events == "LARGE":
        window["hexadecimal"].update(ten_generate_hexadecimal())

    # UUID window
    if window == window6 and events == sg.WIN_CLOSED:
        break
    if window == window6 and events == "Ok":
        break
    if window == window6 and events == "Back":
        window6.hide()
        window1.un_hide()
    if window == window6 and events == "Display":
        window6["uuid"].update(generate_uuid())
