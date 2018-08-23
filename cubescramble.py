#adding window user interface with Tkinter library

from tkinter import *
import random

#window initiated
window=Tk()
#button click data


def close_window():
    window.destroy()
    exit()

#click  defined for getting output with click
def click():



    stringnumbers=dataentry.get()  # get the number in the string form

    numbers=int(stringnumbers)   #converted the string to integer for calculation



#logic to get the scrambel and print

    moveslist=[ 'Ri' , 'R' , 'Ui' , 'U' , 'Li' , 'L' , 'Bi' , 'B' , 'Di' , 'D' , 'Fi' ,'F' ]
    for x in range(0,numbers):
        puzzle=random.choices(moveslist,k=20)

        output = Text(window, width=55, height=3 ,font=( "",25 ) , bg="white")
        output.grid(row=5+x, column=0)
        output.delete(0.0, END)
        output.insert(END,puzzle)



########scroll bar added for handling more results
#scrollbar=Scrollbar(window)
#scrollbar.pack(side=RIGHT, Fill=Y)

#output=Listbox(window, yscrollcommand=scrollbar.set)
#output.pack(side=LEFT ,fill=BOTH)
#scrollbar.config(command=output.yview)



#title

window.title("Random Scramble Creator")
window.configure(background="green")


Label(window,text="3*3*3 Scrambler" ,   font=("Courier" ,30 )  ,bg="red") .grid(row=0, column=0 )


Label(window, text="Please enter the number of Scrambles You wish to have:", bg="black" ,  font=( "",19 ) ,fg="white").grid(row=1,column=0)

# data enrty box
dataentry= Entry(window, width=5, bg="white",fg="black")
dataentry.grid(row=1,column=1)
#data save button

Button(window,text="Get me scrambles" , width="14", command=click, bg="black", font=( "",19 ),   fg="white").grid(row=1, column=2)


# Label scramble

Label(window, text="Your Scramble:" ,  bg="black", font=( "",19 ),fg="white").grid(row=4, column=0)




#exit stuff
Label(window, text="Exit Scrambler" ,  bg="black", fg="white", font=( "",19 )).grid(row=998,column=0)
Button(window,text="Exit" , width="6", command=close_window , bg="white", fg="black",  font=( "",19 )).grid(row=999, column=0)






window.mainloop()
