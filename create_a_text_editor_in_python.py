import tkinter as tk # some lines are put together using ";" due to space.
from tkinter import filedialog
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete('1.0', tk.END)
            text_editor.insert(tk.END, file.read())
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get('1.0', tk.END))
window = tk.Tk()
window.title("Text Editor") 
text_editor = tk.Text(window); text_editor.pack()
menu_bar = tk.Menu(window); window.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
window.mainloop() 