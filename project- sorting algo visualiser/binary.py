
from tkinter import *
from tkinter import ttk
import random
import tkinter
import time
import os
from PIL import ImageTk, Image


root = Tk()
root.title("Sorting/Searching Algorithm Visualiser")
root.geometry("2000x800")
root.config(bg='#8646f4')
heading1 = Label(root, text="Sorting/Searching Algorithm Visualiser",
                 bg="#8646f1", fg="#ededed", font="tahoma 20 bold")
heading1.grid(row=0, column=2, pady=(10, 0))

arr = []


def linear_search(data, drawrectangle, delay):
    for i in range(len(data)):

            findnumber = int(number.get())
            if data[i] != findnumber:
                drawrectangle(data, [
                               'purple' if x == i else 'red' for x in range(len(data))])
                time.sleep(delay)

            elif data[i] == findnumber:
                drawrectangle(data, [
                               'green' if x == i else 'red' for x in range(len(data))])
                time.sleep(delay)
    drawrectangle(data, ['#722ce1' for x in range(len(data))])


def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(
                    data, ['purple' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(delay)
    drawrectangle(data, ['#722ce1' for x in range(len(data))])


def insertionSort(data, drawrectangle, delay):
    for i in range(len(data)):
        drawrectangle(
            data, ['yellow' if x == i else 'red' for x in range(len(data))])
        time.sleep(delay)
        key = data[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        drawrectangle(data, ['green' if x == j or x == j +
                      1 else 'red' for x in range(len(data))])
        time.sleep(delay)
    drawrectangle(data, ['#722ce1' for x in range(len(data))])


def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)):
        drawrectangle(
            data, ['yellow' if x == i else 'red' for x in range(len(data))])
        time.sleep(delay)

        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        drawrectangle(data, ['purple' if x ==
                      min_idx else 'red' for x in range(len(data))])
        time.sleep(delay)
        data[i], data[min_idx] = data[min_idx], data[i]

    drawrectangle(data, ['#722ce1' for x in range(len(data))])


def binary_search(data, x, drawrectangle, delay):
    

    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        
        mid = (high + low) // 2
        drawrectangle(data,['yellow' if x==mid else 'red' for x in range(len(data))])
        time.sleep(delay)

        if arr[mid] < x:
            low = mid + 1
            drawrectangle(data,['yellow' if x==low else 'orange' if x==high else 'red' for x in range(len(data))])
            time.sleep(delay)
 
        elif arr[mid] > x:
            high = mid - 1
            drawrectangle(data,['yellow' if x==low else 'orange' if x==high else 'red' for x in range(len(data))])
            time.sleep(delay)
 
        else:
            drawrectangle(data,['green' if x==mid else 'orange' if x==high else 'red' for x in range(len(data))])
            time.sleep(delay)
            return mid
            


def binary():
    global arr
    global canvas1
    canvas1 = Canvas(root, width=503, height=382, bg="white")
    canvas1.grid(row=1, column=3,pady=10)
    binary_search(arr,number.get() ,drawrectangle, speed.get())




def sorting_insertion():
    global arr
    global canvas1
    canvas1 = Canvas(root, width=503, height=382, bg="white")
    canvas1.grid(row=1, column=3,pady=10)
    insertionSort(arr, drawrectangle, speed.get())

def sorting_bubble():
    global arr
    global canvas1
    canvas1 = Canvas(root, width=503, height=382, bg="white")
    canvas1.grid(row=1, column=3,pady=10)
    bubble_sort(arr, drawrectangle, speed.get())


def sorting_selection():
    global arr
    global canvas1
    canvas1 = Canvas(root, width=503, height=382, bg="white")
    canvas1.grid(row=1, column=3,pady=10)
    selection_sort(arr, drawrectangle, speed.get())


def searching_linear():
    global arr
    global canvas1
    canvas1 = Canvas(root, width=503, height=382, bg="white")
    canvas1.grid(row=1, column=3,pady=10)
    linear_search(arr, drawrectangle, speed.get())


def Generate_array():
    global arr
    lowest = int(low.get())
    highest = int(high.get())
    size = int(arrsize.get())

    arr = []
    for i in range(size):
        arr.append(random.randrange(lowest, highest+1))

    drawrectangle(arr, ['red' for x in range(len(arr))])


def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 600
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 20
    spacing = 10
    normalized_array = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height*340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(arr[i]))

    root.update_idletasks()

frame1 = Frame(root, bg="#ededed", padx=10, pady=10, height=800, width=400)
frame1.grid(row=1, column=1, padx=10,pady=12)

canvas = Canvas(root, width=620, height=600, bg="#ededed")
canvas.grid(row=1, column=2, padx=20,pady=12)


low = Scale(frame1, bg='#8646f1', fg='#ededed', orient=HORIZONTAL,
            from_=1, to=20, label="Lower Value", font="lucida 10 bold")
