import pickle    
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import os,time,sys
from tkinter import font
from tkinter import messagebox
# Fonts ##
LightFontface = Font=('HelveticaNeueLT Com 25 UltLt', 25, "normal")
smallfont = Font=('HelveticaNeueLT Com 25 UltLt', 15, "normal")
displayfont = font=('HelveticaNeueLT Com 25 UltLt', 40, "normal")
equalsfont = font=("HelveticaNeueLT Com 25 UltLt", 30, "normal")
# colors ##
Digitbackground_color = "#AEAEAE"
normal_button_height = 1
normal_button_width = 2
# pad sizes ##
button_padx = 1
button_pady = 1
keypressed = 0
# commands ##
def ButtonPress(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)
	display = text_Input.get()
	if display[0] in '+–÷×%.':
		operator = ""
		text_Input.set("0")	
	if display[0] in "0":
		operator = ""
		text_Input.set("0")	 	
def ButtonClear():
	global operator
	operator = ""
	text_Input.set("0")
def plusminus():
	global operator
	operator = str(-float(text_Input.get()))
	text_Input.set(operator)
def ButtonEquals():
	try:
		global operator
		sumup = str(eval(operator.replace("×", "*").replace("÷","/").replace("²", "**2").replace("–", "-").replace("⁻¹","**(-1)")))
		operator = sumup
		text_Input.set(sumup)
	except Exception as ex:
		text_Input.set("Error")
		operator = ""	
def calculatorstart():
	text_Input.set("0")
	operator = ""
def Backspace():	
	global operator
	backspace = text_Input.get()
	backspace = backspace[:-1]
	operator = backspace
	text_Input.set(operator)
	result = text_Input.get()
	if len(result) < 1:
		operator = ""
		text_Input.set("0")	
# configuration

cal = Tk()
cal.configure(bd=0, bg="#3b3b3b")
cal.attributes("-alpha", 0.93)
#cal.wm_iconbitmap(app_icon)
cal.title("Calculator by Luka Gogilashvili")


cal.resizable(False, False)
operator = ""
text_Input = ""
text_Input = StringVar()
# GUI ##
txtDisplay = Entry(cal, font=displayfont, state="disabled", disabledbackground= "#3b3b3b", disabledforeground="#FFFFFF", insertbackground="#3b3b3b", width=11, relief=FLAT, textvariable = text_Input,
				   bg ="#3b3b3b", fg="#FFFFFF", command = calculatorstart(), justify = "right").grid(row=0, column=0, columnspan=5, sticky=NSEW)
txtDisplay
## Buttons ##
minus1xarixsi = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, font=LightFontface, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", text="⁻¹",
				command = lambda:ButtonPress("⁻¹")).grid(row=3, column=1, sticky=NSEW, padx=1, pady=1)
#akvadrateba = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, font=LightFontface, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", text="×²",
#				command = lambda:ButtonPress("²")).grid(row=3, column=3, sticky=NSEW, padx=1, pady=1)
pliusminus = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, font=LightFontface, relief=FLAT, activebackground="#787878", activeforeground="#385646", fg="#000000", bg="#bebebe", text="+/-",
	command = lambda:plusminus()).grid(row=1, column=2, sticky=NSEW, padx=1, pady=1)
percentage = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, font=LightFontface, relief=FLAT, activebackground="#787878", activeforeground="#385646", fg="#000000", bg="#bebebe", text="%",
			command = lambda:ButtonPress("%")).grid(row=1, column=3, sticky=NSEW, padx=1, pady=1)

button7 = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, font=LightFontface, relief=FLAT,  activebackground=Digitbackground_color,fg="#000000", bg="#e0e0e0", text="7",
				 command = lambda:ButtonPress(7)).grid(row=2, column=0, sticky=NSEW, padx=1, pady=1)

button8 = Button(cal, height=normal_button_height, padx=16, width=normal_button_width, font=LightFontface, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", text="8",
				 command = lambda:ButtonPress(8)).grid(row=2, column=1, sticky=NSEW, padx=1, pady=1)

button9 = Button(cal, height=normal_button_height, padx=16, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="9",
				 command = lambda:ButtonPress(9)).grid(row=2, column=2, sticky=NSEW, padx=1, pady=1)

