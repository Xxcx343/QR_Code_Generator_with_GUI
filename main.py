import qrcode
import os
import tkinter as tk
from tkinter import filedialog


def generate_qrcode():
    if entry_filename.get() and entry_qradress.get():
        qradress = entry_qradress.get()
        filename = entry_filename.get() + ".png"
        directory = entry_directory.get()

        image = qrcode.make(qradress)
        image_path = os.path.join(directory, filename)
        image.save(image_path)
        label_result.config(text=f"QR code was generated!")

    elif entry_filename.get():
        label_result.config(text=f"Give a data for QR code!")

    elif entry_qradress.get():
        label_result.config(text=f"Give a name for QR code!")

    else:
        label_result.config(text=f"Give a data and name for QR code!")




def browse_directory():
    directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory)


# create tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# create GUI elements
label_qradress = tk.Label(window, text="Data for qrcode:")
label_filename = tk.Label(window, text="Name for qrcode:")


entry_qradress = tk.Entry(window)
entry_filename = tk.Entry(window)
entry_directory = tk.Entry(window)

button_generate = tk.Button(window, text="Make Qr Code", command=generate_qrcode)
button_directory = tk.Button(window, text="Choose Folder", command=browse_directory)

label_result = tk.Label(window)

# GUI using grid layout
label_qradress.grid(row=0, column=0)
entry_qradress.grid(row=0, column=1)
label_filename.grid(row=1, column=0)
entry_filename.grid(row=1, column=1)

button_directory.grid(row=1, column=2)
button_generate.grid(row=2, column=2)
label_result.grid(row=2, column=1)


# start tkinter event loop
window.mainloop()