# all imports
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import tkinter.font as tkfont
from ctypes import windll
import random
from datetime import date

# config for root window
app = Tk()
app.title('Chord Crafter')
app.geometry("1275x665")
app.configure(background='light blue')

# font config
font_button = tkfont.Font(family = 'courier new bold italic', size = 14)
font_button_library = tkfont.Font(family = 'courier new italic', size = 13)
font_message = tkfont.Font(family = 'courier new bold italic', size = 16)
windll.shcore.SetProcessDpiAwareness(1)

# create message box and place on screen / create welcome message
message_box  = Frame(app, bd = 5, relief = SUNKEN, height = 646, width = 908)
message_box.grid(row = 0, column = 1, rowspan = 6,padx=4)
message_box.grid_propagate(0)
welcome_label = Label(message_box,text='Use the buttons on the left to create chord progressions!', font=font_message, fg='green')
welcome_label.grid(row=0,column=0)

# variables for filter checkboxes
var1 = IntVar (value=1)   # C Major
var2 = IntVar (value=1)   # G Major
var3 = IntVar (value=1)   # D Major
var4 = IntVar (value=1)   # A Major
var5 = IntVar (value=1)   # E Major
var6 = IntVar (value=1)   # B Major
var7 = IntVar (value=1)   # F# Major
var8 = IntVar (value=1)   # Db Major
var9 = IntVar (value=1)   # Ab Major
var10 = IntVar (value=1)  # Eb Major
var11 = IntVar (value=1)  # Bb Major
var12 = IntVar (value=1)  # F Major
var13 = IntVar (value=1)  # Major
var14 = IntVar (value=1)  # Minor
var15 = IntVar (value=1)  # Lydian
var16 = IntVar (value=1)  # Mixolydian
var17 = IntVar (value=1)  # Dorian
var18 = IntVar (value=1)  # Phrygian

# functions to route filter IDs out
def route_key():
    var_code_key = [var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),
                   var9.get(),var10.get(),var11.get(),var12.get()]
    return var_code_key
def route_mode():
    var_code_mode = [var13.get(),var14.get(),var15.get(),var16.get(),var17.get(),var18.get()]
    return var_code_mode

