import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import traceback

def send_request():
    messagebox.showinfo("Заявка принята", "С вами свяжутся в течении 24 часов!")

def on_logo_click(event):
    global logo_x, logo_y
    logo_x, logo_y = event.x, event.y

def on_logo_drag(event):
    global logo_x, logo_y
    new_x, new_y = event.x, event.y
    canvas.move(logo_id, new_x - logo_x, new_y - logo_y)
    logo_x, logo_y = new_x, new_y

def move_start(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def move_drag(event):
    global start_x, start_y
    form_frame.place(x=root.winfo_pointerx() - root.winfo_rootx() - start_x,
                     y=root.winfo_pointery() - root.winfo_rooty() - start_y,
                     anchor=tk.NW)

def change_images():
    current_image_id = bottom_right_image_id
    current_image = canvas.itemcget(current_image_id, "image")
    next_image = background2_img if current_image == str(background_img) else background_img
    canvas.itemconfig(current_image_id, image=next_image)
    root.after(10000, change_images)  

root = tk.Tk()
root.title("Приложение для компании ООО Маминсон тревел")

try:
    initial_width, initial_height = 1600, 940

    background_image = Image.open("fon.jpg")
    background_image = background_image.resize((initial_width, initial_height), Image.ANTIALIAS)
    background_img = ImageTk.PhotoImage(background_image)

    background2_image = Image.open("okno.png")
    background2_image = background2_image.resize((initial_width, initial_height), Image.ANTIALIAS)
    background2_img = ImageTk.PhotoImage(background2_image)

    logo_image = Image.open("logo.jpg")
    logo_image = logo_image.resize((logo_image.width // 2, logo_image.height // 2), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(logo_image)

    root.geometry(f"{initial_width}x{initial_height}")

    canvas = tk.Canvas(root, width=initial_width, height=initial_height)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=background_img, tags="bg_images")

    bottom_right_image_id = canvas.create_image(initial_width, initial_height, anchor=tk.SE, image=background_img, tags="images")

    logo_id = canvas.create_image(initial_width // 2, initial_height // 2, anchor=tk.CENTER, image=logo_img)
    logo_x, logo_y = initial_width // 2, initial_height // 2

    form_width = int((initial_width - 40) / 3.5)  

    form_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
    form_frame.place(x=20, y=20, width=form_width, height=80)

    name_label = tk.Label(form_frame, text="Имя:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = tk.Label(form_frame, text="Номер телефона:")
    phone_label.grid(row=0, column=2, padx=5, pady=5)

    phone_entry = tk.Entry(form_frame)
    phone_entry.grid(row=0, column=3, padx=5, pady=5)

    submit_button = tk.Button(form_frame, text="Отправить заявку", command=send_request)
    submit_button.grid(row=1, columnspan=4, padx=5, pady=5)

    canvas.tag_bind(logo_id, "<Button-1>", on_logo_click)
    canvas.tag_bind(logo_id, "<B1-Motion>", on_logo_drag)

    form_frame.bind("<Button-1>", move_start)
    form_frame.bind("<B1-Motion>", move_drag)

    root.after(10000, change_images)

    root.mainloop()

except Exception as e:
    traceback.print_exc()
    print("Ошибка при загрузке и изменении размеров изображения фона или логотипа:", e)
