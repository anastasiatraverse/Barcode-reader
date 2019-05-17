from tkinter import *
from method_1 import decode_barcode
from method_2 import barcode_detect
import create_barcode
from PIL import Image, ImageTk


def show_create(num):
    create_barcode.create('upc', num)
    path = 'created_barcode.png'
    win = Toplevel(root)
    win.title('Create barcode')
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

def show_decode():
    path = 'result.png'
    win = Toplevel(root)
    win.title('Decode barcode')
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)



def get_create():
    def get_num():
        if number.get() and len(number.get())==11:
            num = number.get()
            show_create(num)
        else:
            Label(win, text="Please fill all fields correctly! UPC must have 11 digits! ").grid(row=4, column=1)
    win = Toplevel(root)
    win.title('Create barcode')
    number = StringVar()
    Label(win, text="Enter number").grid(row=1, column=1)
    Entry(win, textvariable=number).grid(row=2, column=1)
    Button(win, text="Enter!", command = get_num).grid(row=3, column=1)

def decode_m1():
    def get_value():
        if v_file.get():
            file = v_file.get()
            decode_barcode.decode(file)
            show_decode()
        else:
            Label(win, text="Please fill all fields correctly!").grid(row=4, column=1)
    win= Toplevel(root)
    win.title("Decode Barcode, method 1")
    v_file = StringVar()
    Label(win, text="Please enter file name!").grid(row=1, column=1)
    Entry(win, textvariable=v_file).grid(row=2, column=1)
    Button(win, text='Enter!', command=get_value).grid(row=3, column=1)

def decode_m2():
    def get_value():
        if v_file.get():
            file = v_file.get()
            barcode_detect.decode(file)
            show_decode()
        else:
            Label(win, text="Please fill all fields correctly!").grid(row=4, column=1)
    win= Toplevel(root)
    win.title("Decode Barcode, method 2")
    v_file = StringVar()
    Label(win, text="Please enter file name!").grid(row=1, column=1)
    Entry(win, textvariable=v_file).grid(row=2, column=1)
    Button(win, text='Enter!', command=get_value).grid(row=3, column=1)



root = Tk()

root.title('Barcode decoding')
root.geometry('600x300')

Label(root, text='Hello!\n'
                 'Please choose one of possible option').grid(row = 1, column=1, columnspan=3)



Button(root, text="Create barcode", command = get_create).grid(row=2, column=1)
Button(root, text="Decode barcode (Canny edge detection)", command =decode_m1).grid(row=2, column=2)
Button(root, text="Decode barcode (MIN/MAX)", command = decode_m2).grid(row=2, column=3)
root.mainloop()


