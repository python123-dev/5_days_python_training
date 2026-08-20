#Tkinter Widgets
#run this file directly: python tkinter_widgets.py
import tkinter as tk

root = tk.Tk()
root.title('Tkinter Widgets')
root.geometry('350x400')

#Label - plain text
label = tk.Label(root, text='Tkinter Widgets Demo', font=('Arial', 14, 'bold'))
label.pack(pady=10)

#Label - with an image (uses the png we downloaded for the http notebook)
try:
    logo = tk.PhotoImage(file='python_logo.png')
    image_label = tk.Label(root, image=logo)
    image_label.pack(pady=5)
except tk.TclError:
    tk.Label(root, text='(python_logo.png not found, skipping image)').pack(pady=5)

#Button
def on_click():
    result_label.config(text='Button was clicked!')

button = tk.Button(root, text='Click Me', command=on_click)
button.pack(pady=5)

result_label = tk.Label(root, text='')
result_label.pack()

#Entry - single line text input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.insert(0, 'type something here')

#Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text='Subscribe to newsletter', variable=check_var)
checkbutton.pack(pady=5)

#Radiobutton - a group of mutually exclusive choices
radio_var = tk.StringVar(value='python')
tk.Radiobutton(root, text='Python', variable=radio_var, value='python').pack()
tk.Radiobutton(root, text='Java', variable=radio_var, value='java').pack()
tk.Radiobutton(root, text='C++', variable=radio_var, value='cpp').pack()

#Menu - attached to the root window
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
