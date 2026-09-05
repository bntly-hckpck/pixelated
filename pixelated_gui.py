import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image
from pixelated import pixelated_img

# main window
root = tk.Tk()
root.title("pixelated")
window_width = 900
window_height = 600
root.resizable(False, False)

# screen dimensions & center points
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_center = int(screen_width/2 - window_width / 2)
y_center = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{x_center}+{y_center}') # centering main window

# file paths
input_path = tk.StringVar(value="no input path selected yet")
output_path = tk.StringVar(value="no output path selected yet")

# image choosing
def input_image():
    filepath = filedialog.askopenfilename(title="select image to pixelate", filetypes=[("PNG files", "*.png")])
    input_path.set(filepath)

# image saving
def image_output():
    filepath = filedialog.asksaveasfilename(title="save pixelated image as", filetypes=[("PNG files", "*.png")])
    output_path.set(filepath)

# image pixelation
def pixelate():
    if input_path.get() == "no input path selected yet":
        messagebox.showwarning("pixelated", "select input image first")
        return
    if output_path.get() == "no output path selected yet":
        messagebox.showwarning("pixelated", "select output path first")
        return
    try:
        image = Image.open(input_path.get())
        output = output_path.get()
        result = pixelated_img(image, 64, 64)
        result.save(output)
        messagebox.showinfo("pixelated", "image saved")
    except Exception as e:
        messagebox.showerror("pixelated", f"error: {e}")

# input elements

# output elements

# pixelating elements

root.mainloop()


