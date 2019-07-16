#Lawrence M Machi III
#Final Project 
from tkinter import*

class CalcGUI:
    def __init__(self):
        #Main window
        self.main = Tk()
        #Title of window
        self.main.title('Basic Operations Calculator')
        #Create 5 frames
        self.begin = Frame()
        self.top = Frame()
        self.mid = Frame()
        self.bottom = Frame()
        self.done = Frame()

        #Explain if user wants to do percentage put in first number only
        self.instruc = Label(self.begin,text = "If you want to do percentage put in the first number only.")
        self.instruc.pack(side = 'left')
        
        #Input first num
        self.first_num = Label(self.top,text = 'Enter first number:')
        self.calc_entry = Entry(self.top,width = 10)

        #Pack the frame
        self.first_num.pack(side = 'left')
        self.calc_entry.pack(side = 'left')

        #Second num input
        self.second_num = Label(self.mid,text = 'Enter a second number: ')
        self.calc_entry2 = Entry(self.mid,width = 10)

        #Pack second frame
        self.second_num.pack(side = 'left')
        self.calc_entry2.pack(side = 'left')
        
        #Object to give output label
        self.result = Label(self.done, text = 'This operation result is = ')
        self.value = StringVar()

        #StringVar obj displays result
        self.value_label = Label(self.done,textvariable = self.value)

        #Pack very bottom
        self.value_label.pack(side = 'bottom')
        self.result.pack(side = 'bottom')

        #Functions for calculator
        self.calcAdd = Button(self.bottom,text = '+',command = self.add) #Add widget 
        self.calcSub = Button(self.bottom,text = '-',command = self.subtract) #Subtract widget
        self.calcMult = Button(self.bottom,text = '*',command = self.multiply) #Multiply Widget
        self.calcDiv = Button(self.bottom,text = '/',command = self.divide) #Divide Widget
        self.calcPer = Button(self.bottom,text = '%',command = self.percent) #Percentage Widget
        self.quit = Button(self.bottom,text = 'Quit',command = self.main.destroy) #Quits program
        
        #Pack buttons
        self.calcAdd.pack(side = 'left')
        self.calcSub.pack(side = 'left')
        self.calcMult.pack(side = 'left')
        self.calcDiv.pack(side = 'left')
        self.calcPer.pack(side = 'left')
        self.quit.pack(side = 'right')
    
        #Pack Frames
        self.begin.pack()
        self.top.pack()
        self.mid.pack()
        self.bottom.pack()
        self.done.pack()

        #tkinter main loop
        mainloop()

    def add(self):
        try:
            self.num1 = float(self.calc_entry.get())
            self.num2 = float(self.calc_entry2.get())
            #Add numbers
            self.result = self.num1 + self.num2
        #Checking if the inputted numbers are not a key or letter
        except ValueError:
            self.result = "Invalid, use a number."

        #Store in stringVar object
        self.value.set(self.result)

    def subtract(self):
        try:
            self.num1 = float(self.calc_entry.get())
            self.num2 = float(self.calc_entry2.get())
            #Subtract numbers
            self.result = self.num1 - self.num2
        #Checking if the inputted numbers are not a key or letter
        except ValueError:
            self.result = "Invalid, use a number."

        #Store in stringVar object
        self.value.set(self.result)

    def multiply(self):
        try:
            self.num1 = float(self.calc_entry.get())
            self.num2 = float(self.calc_entry2.get())
            #Multiply numbers
            self.result = self.num1 * self.num2
        #Checking if the inputted numbers are not a key or letter
        except ValueError:
            self.result = "Invalid, use a number."

        #Store in stringVar object
        self.value.set(self.result)

    def divide(self):
        try:
            self.num1 = float(self.calc_entry.get())
            self.num2 = float(self.calc_entry2.get())
            #Divide numbers
            self.result = self.num1 / self.num2
        #Checking if the inputted numbers are not a key or letter
        except ValueError:
            self.result = "Invalid, use a number."

        #Store in stringVar object
        self.value.set(self.result)

    def percent(self):
        try:
            self.num1 = float(self.calc_entry.get())
            #Take the percentage
            self.result = self.num1 / 100
        #Checking if the inputted number are not a key or letter
        except ValueError:
            self.result = "Invalid, use a number."
            
        #Store in object
        self.value.set(self.result)
        
add_Num = CalcGUI()

