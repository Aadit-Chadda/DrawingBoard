import time
from tkinter import *
import pygetwindow
import pyautogui
from PIL import Image

current_x, current_y = 0, 0
color = 'black'


def locate_xy(event):
    global current_x, current_y
    
    current_x, current_y = event.x, event.y


def addLine(event):
    global current_x, current_y
    
    canvas.create_line((current_x, current_y, event.x, event.y), fill=color)
    current_x, current_y = event.x, event.y


def eraser(event):
    global current_x, current_y
    
    canvas.create_rectangle((current_x + 10, current_y + 10, event.x, event.y), fill='white')
    current_x, current_y = event.x, event.y


def show_color(new_color):
    global color
    
    color = new_color


def new_canvas():
    canvas.delete('all')
    display_pallete()


def erase():
    global color
    
    color = 'white'
    

def save_it():
    win = Toplevel()
    win.title('Save as Image')
    show = Label(win, text='Enter name of file: ')
    show.pack()
        
    def button_command():
        text = e.get()
        content = text
        win.destroy()
        titles = pygetwindow.getAllTitles()
        print(titles)
            
        path = '/Users/aadit/desktop/' + content + '.png'
        x1, y1, width, height = pygetwindow.getWindowGeometry('Python Whiteboard')
        x2 = x1 + width
        y2 = y1 + height
        pyautogui.screenshot(path)
        im = Image.open(path)
        im = im.crop(x1, y1, x2, y2)
        im.save(path)
        
    e = Entry(win)
    e.pack()
    button1 = Button(win, text='Enter', command=button_command)
    button1.pack()
    win.mainloop()


window = Tk()
window.title('Whiteboard')
window.state('zoomed')
window.geometry('1920x1000')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

menubar = Menu(window)
window.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)

canvas = Canvas(window, background='white')
canvas.grid(row=0, column=0, sticky='nsew')

clear = Button(window, text='Clear', fg='red', activebackground='red', command=new_canvas)
clear.grid(row=1, column=0, sticky='se')

save = Button(window, text='Save', fg='green', activebackground='green', command=save_it)
save.grid(row=1, column=1, sticky='sw')

eraser = Button(window, text='E', pady=20, command=eraser)
eraser.grid(row=1, column=0, sticky='sw')

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)


def display_pallete():
    id = canvas.create_rectangle((10, 10, 30, 30), fill='black')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
    
    id = canvas.create_rectangle((10, 40, 30, 60), fill='turquoise')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('turquoise'))
    
    id = canvas.create_rectangle((10, 70, 30, 90), fill='brown4')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
    
    id = canvas.create_rectangle((10, 100, 30, 120), fill='red')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    
    id = canvas.create_rectangle((10, 130, 30, 150), fill='orange')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    
    id = canvas.create_rectangle((10, 160, 30, 180), fill='yellow')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    
    id = canvas.create_rectangle((10, 190, 30, 210), fill='green')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
    
    id = canvas.create_rectangle((10, 220, 30, 240), fill='blue')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
    
    id = canvas.create_rectangle((10, 250, 30, 270), fill='purple')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
    
    id = canvas.create_rectangle((10, 280, 30, 300), fill='grey')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('grey'))
    
    id = canvas.create_rectangle((10, 310, 30, 330), fill='white')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_color('white'))


display_pallete()

window.mainloop()