buttonAdd = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground="#CC7B33", fg="#ffffff", bg="#f3933d", font=LightFontface, text="+",
				   command = lambda:ButtonPress("+")).grid(row=4, column=3, sticky=NSEW, padx=1, pady=1)

button4 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="4",
				 command = lambda:ButtonPress(4)).grid(row=3, column=0, sticky=NSEW, padx=1, pady=1)

button5 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="5",
				 command = lambda:ButtonPress(5)).grid(row=3, column=1, sticky=NSEW, padx=1, pady=1)

button6 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="6",
				 command = lambda:ButtonPress(6)).grid(row=3, column=2, sticky=NSEW, padx=1, pady=1)

button1 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color,  fg="#000000", bg="#e0e0e0", font=LightFontface, text="1",
				 command = lambda:ButtonPress(1)).grid(row=4, column=0, sticky=NSEW, padx=1, pady=1)


buttonsub = Button(cal, height=normal_button_height, padx=16, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#FFFFFF", bg="#f3933d", font=LightFontface, text="–",
				   command = lambda:ButtonPress("–")).grid(row=5, column=3, sticky=NSEW, padx=1, pady=1)

buttonpoint = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text=".",
					 command = lambda:ButtonPress(".")).grid(row=5, column=1, sticky=NSEW, padx=1, pady=1)

#buttonbracket = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, bg="#bebebe", fg="#000000", activebackground="#787878", activeforeground="#385646", font=smallfont, text="(",
#				command = lambda:ButtonPress("()")).grid(row=2, column=0, sticky=NSEW, padx=1, pady=1)

#buttonbracket1 = Button(cal, height=normal_button_height, width=normal_button_width, padx=8, relief=FLAT, bg="#bebebe", fg="#000000", activebackground="#787878", activeforeground="#385646", font=smallfont, text=")",
#					command = lambda:ButtonPress(")")).grid(row=2, column=1, sticky=NSEW, padx=1, pady=1)	

button2 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="2",
				 command = lambda:ButtonPress(2)).grid(row=4, column=1, sticky=NSEW, padx=1, pady=1)

button3 = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="3",
				 command = lambda:ButtonPress(3)).grid(row=4, column=2, sticky=NSEW, padx=1, pady=1)

buttonmultiply = Button(cal, height=normal_button_height, width=normal_button_width, relief=FLAT, activebackground="#CC7B33", fg="#FFFFFF", bg="#f3933d", font=LightFontface, text="×",
				 	   command = lambda:ButtonPress("×")).grid(row=2, column=3, stick=NSEW, padx=1, pady=1)

button0 = Button(cal, height=normal_button_height, padx=19, width=normal_button_width, relief=FLAT, activebackground=Digitbackground_color, fg="#000000", bg="#e0e0e0", font=LightFontface, text="0",
				 command = lambda:ButtonPress(0)).grid(row=5, column=0, sticky=NSEW, padx=1, pady=1)

buttonclr = Button(cal, height=normal_button_height, width=normal_button_width, activebackground="#787878", activeforeground="#385646", relief=FLAT, fg="#000000", bg="#bebebe", font=smallfont, text="C",
				   command = ButtonClear).grid(row=1, column=0, sticky=NSEW, padx=1, pady=1)

buttonbackspace = Button(cal, height=normal_button_height, width=normal_button_width, activebackground="#787878", activeforeground="#385646", relief=FLAT, fg="#000000", bg="#bebebe", font=equalsfont, text="␡", anchor="center",
				command = Backspace).grid(row=1, column=1, sticky=NSEW, padx=1, pady=1)

buttonEquals = Button(cal, height=normal_button_height, width=normal_button_width, fg="#FFFFFF", bg="#f3933d", font=LightFontface, relief=FLAT, text="=",
					 command = ButtonEquals).grid(row=5, column=2, sticky=NSEW, padx=1, pady=1)

buttondivide = Button(cal, height=normal_button_height, width=normal_button_width, activebackground="#CC7B33", relief=FLAT, fg="#FFFFFF", bg="#f3933d", font=LightFontface, text="÷",
					  command = lambda:ButtonPress("÷")).grid(row=3, column=3, sticky=NSEW, padx=1, pady=1)
cal.mainloop()