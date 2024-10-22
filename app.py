import tkinter as tk
from tkinter import filedialog

DEFAULT_TITLE = "PyText"

root = tk.Tk()
root.title(DEFAULT_TITLE)

text = tk.Text(root, wrap="word", undo=True)
text.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


def new_file():
    """Inicia um novo arquivo em branco."""

    text.delete("1.0", tk.END)
    root.title(DEFAULT_TITLE)


def open_file():
    """Abre um arquivo existente."""

    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
        root.title(file_path)


def save_file():
    """Salva o conteúdo do editor em um arquivo no disco."""

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            content = text.get("1.0", tk.END)
            file.write(content)
        root.title(file_path)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

root.mainloop()