low.grid(row=2, column=1, pady=(0,5))

high = Scale(frame1, bg='#8646f1', fg='#ededed', orient=HORIZONTAL,
             from_=20, to=300, label="Upper value", font="lucida 10 bold")
high.grid(row=3, column=1, pady=8)

arrsize = Scale(frame1, bg='#8646f1', fg='#ededed', orient=HORIZONTAL,
                from_=4, to=80, label="Size", font="lucida 10 bold")
arrsize.grid(row=4, column=1, pady=8)

speed = Scale(frame1, bg='#8646f1', fg='#ededed', from_=0, to=4.0, length=100, digits=2,
              resolution=0.2, orient=HORIZONTAL, label="Speed ", font="lucida 10 bold")
speed.grid(row=5, column=1, pady=8)

number = Scale(frame1, fg='#ededed', bg='#8646f1', orient=HORIZONTAL,
               from_=1, to=300, label="Number", font="lucida 10 bold")
number.grid(row=6, column=1, pady=8)

myarray = Button(frame1, text="Show Array", bg="purple", fg="#ededed",
                 command=Generate_array, relief=GROOVE, pady=2, width=12, font="lucida 10 bold")
myarray.grid(row=7, column=1, pady=7)

search = Button(frame1, text="Linear Search",  bg="purple", fg="#ededed",
                width=12, command=searching_linear, relief=GROOVE, pady=2, font="lucida 10 bold")
search.grid(row=8, column=1,pady=7)
binary = Button(frame1, text="Binary Search",  bg="purple", fg="#ededed",
                   width=12, command=binary,  relief=GROOVE,pady=2, font="lucida 10 bold")
binary.grid(row=9, column=1, pady=(5,0))


def graphclicklinear():
    path='graphlinear.png'
    img=ImageTk.PhotoImage(Image.open(path))
    img1=Label(canvas1,image=img)
    img1.photo=img
    img1.grid(row=1,column=3) 
   

def graphclickbubble():
    path='graphbubble.png'

    img=ImageTk.PhotoImage(Image.open(path))
    img1=Label(canvas1,image=img)
    img1.photo=img
    img1.grid(row=1,column=3) 
    canvas1.delete("all")
    
def graphclickselection():
    path='graphselection.png'

    img=ImageTk.PhotoImage(Image.open(path))
    img1=Label(canvas1,image=img)
    img1.photo=img
    img1.grid(row=1,column=3) 
    canvas1.delete("all")

def graphclickins():
    path='graphinsertion.png'

    img=ImageTk.PhotoImage(Image.open(path))
    img1=Label(canvas1,image=img)
    img1.photo=img
    img1.grid(row=1,column=3) 

def graphclickbs():
    path='bsgraph.jpeg'

    img=ImageTk.PhotoImage(Image.open(path))
    img1=Label(canvas1,image=img)
    img1.photo=img
    img1.grid(row=1,column=3) 

button1=Button(frame1,text="Graph",bg="purple",  relief=GROOVE,fg="#ededed",width=5,font="lucida 10 bold",command=graphclicklinear)
button1.grid(row=8,column=2,padx=5,pady=7)

bubble = Button(frame1, text="Bubble Sort",  bg="purple", fg="#ededed",
                width=12, command=sorting_bubble, relief=GROOVE, pady=2, font="lucida 10 bold")
bubble.grid(row=10, column=1, pady=7)

button6=Button(frame1,text="Graph",bg="purple", relief=GROOVE, fg="#ededed",width=5,font="lucida 10 bold",command=graphclickbubble)
button6.grid(row=10,column=2,padx=5,pady=7)



button5=Button(frame1,text="Graph",bg="purple", relief=GROOVE, fg="#ededed",width=5,font="lucida 10 bold",command=graphclickbs)
button5.grid(row=9,column=2,padx=5,pady=7)


insertion = Button(frame1, text="Insertion Sort",  bg="purple", fg="#ededed",
                   width=12, command=sorting_insertion, relief=GROOVE,pady=2, font="lucida 10 bold")
insertion.grid(row=11, column=1,pady=7)

button3=Button(frame1,text="Graph",bg="purple", relief=GROOVE, fg="#ededed",width=5,font="lucida 10 bold",command=graphclickins)
button3.grid(row=11,column=2,padx=5,pady=7)

selection = Button(frame1, text="Selection Sort",  bg="purple", fg="#ededed",
                   width=12, command=sorting_selection,  relief=GROOVE,pady=2, font="lucida 10 bold")
selection.grid(row=12, column=1, pady=(5,0))


button4=Button(frame1,text="Graph",bg="purple", relief=GROOVE, fg="#ededed",width=5,font="lucida 10 bold",command=graphclickselection)
button4.grid(row=12,column=2,padx=5,pady=7)

root.mainloop()
