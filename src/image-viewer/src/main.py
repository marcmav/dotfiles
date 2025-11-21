import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Sierra')
root.configure(bg='#1e1e1e')

# --- Top frame ---
top_frame = tk.Frame(root, bg='#252526', height=50)
top_frame.pack(fill='x', side='top')
top_frame.pack_propagate(False)

label = tk.Label(
    top_frame,
    text='Sierra',
    font=('Fira Code', 11),
    bg='#252526',
    fg='#d4d4d4')
label.pack(expand=True)

# --- Center frame for image ---
image_frame = tk.Frame(root, bg='#1e1e1e')
image_frame.pack(expand=True, fill='both')

# Image label
image_label = tk.Label(image_frame, bg='#1e1e1e')
image_label.pack(expand=True)

# --- Bottom frame ---
bottom_frame = tk.Frame(root, bg='#252526', height=50)
bottom_frame.pack(fill='x', side='bottom')
bottom_frame.pack_propagate(False)

command_entry = tk.Entry(
    bottom_frame,
    font=('Fira Sans', 9),
    width=30,
    bg='#333333',
    fg='#d4d4d4',
    insertbackground='#aeafad')
command_entry.pack(side='right', padx=(0, 10), pady=10)
command_entry.focus()

command_label = tk.Label(
    bottom_frame,
    text='Command:',
    font=('Fira Sans', 9),
    bg='#252526',
    fg='#d4d4d4')
command_label.pack(side='right', padx=(0, 5))

# --- Functions ---
current_image = None

def display_image(path):
    global current_image
    try:
        img = Image.open(path)
        img = img.resize((600, 400))  # fixed size
        current_image = ImageTk.PhotoImage(img)
        image_label.config(image=current_image)
    except Exception as e:
        print(f'Error opening image: {e}')

def open_file_dialog():
    '''Open file explorer to choose image.'''
    file_path = filedialog.askopenfilename(
        filetypes=[('Image files', '*.png *.jpg *.jpeg *.gif *.bmp')]
    )
    if file_path:
        display_image(file_path)

def run_command(event=None):
    '''Run commands from entry box.'''
    cmd = command_entry.get().strip().lower()

    if cmd == 'open':
        # open file manager if no path is given
        open_file_dialog()

    elif cmd.startswith('open '):
        path = cmd[5:].strip()
        display_image(path)

    elif cmd == 'close':
        image_label.config(image='')

    command_entry.delete(0, tk.END)

# Bind Enter key
command_entry.bind('<Return>', run_command)

root.mainloop()     