# function for random chord progression
def prog():
    # clears the frame
    for widgets in message_box.winfo_children():
        widgets.destroy ()

    # dictionaries and filter ids
    prog_code_key = route_key()
    prog_code_mode = route_mode()
    prog_chords = {  # Chords of a key listed in order of circle of fifths
        1: ["C", "Dm", "Em", "F", "G", "Am", "B°"],  # C
        2: ["G", "Am", "Bm", "C", "D", "Em", "F#°"],  # G
        3: ["D", "Em", "F#m", "G", "A", "Bm", "C#°"],  # D
        4: ["A", "Bm", "C#m", "D", "E", "F#m", "G#°"],  # A
        5: ["E", "F#m", "G#m", "A", "B", "C#m", "D#°"],  # E
        6: ["B", "C#m", "D#m", "E", "F#", "G#m", "A#°"],  # B
        7: ["F#", "G#m", "A#m", "B", "C#", "D#m", "F°"],  # F#
        8: ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C°"],  # Db
        9: ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "G°"],  # Ab
        10: ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "D°"],  # Eb
        11: ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "A°"],  # Bb
        12: ["F", "Gm", "Am", "Bb", "C", "Dm", "E°"]  # F
    }
    prog_modes = {  # Names of all the different scales
        1: ["C Major", "C Minor", "C Lydian", "C Mixolydian", "C Dorian", "C Phrygian"],
        2: ["G Major", "G Minor", "G Lydian", "G Mixolydian", "G Dorian", "G Phrygian"],
        3: ["D Major", "D Minor", "D Lydian", "D Mixolydian", "D Dorian", "D Phrygian"],
        4: ["A Major", "A Minor", "A Lydian", "A Mixolydian", "A Dorian", "A Phrygian"],
        5: ["E Major", "E Minor", "E Lydian", "E Mixolydian", "E Dorian", "E Phrygian"],
        6: ["B Major", "B Minor", "B Lydian", "B Mixolydian", "B Dorian", "B Phrygian"],
        7: ["F# Major", "F# Minor", "F# Lydian", "F# Mixolydian", "F# Dorian", "F# Phrygian"],
        8: ["Db Major", "Db Minor", "Db Lydian", "Db Mixolydian", "Db Dorian", "Db Phrygian"],
        9: ["Ab Major", "Ab Minor", "Ab Lydian", "Ab Mixolydian", "Ab Dorian", "Ab Phrygian"],
        10: ["Eb Major", "Eb Minor", "Eb Lydian", "Eb Mixolydian", "Eb Dorian", "Eb Phrygian"],
        11: ["Bb Major", "Bb Minor", "Bb Lydian", "Bb Mixolydian", "Bb Dorian", "Bb Phrygian"],
        12: ["F Major", "F Minor", "F Lydian", "F Mixolydian", "F Dorian", "F Phrygian"]}
    prog_mode_order = {  # Order for switching chords to different modes
        1: [0, 1, 2, 3, 4, 5, 6],  # Major
        2: [5, 6, 0, 1, 2, 3, 4],  # Minor
        3: [3, 4, 5, 6, 0, 1, 2],  # Lydian
        4: [4, 5, 6, 0, 1, 2, 3],  # Mixolydian
        5: [1, 2, 3, 4, 5, 6, 0],  # Dorian
        6: [2, 3, 4, 5, 6, 0, 1],  # Phrygian
    }
    prog_chord_subs = {  # These are the chords that the program can use to make the progressions more interesting
        1: ["Cm", "D", "E", "Fm", "Gm", "A", "B"],  # C
        2: ["Gm", "A", "B", "Cm", "Dm", "E", "F#"],  # G
        3: ["Dm", "E", "F#", "Gm", "Am", "B", "C#"],  # D
        4: ["Am", "B", "C#", "Dm", "Em", "F#", "G#"],  # A
        5: ["Em", "F#", "G#", "Am", "Bm", "C#", "D#"],  # E
        6: ["Bm", "C#", "D#", "Em", "F#m", "G#", "A#"],  # B
        7: ["F#m", "G#", "A#", "Bm", "C#m", "D#", "F"],  # F#
        8: ["Dbm", "Eb", "F", "Gbm", "Abm", "Bb", "C"],  # Db
        9: ["Abm", "Bb", "C", "Dbm", "Ebm", "F", "G"],  # Ab
        10: ["Ebm", "F", "G", "Abm", "Bbm", "C", "D"],  # Eb
        11: ["Bbm", "C", "D", "Ebm", "Fm", "G", "A"],  # Bb
        12: ["Fm", "G", "A", "Bbm", "Cm", "D", "E"]  # F
    }

    # generates codes to filter keys and modes
    key_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for ele in range (0, 12):
        if prog_code_key[ele] == 0:
            key_id[ele] = 0
    mode_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for ele in range (0, 6):
        if prog_code_mode[ele] == 0:
            mode_id[ele] = 0

    # generates the key and mode numbers
    key_id = list (filter (lambda x: x != 0, key_id))
    mode_id = list (filter (lambda x: x != 0, mode_id))
    if key_id == 1:
        key_length = 1
    else:
        key_length = len (key_id)
    key_selection = random.randint (1, key_length)
    key = key_id[key_selection - 1]
    if mode_id[0] > 1:
        for ele in range (7, 13):
            mode_id = list (filter (lambda x: x != ele, mode_id))
    if mode_id == 1:
        mode_length = 1
    else:
        mode_length = len (mode_id)
    mode_selection = random.randint (1, mode_length)
    mode = mode_id[mode_selection - 1]
    if mode > 6:
        mode = 1

    # alters key to allow for mode changes
    if mode == 1:  # major
        key_adjust = 0
    if mode == 2:  # minor
        for ele in range (1, 13):
            if key in range (1, 4):
                key_adjust = 9
            if key in range (4, 13):
                key_adjust = -3
    if mode == 3:  # lydian
        if key in range (1, 12):
            key_adjust = 1
        if key == 12:
            key_adjust = -11
    if mode == 4:  # mixolydian
        if key == 1:
            key_adjust = 11
        if key in range (2, 13):
            key_adjust = -1
    if mode == 5:  # dorian
        if key in range (1, 3):
            key_adjust = 10
        if key in range (3, 13):
            key_adjust = -2
    if mode == 6:  # phrygian
        if key in range (1, 5):
            key_adjust = 8
        if key in range (5, 13):
            key_adjust = -4

    # gives all info for user to be displayed
    key_mode_change = key + key_adjust
    global key_name
    key_name = prog_modes[key][mode - 1]
    chord_choice = prog_chords[key_mode_change]
    sub_choice = prog_chord_subs[key_mode_change]

    # These are the chord arrays the algorithm will choose from to make the prog
    chord_selection = [chord_choice[x] for x in prog_mode_order[mode]]
    sub_chord_selection = [sub_choice[x] for x in prog_mode_order[mode]]

    # function for enter key within prog
    def prog_enter():
        # clear labels and unbind the enter key
        proglabel_1.destroy ()
        proglabel_2.destroy ()
        app.unbind ('<Return>')

        # takes user input and generates the chord progression
        global chord_num
        chord_num = prog_entry.get ().lower ()
        if chord_num in ["rand","random",""]:
            chord_num = int (random.randint (2, 7))
        else:
            try:
                chord_num = int(chord_num)
            except:
                messagebox.showerror ('error', 'Enter a valid input')
                prog()

        # labels all available chords
        i = chord_selection[0]
        ii = chord_selection[1]
        iii = chord_selection[2]
        iv = chord_selection[3]
        v = chord_selection[4]
        vi = chord_selection[5]
        vii = chord_selection[6]
        sub_i = sub_chord_selection[0]
        sub_ii = sub_chord_selection[1]
        sub_iii = sub_chord_selection[2]
        sub_iv = sub_chord_selection[3]
        sub_v = sub_chord_selection[4]
        sub_vi = sub_chord_selection[5]
        sub_vii = sub_chord_selection[6]

        # builds the first two chords of the prog
        rand_second = random.randint (1, 6)
        chord_first = i
        chord_second = chord_selection[rand_second]
        global chord_progression
        chord_progression = [chord_first, chord_second]

        if chord_num in [1,2]:
            # bypasses the loop if the user only wants 1 or 2 chords
            proglabel_3 = Label (message_box, text='Your chord progression is in the key of ' + key_name, font=font_message)
            proglabel_4 = Label (message_box, text="Use these chords: " + ' '.join (chord_progression), font=font_message, fg='green')
            proglabel_3.grid (row=2, column=0, sticky='w')
            proglabel_4.grid (row=3, column=0, sticky='w')
        else:
            # builds the chord progression
            # 1. starts with the first two chords and decides which chords should go next
            #    Uses music theory to make good decisions for next chord
            # 2. Uses the new chord it picked to go through decision process again
            for change in range (1, chord_num - 1):
                # all random nums
                rand_option = random.randint (1, 3)
                rand_prop = random.randint (1, 10)
                rand = random.randint (0, 13)
                rand_selection = [i, ii, iii, iv, v, vi, vii, sub_i, sub_ii, sub_iii, sub_iv, sub_v, sub_vi, sub_vii]

                if chord_progression[change] == i:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = iv
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = v
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            chord_progression_new = vi
                        if rand_prop == 10:
                            chord_progression_new = vii
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = ii
                        if rand_prop in [6,7,8,9,10]:
                            chord_progression_new = iii

                if chord_progression[change] == ii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = iv
                        if rand_prop in [8, 10]:
                            chord_progression_new = sub_vi
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = v
                        if rand_prop in [9, 10]:
                            chord_progression_new = sub_v
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = iv
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = rand_selection[rand]

                if chord_progression[change] == iii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = vi
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = sub_vi
                    if rand_option == 2:
                        if rand_prop == 1:
                            chord_progression_new = vii
                        if rand_prop in [2, 3]:
                            chord_progression_new = sub_vii
                        if rand_prop in [4, 5, 6, 7, 8, 9, 10]:
                            chord_progression_new = v
                    if rand_option == 3:
                        chord_progression_new = v

                if chord_progression[change] == iv:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = i
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_iv
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = v
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_iii
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = ii
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = rand_selection[rand]

                if chord_progression[change] == v:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = i
                        if rand in [9, 10]:
                            chord_progression_new = vii
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = iii
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_iii
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = vi
                        if rand_prop in [9, 10]:
                            chord_progression_new = sub_vii

                if chord_progression[change] == vi:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = ii
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = sub_ii
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = iv
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_iv
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = i
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = v

                if chord_progression[change] == vii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = vi
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_vi
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = i
                        if rand_prop in [9, 10]:
                            chord_progression_new = sub_i
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = iii
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_iii

                if chord_progression[change] == sub_i:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = v
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_v
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = iv
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_iv
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            chord_progression_new = vi
                        if rand_prop == 10:
                            chord_progression_new = vii

                if chord_progression[change] == sub_ii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = v
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_v
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4]:
                            chord_progression_new = ii
                        if rand_prop in [5, 6, 7, 8, 9, 10]:
                            chord_progression_new = iii
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = vi
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = sub_vi

                if chord_progression[change] == sub_iii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = vi
                        if rand_prop in [9, 10]:
                            chord_progression_new = sub_vii
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = iii
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = sub_vi
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = i
                        if rand_prop in [6, 7, 8, 9, 10]:
                            chord_progression_new = v

                if chord_progression[change] == sub_iv:
                    if rand_option == 1:
                        if rand in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = i
                        if rand in [8, 9, 10]:
                            chord_progression_new = sub_i
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = v
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = sub_v
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = vi
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = rand_selection[rand]

                if chord_progression[change] == sub_v:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7, 8]:
                            chord_progression_new = i
                        if rand_prop in [9, 10]:
                            chord_progression_new = sub_i
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = ii
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_ii
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6, 7]:
                            chord_progression_new = vi
                        if rand_prop in [8, 9, 10]:
                            chord_progression_new = rand_selection[rand]

                if chord_progression[change] == sub_vi:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = i
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = vi
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = ii
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_ii
                    if rand_option == 3:
                        chord_progression_new = rand_selection[rand]

                if chord_progression[change] == sub_vii:
                    if rand_option == 1:
                        if rand_prop in [1, 2, 3, 4, 5]:
                            chord_progression_new = iii
                        if rand_prop in [5, 6, 7, 8, 9, 10]:
                            chord_progression_new = sub_iii
                    if rand_option == 2:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = i
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = vi
                    if rand_option == 3:
                        if rand_prop in [1, 2, 3, 4, 5, 6]:
                            chord_progression_new = iii
                        if rand_prop in [7, 8, 9, 10]:
                            chord_progression_new = sub_vi
                chord_progression.append (chord_progression_new)

        # This will display the chords to the user
        proglabel_3 = Label (message_box, text='Your chord progression is in the key of ' + key_name, font=font_message)
        proglabel_4 = Label (message_box, text="Use these chords: " + ' '.join (chord_progression), font=font_message, fg='green')
        proglabel_3.grid (row=2, column=0, sticky='w')
        proglabel_4.grid (row=3, column=0, sticky='w')

    # asks the user for num of chords and binds enter key
    proglabel_1 = Label (message_box, text='How many chords would you like in your progression?', font=font_message)
    proglabel_2 = Label (message_box, text='Hit "Enter" for random amount', font=font_message)
    prog_entry = Entry (message_box, font=font_message)
    prog_enter_button = ttk.Button(message_box, command=prog_enter)
    app.bind ('<Return>', lambda event: prog_enter ())
    chord_num = prog_entry.get()

    # place labels / entry box in the message box
    proglabel_1.grid (row=0, column=0, sticky='w')
    proglabel_2.grid (row=1, column=0, sticky='w')
    prog_entry.grid (row=2, column=0, sticky='w', padx = 5, pady =5)
    prog_enter_button.grid_forget ()

