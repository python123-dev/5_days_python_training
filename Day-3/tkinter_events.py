#Event-Driven Programming - command callbacks, bind(), and reacting to live user input
#run this file directly: python tkinter_events.py
import tkinter as tk

root = tk.Tk()
root.title('Tkinter Events')
root.geometry('350x350')

status = tk.Label(root, text='Interact with the widgets below', fg='blue')
status.pack(pady=10)

#command= callback - fires when the button is clicked
def on_button_click():
    status.config(text='Button clicked!')

tk.Button(root, text='Click Me', command=on_button_click).pack(pady=5)

#StringVar + trace - react live as the Entry text changes, no button needed
name_var = tk.StringVar()

def on_name_change(*args):
    status.config(text=f'You typed: {name_var.get()}')

name_var.trace_add('write', on_name_change)
tk.Entry(root, textvariable=name_var, width=30).pack(pady=5)

#bind() - low level event binding for keyboard/mouse events
def on_key_press(event):
    status.config(text=f'Key pressed: {event.keysym}')

def on_mouse_enter(event):
    status.config(text='Mouse entered the button!')

def on_mouse_leave(event):
    status.config(text='Mouse left the button')

root.bind('<Key>', on_key_press)

hover_button = tk.Button(root, text='Hover over me')
hover_button.pack(pady=5)
hover_button.bind('<Enter>', on_mouse_enter)
hover_button.bind('<Leave>', on_mouse_leave)

#capturing a selection from a menu, another way of triggering events
choice_var = tk.StringVar(value='Choose a fruit')

def on_menu_select(value):
    choice_var.set(value)
    status.config(text=f'Selected: {value}')

menu_button = tk.Menubutton(root, textvariable=choice_var, relief='raised')
fruit_menu = tk.Menu(menu_button, tearoff=0)
for fruit in ('Apple', 'Banana', 'Cherry'):
    fruit_menu.add_command(label=fruit, command=lambda f=fruit: on_menu_select(f))
menu_button.config(menu=fruit_menu)
menu_button.pack(pady=5)

#double-click event on the status label itself
status.bind('<Double-Button-1>', lambda event: status.config(text='Double-clicked the status label!'))

root.mainloop()
