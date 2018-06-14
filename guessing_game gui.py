import tkinter as tki # Tkinter -> tkinter in Python3
import tkinter.filedialog
import csv
import random

class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=800, height=300)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)
        
        tip_field_frm = tki.Frame(self.root)
        tip_field_frm.pack()

        guess_button_frm = tki.Frame(self.root)
        guess_button_frm.pack()

        tips_button_frm = tki.Frame(self.root)
        tips_button_frm.pack()

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("Calibri", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self.tip_field = tki.Entry(tip_field_frm)
        self.tip_field.pack()

        self.guess_btn = tki.Button(guess_button_frm)
        self.guess_btn['text'] = 'Guess it!'
        self.guess_btn['command'] = self.guess
        self.guess_btn.pack()

        self.tips_btn = tki.Button(tips_button_frm)
        self.tips_btn['text'] = 'Tips so far'
        self.tips_btn['command'] = self.tips
        self.tips_btn.pack()

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        self.game_started=False

        self.current_guess={}

        self.tips=[]

        self.start_game()
        
        self.tips_so_far=''

    def guess(self):
        tip = self.tip_field.get()
        
        if tip not in self.tips_so_far:

            if 'legs' in tip.lower():
                legs=0
                msg=''
                for char in tip:
                    if char.isdigit():
                        legs=char
                if int(legs) == self.current_guess['legs']:
                    msg=("Yes! The animal has "+legs+" legs!")
                    self.tips.append('Has '+str(legs)+' legs')
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    if int(legs) > self.current_guess['legs']:
                        msg=("No, this animal doesnt have "
                             +legs+" legs! Try lower.")
                    else:
                        msg=("This animal will need more than "
                             +legs+" legs! Try again.")
                    self.tips_so_far = self.tips_so_far + '__'+tip
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'flies' in tip.lower():
                msg=''
                if self.current_guess['flies']:
                    msg=("Yes! It does fly! Can you guess what it is?")
                    self.tips.append('It flies')
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    msg=("Nope! That thing definitely does not fly!")
                    self.tips.append('It does not fly')
                    self.tips_so_far = self.tips_so_far + '__'+tip
                    
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'swims' in tip.lower():
                msg=''
                if self.current_guess['swims']:
                    msg=("Yes! It does swim! Can you guess what it is?")
                    self.tips.append('It swims')
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    msg=("Nope! That thing definitely does not swim!")
                    self.tips.append('It does not swim')
                    self.tips_so_far = self.tips_so_far + '__'+tip
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'from' in tip.lower():
                msg=''
                continent=tip.lower()[tip.lower().find(' ')+1:]
                if self.current_guess['habitat']==continent:
                    msg=("Yes! It is from "+continent+"! Can you guess what it is?")
                    self.tips.append("From "+continent)
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    msg=("Nope, i'm afraid it is not from "+continent)
                    self.tips.append("Not from "+continent)
                    self.tips_so_far = self.tips_so_far + '__'+tip
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'its a' in tip.lower():
                msg=''
                tp=tip.lower()[tip.lower().find('a')+2:]
                if self.current_guess['type']==tp:
                    msg=("Yes! It is a "+tp+"!")
                    self.tips.append("It's a "+tp)
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    msg=("Nope, i'm afraid it is not a "+tp+"!")
                    self.tips.append("Not a "+tp)
                    self.tips_so_far = self.tips_so_far + '__'+tip
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'eggs' in tip.lower():
                msg=''
                if self.current_guess['eggs']:
                    msg=("Yes! It lays eggs!")
                    self.tips.append("It lays eggs")
                    self.tips_so_far = self.tips_so_far + '__'+tip
                else:
                    msg=("I'm sorry but this animal does not lays eggs.")
                    self.tips.append("It doesn't lays eggs")
                    self.tips_so_far = self.tips_so_far + '__'+tip
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
    
            if 'guess' in tip.lower():
                msg=''
                guess=tip.lower().split(' ')[-1]
                if self.current_guess['name']==guess:
                    msg=("Yes! It is a "+guess+"! Congratulations you won the game!")
                else:
                    msg=("Nope, i'm afraid it is not a "+guess+"!")
                msg=msg+'\n'
                self.txt.insert(1.0, msg)
            
        else:
            self.tips_so_far_func()

    def tips(self):
        if len(self.tips) > 0:
            self.txt.insert(1.0, '\n')
            for item in self.tips:
                self.txt.insert(1.0, item+'\n')
            self.txt.insert(1.0, 'Tips you alread discovered:\n')
        else:
            self.txt.insert(1.0, "You haven't made any guess so far.\n\n")
            
    def tips_so_far_func(self):
        self.txt.insert(1.0, "You already tried that!\n\n")
        
    def start_game(self):
        if self.game_started == False:
            animals={1: ['lion', 'mammal', 'africa', 4, False, False, False],
                     2: ['penguin','bird', 'north pole', 2, False, True, True]}

            animal=random.randint(1, 2)
            self.current_guess['name']=animals[animal][0]
            self.current_guess['type']=animals[animal][1]
            self.current_guess['habitat']=animals[animal][2]
            self.current_guess['legs']=animals[animal][3]
            self.current_guess['flies']=animals[animal][4]
            self.current_guess['swims']=animals[animal][5]
            self.current_guess['eggs']=animals[animal][6]

            msg=("A secret animal was chosen. Now try and guess it!\n"
            "Ask how many legs does it have with 'n legs'.\n"
            "Type 'it flies' if you think it does! Or maybe 'it swims'? Does it 'lays eggs'?\n"
            "Can you guess from which continent is it from? (type 'from africa', for example)\n"
            "When you find out what it is, just type 'guess [name of the animal]\n"
            )
            self.txt.insert(1.0, msg)
            game_started = True

app = App()
app.root.mainloop()