# function for random key button
def rand_key():
    # clears the frame
    for widgets in message_box.winfo_children():
        widgets.destroy ()

    # dictionaries and filter ids
    rand_code_key=route_key ()
    rand_code_mode=route_mode ()
    rand_chords={  # Chords of a key listed in order of circle of fifths
            1: ["C", "Dm", "Em", "F", "G", "Am", "B°"],  # C
            2: ["G", "Am", "Bm", "C", "D", "Em", "F#°"],  # G
            3: ["D", "Em", "F#m", "G", "A", "Bm", "C#°"],  # D
            4: ["A", "Bm", "C#m", "D", "E", "F#m", "G#°"],  # A
            5: ["E", "F#m", "G#m", "A", "B", "C#m", "D#°"],  # E
            6: ["B", "C#m", "D#m", "E", "F#", "G#m", "A#°"],  # B
            7: ["F#", "G#m", "A#m", "B", "C#", "D#m", "F°"],  # F#
            8: ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C°"],  # Db
            9: ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "G°"],  # Ab
            10: ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "D°"],  # Eb
            11: ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "A°"],  # Bb
            12: ["F", "Gm", "Am", "Bb", "C", "Dm", "E°"]  # F
        }
    rand_modes={  # Names of all the different scales
            1: ["C Major", "C Minor", "C Lydian", "C Mixolydian", "C Dorian", "C Phrygian"],
            2: ["G Major", "G Minor", "G Lydian", "G Mixolydian", "G Dorian", "G Phrygian"],
            3: ["D Major", "D Minor", "D Lydian", "D Mixolydian", "D Dorian", "D Phrygian"],
            4: ["A Major", "A Minor", "A Lydian", "A Mixolydian", "A Dorian", "A Phrygian"],
            5: ["E Major", "E Minor", "E Lydian", "E Mixolydian", "E Dorian", "E Phrygian"],
            6: ["B Major", "B Minor", "B Lydian", "B Mixolydian", "B Dorian", "B Phrygian"],
            7: ["F# Major", "F# Minor", "F# Lydian", "F# Mixolydian", "F# Dorian", "F# Phrygian"],
            8: ["Db Major", "Db Minor", "Db Lydian", "Db Mixolydian", "Db Dorian", "Db Phrygian"],
            9: ["Ab Major", "Ab Minor", "Ab Lydian", "Ab Mixolydian", "Ab Dorian", "Ab Phrygian"],
            10: ["Eb Major", "Eb Minor", "Eb Lydian", "Eb Mixolydian", "Eb Dorian", "Eb Phrygian"],
            11: ["Bb Major", "Bb Minor", "Bb Lydian", "Bb Mixolydian", "Bb Dorian", "Bb Phrygian"],
            12: ["F Major", "F Minor", "F Lydian", "F Mixolydian", "F Dorian", "F Phrygian"]}
    rand_mode_order={ #Order for switching chords to different modes
            1: [0,1,2,3,4,5,6],  #Major
            2: [5,6,0,1,2,3,4],  #Minor
            3: [3,4,5,6,0,1,2],  #Lydian
            4: [4,5,6,0,1,2,3],  #Mixolydian
            5: [1,2,3,4,5,6,0],  #Dorian
            6: [2,3,4,5,6,0,1],  #Phrygian
            }

    # generates codes to filter keys and modes
    key_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for ele in range(0, 12):
        if rand_code_key[ele] == 0:
            key_id[ele] = 0
    mode_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for ele in range (0, 6):
        if rand_code_mode[ele] == 0:
            mode_id[ele] = 0

    # generates the key and mode numbers
    key_id=list(filter(lambda x: x != 0, key_id))
    mode_id=list (filter (lambda x: x != 0, mode_id))
    if key_id == 1:
        key_length=1
    else:
        key_length=len(key_id)
    key_selection=random.randint(1, key_length)
    key=key_id[key_selection-1]
    if mode_id[0] > 1:
        for ele in range (7,13):
            mode_id=list(filter (lambda x: x != ele, mode_id))
    if mode_id == 1:
        mode_length=1
    else:
        mode_length=len(mode_id)
    mode_selection=random.randint(1, mode_length)
    mode=mode_id[mode_selection-1]
    if mode > 6:
        mode=1

    # alters key to allow for mode changes
    if mode  == 1:                  # major
        key_adjust = 0
    if mode == 2:                   # minor
        for ele in range (1, 13):
            if key in range (1, 4):
                key_adjust = 9
            if key in range (4, 13):
                key_adjust = -3
    if mode == 3:                   # lydian
        if key in range (1, 12):
            key_adjust = 1
        if key == 12:
            key_adjust = -11
    if mode == 4:                   # mixolydian
        if key == 1:
            key_adjust = 11
        if key in range (2, 13):
            key_adjust = -1
    if mode == 5:                   # dorian
        if key in range (1,3):
            key_adjust = 10
        if key in range (3,13):
            key_adjust = -2
    if mode == 6:                   # phrygian
        if key in range (1, 5):
            key_adjust = 8
        if key in range (5, 13):
            key_adjust = -4

    # gives all info for user to be displayed
    key_mode_change = key + key_adjust
    key_name_rand = rand_modes[key][mode - 1]
    chord_choice = rand_chords[key_mode_change]
    mode_choice = [chord_choice[x] for x in rand_mode_order[mode]]

    # display key info in the message box
    keylabel_1 = Label (message_box, text='Write a song in the key of ' + key_name_rand, font=font_message)
    keylabel_2 = Label (message_box, text='The chords are ' + ' '.join (mode_choice),font=font_message, fg = 'green')
    keylabel_1.grid (row=0, column=0, sticky='w')
    keylabel_2.grid (row=1, column=0, sticky='w')

