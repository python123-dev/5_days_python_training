#GUI Layout Management - pack, grid, place and organizing widgets in Frames/Toplevel windows
#run this file directly: python tkinter_layout.py
import tkinter as tk

root = tk.Tk()
root.title('Tkinter Layout Managers')
root.geometry('400x450')

#pack() - stacks widgets top-to-bottom (or side-to-side) in the order added
pack_frame = tk.Frame(root, bd=2, relief='groove')
pack_frame.pack(fill='x', padx=10, pady=10)

tk.Label(pack_frame, text='pack() layout', font=('Arial', 10, 'bold')).pack()
tk.Button(pack_frame, text='Left', width=8).pack(side='left', padx=5, pady=5)
tk.Button(pack_frame, text='Middle', width=8).pack(side='left', padx=5, pady=5)
tk.Button(pack_frame, text='Right', width=8).pack(side='left', padx=5, pady=5)

#grid() - places widgets in a row/column table inside their parent
grid_frame = tk.Frame(root, bd=2, relief='groove')
grid_frame.pack(fill='x', padx=10, pady=10)

tk.Label(grid_frame, text='grid() layout', font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2)
tk.Label(grid_frame, text='Name:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
tk.Entry(grid_frame).grid(row=1, column=1, padx=5, pady=5)
tk.Label(grid_frame, text='Email:').grid(row=2, column=0, sticky='e', padx=5, pady=5)
tk.Entry(grid_frame).grid(row=2, column=1, padx=5, pady=5)

#place() - positions widgets using absolute x, y coordinates
place_frame = tk.Frame(root, bd=2, relief='groove', height=100)
place_frame.pack(fill='x', padx=10, pady=10)

tk.Label(place_frame, text='place() layout', font=('Arial', 10, 'bold')).place(x=10, y=5)
tk.Button(place_frame, text='Top-Left').place(x=10, y=35)
tk.Button(place_frame, text='Bottom-Right').place(x=150, y=65)

#Toplevel - a separate window opened on demand
def open_second_window():
    second = tk.Toplevel(root)
    second.title('Second Window')
    second.geometry('200x100')
    tk.Label(second, text='I am a Toplevel window').pack(expand=True)

tk.Button(root, text='Open Second Window', command=open_second_window).pack(pady=10)

root.mainloop()