# function for filter button
def filter_func():
    # allow esc key to close filter window / disable ctrl + s and ctrl+f to avoid multiple windows
    app.unbind('<Escape>')
    app.unbind ('<Control-f>')
    app.unbind ('<Control-s>')
    def leave():
        # rebind all unbounded keys
        filter_window.destroy ()
        app.bind ('<Escape>', lambda event: app.quit())
        app.bind ('<Control-f>', lambda event: filter_func ())
        app.bind ('<Control-s>', lambda event: save ())
    app.bind ('<Escape>', lambda event: leave())

    # create and config filter window
    filter_window=Toplevel()
    filter_window.title ('Filter Menu')
    filter_window.geometry ("300x580")
    filter_window.configure (background='light grey')
    filter_window.bind('<Escape>', lambda event: leave())

    # create checkboxes
    c1=Checkbutton(filter_window, text='C', variable=var1,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c2=Checkbutton(filter_window, text='G', variable=var2,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c3=Checkbutton(filter_window, text='D', variable=var3,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c4=Checkbutton(filter_window, text='A', variable=var4,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c5=Checkbutton(filter_window, text='E', variable=var5,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c6=Checkbutton(filter_window, text='B', variable=var6,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c7=Checkbutton(filter_window, text='F#', variable=var7,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c8=Checkbutton(filter_window, text='Db', variable=var8,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c9=Checkbutton(filter_window, text='Ab', variable=var9,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c10=Checkbutton(filter_window, text='Eb', variable=var10,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c11=Checkbutton(filter_window, text='Bb', variable=var11,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c12=Checkbutton(filter_window, text='F', variable=var12,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c13=Checkbutton(filter_window, text='Major', variable=var13,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c14=Checkbutton(filter_window, text='Minor', variable=var14,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c15=Checkbutton(filter_window, text='Lydian', variable=var15,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c16=Checkbutton(filter_window, text='Mixolydian', variable=var16,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c17=Checkbutton(filter_window, text='Dorian', variable=var17,padx=15, font=font_message, bg='light grey', activebackground='light blue')
    c18=Checkbutton(filter_window, text='Phrygian', variable=var18,padx=15, font=font_message, bg='light grey', activebackground='light blue')

    # put checkboxes on the screen
    for ele in range (0, 12):
        checkbox_list_1=[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
        checkbox_list_1[ele].grid(row=ele, column=0, sticky='w')
    for ele in range (0, 6):
        checkbox_list_2=[c13, c14, c15, c16, c17, c18]
        checkbox_list_2[ele].grid (row=ele, column=1, stick='w')

    # function for submit button
    def submit():
        check_key=[var1.get (), var2.get (), var3.get (), var4.get (), var5.get (), var6.get (),
                     var7.get (), var8.get (), var9.get (), var10.get (), var11.get (), var12.get ()]
        check_mode=[var13.get (), var14.get (), var15.get (), var16.get (), var17.get (), var18.get ()]
        if check_key == [0,0,0,0,0,0,0,0,0,0,0,0]:
            messagebox.showerror ('error', 'Please select at least one key')
            filter_window.destroy()
            filter_func()
        if check_mode == [0,0,0,0,0,0]:
            messagebox.showerror ('error', 'Please select at least one mode')
            filter_window.destroy()
            filter_func()
        else:
            filter_window.destroy()
        leave()

    # create and display submit button
    submit_button=Button(filter_window, text='Submit', command=submit, padx=90, pady=30, font=font_button,bg='light blue')
    app.bind("<Return>", lambda event: submit())
    submit_button.grid(row=12, column=0, columnspan=2, padx=20, pady=40)

# function for the save button
def save():
    # makes sure that there's a progression to save
    try:
        chord_progression
    except:
        messagebox.showerror ('error', 'Create a chord progression first')
    else:
        # clears the frame
        for widgets in message_box.winfo_children():
            widgets.destroy ()

        # place the chords on the screen again
        chord_label_1 = Label (message_box, text='Your chord progression is in the key of ' + key_name, font=font_message)
        chord_label_2 = Label (message_box, text="Use these chords: " + ' '.join (chord_progression), font=font_message, fg='green')
        chord_label_1.grid (row=0, column=0, sticky='w')
        chord_label_2.grid (row=1, column=0, sticky='w')

        # create connection and cursor
        # conn_save = sqlite3.connect ('CHORD_DATABASE.db')
        # c_save = conn_save.cursor ()

        # create chord table
        # c_save.execute("""CREATE TABLE progressions (
        #         prog_date text,
        #         prog_name text,
        #         prog text,
        #         prog_notes text
        #         )""")

        # check if the user wants to save
        user_check = messagebox.askyesno ('Save progression?', 'Are you sure you want to save this progression?')
        if user_check == 1:
            # function for first entry
            def save_1():
                # unbind the enter key
                app.unbind ('<Return>')

                # function for the second entry key
                def save_2():
                    # create connection / cursor
                    conn_save_1 = sqlite3.connect ('CHORD_DATABASE.db')
                    c_save_1 = conn_save_1.cursor ()
                    app.unbind ('<Return>')

                    # insert into table
                    c_save_1.execute ("INSERT INTO progressions VALUES (:prog_date, :prog_name, :prog, :prog_notes)",
                                    {
                                        'prog_date': date.today ().strftime ("%m/%d/%Y"),
                                        'prog_name': save_entry_1.get(),
                                        'prog': str(' '.join(chord_progression)),
                                        'prog_notes': save_entry_2.get()
                                    })

                    # delete old labels and notify the user that the progression is saved
                    save_label_1.grid_forget()
                    save_label_2.grid_forget()
                    save_entry_1.grid_forget()
                    save_entry_2.grid_forget()
                    save_label_3 = Label(message_box,text='Your progression has been saved!',font=font_message,fg='green')
                    save_label_3.grid(row=5,column=0,sticky='w')

                    # commit and close
                    conn_save_1.commit ()
                    conn_save_1.close ()

                # ask if the user wants to add notes
                notes_check = messagebox.askyesno ('Add notes?', 'Do you want to add notes?')
                if notes_check == 1:
                    # create second direction and entry box
                    global save_entry_2
                    save_label_2 = Label (message_box, text='Enter your notes here: ',font=font_message)
                    save_entry_2 = Entry (message_box, width=30,font=font_message)
                    app.bind ('<Return>', lambda event: save_2())
                    save_button_2 = ttk.Button(message_box,command=save_2)
                    save_label_2.grid (row=5, column=0,sticky='w')
                    save_entry_2.grid (row=6, column=0,sticky='w',padx=6)
                    save_button_2.grid_forget()
                    str (save_entry_2)
                else:
                    # creates an N/A note
                    save_entry_2 = Entry (message_box)
                    save_entry_2.grid_forget()
                    save_entry_2.insert(0,'N/A')

                    # delete old labels and notify the user that the progression is saved
                    save_label_1.grid_forget()
                    save_entry_1.grid_forget()
                    save_entry_2.grid_forget()
                    save_label_3_else = Label(message_box,text='Your progression has been saved!',font=font_message,fg='green')
                    save_label_3_else.grid(row=5,column=0,sticky='w')

                    # creates connection and cursor
                    conn_save_2 = sqlite3.connect ('CHORD_DATABASE.db')
                    c_save_2 = conn_save_2.cursor ()
                    app.unbind ('<Return>')

                    # insert into table
                    c_save_2.execute ("INSERT INTO progressions VALUES (:prog_date, :prog_name, :prog, :prog_notes)",
                                    {
                                        'prog_date': date.today ().strftime ("%m/%d/%Y"),
                                        'prog_name': save_entry_1.get(),
                                        'prog': str(' '.join(chord_progression)),
                                        'prog_notes': save_entry_2.get()
                                    })

                    # commit and close
                    conn_save_2.commit ()
                    conn_save_2.close ()

            # create first direction and entry box
            save_label_1  = Label(message_box,text='What would you like to name this progression?',font=font_message)
            save_entry_1 = Entry(message_box,width=30,font=font_message)
            app.bind('<Return>', lambda event: save_1())
            save_button_1 = ttk.Button(message_box, command=save_1)
            save_label_1.grid(row=3,column=0,sticky='w')
            save_entry_1.grid(row=4,column=0,padx=6,sticky='w')
            save_button_1.grid_forget()
            str(save_entry_1)

# function for chord library button
def library():
    # clears the frame
    for widgets in message_box.winfo_children ():
        widgets.destroy ()

    # unbind enter
    app.unbind ('<Return>')

    # create new frame for library window
    library_box_1 = Frame(message_box, relief=SUNKEN, height = 50, width = 908)
    library_box_2 = Frame(message_box, bd=2, relief=SUNKEN, height = 576, width = 908)
    library_box_1.pack(fill=BOTH,expand=TRUE,side=TOP)
    library_box_2.pack(fill=BOTH,expand=TRUE,side=BOTTOM)
    library_box_1.pack_propagate(0)
    library_box_2.pack_propagate(0)

    # config frame with scrollbar
    canvas_library = Canvas (library_box_2)
    canvas_library.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar (library_box_2, orient=VERTICAL, command=canvas_library.yview)
    my_scrollbar.pack (side=RIGHT, fill=Y)

    # config the canvas
    canvas_library.configure (yscrollcommand=my_scrollbar.set)
    canvas_library.bind ('<Configure>', lambda e: canvas_library.configure (scrollregion=canvas_library.bbox ("all")))

    # allowing scrolling with touchpad
    def _on_mouse_wheel(event):
        canvas_library.yview_scroll (-1 * int ((event.delta / 100)), "units")
    canvas_library.bind_all ("<MouseWheel>", _on_mouse_wheel)

    # create another frame and add the window to the frame
    library_mainframe = Frame(canvas_library)
    canvas_library.create_window ((0, 0), window=library_mainframe, anchor="nw")

    # function for manual add button
    def add():
        # clears the frame / clears the buttons and scrollbar
        for labels in library_mainframe.winfo_children ():
            labels.destroy ()
        for buttons in library_box_1.winfo_children ():
            buttons.destroy ()

        # function to save manual progression
        def save_manual():
            # create connection and cursor
            conn_save_manual = sqlite3.connect ('CHORD_DATABASE.db')
            c_save_manual = conn_save_manual.cursor ()

            # if notes is blank, notes will be NA
            if add_notes_entry.get () == '':
                add_notes_entry.insert (0, 'N/A')

            # checks to make sure the user has created a proper progression
            test_list = [date.today ().strftime ("%m/%d/%Y"), add_name_entry.get (), add_prog_entry.get (),
                         add_notes_entry.get ()]
            if test_list == [(date.today ().strftime ("%m/%d/%Y")), '', '', 'N/A']:
                add_notes_entry.delete (0, END)
                messagebox.showerror ('error', 'Create a chord progression first')
            elif test_list[1] == "":
                add_notes_entry.delete (0, END)
                messagebox.showerror ('error', 'You must give your progression a name')
            elif test_list[2] == "":
                add_notes_entry.delete (0, END)
                messagebox.showerror ('error', 'You must add chords for the progression')
            else:
                # unbind the enter key
                app.bind ('<Return>', lambda event: library())

                # check if the user wants to save
                user_check = messagebox.askyesno ('Save progression?', 'Are you sure you want to save this progression?')
                if user_check == 1:
                    # insert into table
                    c_save_manual.execute (
                        "INSERT INTO progressions VALUES (:prog_date, :prog_name, :prog, :prog_notes)",
                        {
                            'prog_date': date.today ().strftime ("%m/%d/%Y"),
                            'prog_name': add_name_entry.get(),
                            'prog': add_prog_entry.get(),
                            'prog_notes': add_notes_entry.get()
                        })

                    # commit and close
                    conn_save_manual.commit ()
                    conn_save_manual.close ()

                    # delete old labels and notify the user that the progression is saved
                    for aspects in library_mainframe.winfo_children ():
                        aspects.destroy ()
                    save_manual_label = Label (library_mainframe, text='Your progression has been saved!',font=font_message, fg='green')
                    save_manual_label.grid (row=0, column=0, sticky='w')
                else:
                    # do nothing if the user doesn't want to save
                    return

        # create add button menu
        save_manual_button = Button(library_box_1,text='Save Progression',font=font_button_library,bg='light grey',command=save_manual,pady=6)
        app.bind ('<Return>', lambda event: save_manual ())
        back_manual_button = Button (library_box_1,text='Back',font=font_button_library,bg='light grey',command=library,pady=6)
        save_manual_button.grid(row=0, column=0, sticky='w', padx=6, pady=6)
        back_manual_button.grid(row=0, column=1, sticky='w', padx=6, pady=6)

        # create and place direction labels and entry boxes
        add_label = Label(library_mainframe, text='Manually create progression below', font=font_message,fg='green')
        add_name_label = Label(library_mainframe, text='Progression Name', font=font_message)
        add_prog_label = Label(library_mainframe, text='Custom Chords', font=font_message)
        add_notes_label =Label(library_mainframe, text='Progression Notes', font=font_message)
        add_name_entry = Entry(library_mainframe, font=font_message, width = 40)
        add_prog_entry = Entry(library_mainframe, font=font_message, width = 40)
        add_notes_entry = Entry(library_mainframe, font=font_message, width = 40)
        add_label.grid(row=0, column=0, sticky='w', columnspan=2)
        add_name_entry.grid(row=1, column=1, sticky='w',padx=12,pady=4)
        add_prog_entry.grid(row=2, column=1, sticky='w',padx=12,pady=4)
        add_notes_entry.grid(row=3, column=1, sticky='w',padx=12,pady=4)
        add_name_label.grid(row=1, column=0, sticky='w',pady=4)
        add_prog_label.grid(row=2, column=0, sticky='w',pady=4)
        add_notes_label.grid(row=3, column=0, sticky='w',pady=4)

    # function for select button
    def select():
        # clears the frame / clears the buttons
        for labels in library_mainframe.winfo_children ():
            labels.destroy ()
        for buttons in library_box_1.winfo_children ():
            buttons.destroy ()

        # create a connection and cursor
        conn_select = sqlite3.connect ('CHORD_DATABASE.db')
        c_select = conn_select.cursor ()

        # create and place labels for the tables
        date_label_new = Label (library_mainframe, text='Date', font=font_message, fg='grey')
        name_label_new = Label (library_mainframe, text='Name', font=font_message, fg='grey')
        prog_label_new = Label (library_mainframe, text='Chords', font=font_message, fg='grey')
        date_label_new.grid (row=0, column=0, sticky='w')
        name_label_new.grid (row=0, column=1, sticky='w', padx=25)
        prog_label_new.grid (row=0, column=2, sticky='w', padx=25)

        # create check boxes
        c_select.execute ("SELECT *, oid FROM progressions")
        select_progressions = c_select.fetchall ()
        var_list = []
        for index_select,items_select in enumerate (select_progressions):
            var_list.append ('v_' + str (index_select))
            var_list[index_select] = IntVar ()
            Checkbutton(library_mainframe, text=select_progressions[index_select][0], font=font_message, variable=var_list[index_select]).grid (row=index_select+1, column=0,sticky='w')
            Label(library_mainframe,text=select_progressions[index_select][1],font=font_message).grid(row=index_select+1, column=1,sticky='w', padx=25)
            Label(library_mainframe, text=select_progressions[index_select][2], font=font_message).grid(row=index_select+1, column=2, sticky='w', padx=25)

        # commit and close
        conn_select.commit ()
        conn_select.close ()

        # function to select progressions to edit
        def edit_prog():
            # clears the frame / clears the buttons
            for stuff in library_mainframe.winfo_children ():
                stuff.destroy ()
            for buttons_edit in library_box_1.winfo_children():
                buttons_edit.destroy()

            app.unbind('<return>')
            app.bind('<Return>',lambda event: save_edit())

            # create edit list
            edit_list = []
            row_index = 0
            for index_check,items_check in enumerate (select_progressions):
                edit_list.append(var_list[index_check].get())
                edit_list_check = 0

                # check that the user selected a progression
                if edit_list == [0]:
                    messagebox.showerror ('error', 'Please select at least one progression')
                    select()
                    return
                else:
                    # check if there's multiple progressions selected
                    for ele in range (0, len (edit_list)):
                        edit_list_check = edit_list_check + edit_list[ele]
                    if edit_list_check > 1:
                        messagebox.showerror ('edit error', 'Select one progression at a time to edit')
                        select()
                        return
                    else:
                        if edit_list[index_check] == 1:
                            Label(library_mainframe,text='Progression Name',font=font_message).grid(row=row_index,column=0, sticky='w',pady=4)
                            Label(library_mainframe,text='Progression Chords',font=font_message).grid(row=row_index+1,column=0, sticky='w',pady=4)
                            Label(library_mainframe,text='Progression Notes',font=font_message).grid(row=row_index+2,column=0, sticky='w',pady=4)
                            Label(library_mainframe, text='', font=font_message).grid (row=row_index + 3,column=0)
                            e_1 = Entry(library_mainframe,font=font_message,fg='grey')
                            e_2 = Entry (library_mainframe,font=font_message,fg='grey')
                            e_3 = Entry (library_mainframe,font=font_message,fg='grey')
                            e_1.grid (row=row_index, column=1, sticky='w',padx=12,pady=4)
                            e_2.grid (row=row_index + 1, column=1, sticky='w',padx=12,pady=4)
                            e_3.grid (row=row_index + 2, column=1, sticky='w',padx=12,pady=4)
                            e_1.insert(0,str(select_progressions[index_check][1]))
                            e_2.insert(0,str(select_progressions[index_check][2]))
                            e_3.insert(0,str(select_progressions[index_check][3]))
                        row_index += 4

                        # function for saving edits
                        def save_edit():
                            # check if the user wants to save
                            user_check = messagebox.askyesno ('Save edits?', 'Are you sure you want to save your changes?')
                            if user_check == 1:
                                # create connection and cursor
                                conn_edit = sqlite3.connect ('CHORD_DATABASE.db')
                                c_edit = conn_edit.cursor ()

                                # checks to make sure the user has created a progression
                                test_list = [date.today ().strftime ("%m/%d/%Y"), e_1.get (), e_2.get (),
                                             e_3.get ()]
                                if test_list == [(date.today ().strftime ("%m/%d/%Y")), '', '', '']:
                                    messagebox.showerror ('error', 'Create a chord progression first')
                                else:
                                    c_edit.execute ("DELETE from progressions WHERE oid = " + str (select_progressions[index_check][4]))
                                    # insert into table
                                    c_edit.execute (
                                        "INSERT INTO progressions VALUES (:prog_date, :prog_name, :prog, :prog_notes)",
                                        {
                                            'prog_date': date.today ().strftime ("%m/%d/%Y"),
                                            'prog_name': e_1.get (),
                                            'prog': e_2.get (),
                                            'prog_notes': e_3.get (),
                                            'oid': select_progressions[index_check][4]
                                        })

                                    # commit and close
                                    conn_edit.commit ()
                                    conn_edit.close ()

                                    # delete old labels and notify the user that the progression is saved
                                    for aspects in library_mainframe.winfo_children ():
                                        aspects.destroy ()
                                    save_edit_label = Label (library_mainframe, text='Your edits have been saved!',
                                                             font=font_message, fg='green')
                                    save_edit_label.grid (row=0, column=0, sticky='w')
                            else:
                                return

            # create edit button menu
            save_edit_button = Button (library_box_1, text='Save Edits', font=font_button_library, bg='light grey', command=save_edit, pady=6)
            back_edit_button = Button (library_box_1, text='Back', font=font_button_library, bg='light grey',command=library, pady=6)
            save_edit_button.grid (row=0, column=0, sticky='w', padx=6, pady=6)
            back_edit_button.grid (row=0, column=1, sticky='w', padx=6, pady=6)

        # function to delete progression
        def delete_prog():
            # create a connection and cursor
            conn_delete = sqlite3.connect ('CHORD_DATABASE.db')
            c_delete = conn_delete.cursor ()

            # uses vars to find which progressions to delete and deletes
            delete_list = []
            for i, items in enumerate (select_progressions):
                delete_list.append (var_list[i].get())
                
            # checks that there's a prog selected
            if delete_list == [0]:
                messagebox.showerror ('error', 'Please select at least one progression')
                select ()
                return
            
            # checks that th user wants to delete prog and then deletes
            user_check = messagebox.askyesno ('Delete Progression?','Are you sure you want to delete this/these progressions?')
            if user_check == 1:
                for i, items in enumerate(delete_list):
                    if delete_list[i] == 1:
                        c_delete.execute (
                        "DELETE from progressions WHERE oid = " + str (select_progressions[i][4]))
            else:
                return

            # commit and close / refresh the screen
            conn_delete.commit ()
            conn_delete.close ()
            select ()

        # function to view chord notes
        def view_notes():
            # clears the frame / clears the buttons
            for labels_view in library_mainframe.winfo_children ():
                labels_view.destroy ()
            for buttons_view in library_box_1.winfo_children ():
                buttons_view.destroy ()

            # creates back button
            back_button_notes = Button(library_box_1,text='Back',command = library,font=font_button_library, bg='light grey', pady=6)
            back_button_notes.grid(row=0,column=0, sticky='w', padx=6, pady=6)

            # uses vars to find which progressions to view notes for
            notes_list = []
            row_index_notes = 0
            count = 0
            for index_notes,items_notes in enumerate(select_progressions):
                notes_list.append (var_list[index_notes].get ())
                if notes_list[index_notes] != 0:
                    count += 1
                if notes_list[index_notes] == 1:
                    Label (library_mainframe, text='Name | ' + str (select_progressions[index_notes][1]),
                           font=font_message, fg='grey').grid (row=row_index_notes, column=0, sticky='w', pady=4)
                    Label (library_mainframe, text='Chords | ' + str (select_progressions[index_notes][2]),
                           font=font_message, fg='grey').grid (row=row_index_notes, column=1, sticky='w', padx=25,
                                                               pady=4)
                    Label (library_mainframe, text='Notes: ' + str (select_progressions[index_notes][3]),
                           font=font_message).grid (row=row_index_notes + 1, column=0, columnspan=2, sticky='w', pady=4)
                    Label (library_mainframe, text='', font=font_message).grid (row=row_index_notes + 2, column=0)
                row_index_notes += 3

            # check that the user selected a progression to view
            if count == 0:
                messagebox.showerror ('error', 'Please select at least one progression')
                select ()
                return

        # create view button row
        edit_button = Button(library_box_1,text='Edit',font=font_button_library,bg='light grey',command=edit_prog,pady=6)
        delete_button = Button(library_box_1,text='Delete',font=font_button_library,bg='light grey',command=delete_prog,padx=4,pady=6)
        notes_button = Button(library_box_1,text='View Notes',font=font_button_library,bg='light grey',command=view_notes,padx=4,pady=6)
        back_button = Button(library_box_1,text='Back',font=font_button_library,bg='light grey',command=library,padx=4,pady=6)
        edit_button.grid (row=0, column=0, sticky='w', padx=6, pady=6)
        delete_button.grid (row=0, column=1, sticky='w', padx=6, pady=6)
        notes_button.grid (row=0, column=2, sticky='w', padx=6, pady=6)
        back_button.grid (row=0, column=4, sticky='w', padx=6, pady=6)

    # create library button menu
    select_button = Button(library_box_1,text='Select', font=font_button_library, bg='light grey',command=select,pady=6)
    add_button = Button(library_box_1,text='Add Progression', font=font_button_library, bg='light grey',command=add,pady=6)
    select_button.grid(row=0,column=0,sticky='w',padx=6,pady=6)
    add_button.grid(row=0,column=1,sticky='w',padx=6,pady=6)

    # create and place labels for the tables
    date_label = Label(library_mainframe,text='Date',font=font_message,fg ='grey')
    name_label = Label(library_mainframe,text='Name',font=font_message,fg ='grey')
    prog_label = Label(library_mainframe,text='Chords',font=font_message,fg ='grey')
    date_label.grid(row=0,column=0,sticky='w')
    name_label.grid(row=0,column=1,sticky='w',padx=25)
    prog_label.grid(row=0,column=2,sticky='w',padx=25)

    # create a connection and cursor
    conn_library = sqlite3.connect ('CHORD_DATABASE.db')
    c_library = conn_library.cursor ()

    # find saved progressions and place them on the screen
    c_library.execute("SELECT *, oid FROM progressions")
    saved_progressions = c_library.fetchall()
    for index,items in enumerate(saved_progressions):
        Label(library_mainframe,text=saved_progressions[index][0],font=font_message).grid(row=index+1,column=0,sticky='w',pady=4)
        Label(library_mainframe, text=saved_progressions[index][1], font=font_message).grid (row=index+1, column=1,sticky='w', padx=25,pady=4)
        Label(library_mainframe, text=saved_progressions[index][2], font=font_message).grid (row=index+1, column=2,sticky='w', padx=25,pady=4)

    # commit and close
    conn_library.commit ()
    conn_library.close ()

# all hotkey bindings
app.bind ('<Control-p>', lambda event: prog())
app.bind ('<Control-r>', lambda event: rand_key())
app.bind ('<Control-f>', lambda event: filter_func())
app.bind ('<Control-s>', lambda event: save())
app.bind ('<Control-l>', lambda event: library())
app.bind ('<Escape>', lambda event: app.quit())

# create buttons / display them in screen
prog_button = Button(app, text='New Progression', padx=79, pady=25, font=font_button, relief=RAISED, command=prog, bd=4, activebackground='light blue')
rand_button = Button(app, text='Random Key', padx=106, pady=25, font=font_button, relief=RAISED, command=rand_key, bd=4, activebackground='light blue')
filter_button = Button(app, text='Filter', padx=128, pady=25, font=font_button, relief=RAISED, command=filter_func, bd=4, activebackground='light blue')
save_button = Button(app, text='Save Progression', padx=73, pady=25, font=font_button, relief=RAISED, command=save, bd=4, activebackground='light blue')
library_button = Button(app, text='Progression Library', padx=56, pady=25, font=font_button, relief=RAISED, command=library, bd=4, activebackground='light blue')
exit_button = Button(app, text='Exit App', padx=117, pady=25, font=font_button, relief=RAISED, command=app.quit, bd=4, activebackground='light blue')

button_list = [prog_button,rand_button,filter_button,save_button,library_button,exit_button]
for a in range(0,6):
    button_list[a].grid(row=a,column=0,padx=5,pady=10)

app.mainloop()