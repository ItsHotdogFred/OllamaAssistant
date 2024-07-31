from pathlib import Path
import ollama
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/ryan/CoolGUI/ExportedFigma/Siama/build/assets/frame0")

initial_width = 700
initial_height = 115
min_height = 115
expansion_step = 10  # Expand by 10px

chat_history = []  # Initialize chat_history as a list

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def reset_window_size():
    window.geometry(f"{initial_width}x{initial_height}")
    canvas.configure(height=initial_height)
    responsetext.place(x=27, y=88, width=650, height=27)

def check_and_expand_window():
    current_height = window.winfo_height()
    text_height = responsetext.winfo_reqheight()
    response_area_height = current_height - 88  # Subtract the height of the upper part

    if text_height > response_area_height:
        new_height = current_height + expansion_step
        window.geometry(f"{initial_width}x{new_height}")
        canvas.configure(height=new_height)
        responsetext.place(x=27, y=88, width=650, height=new_height - 88)

def getinput():
    global chat_history
    reset_window_size()
    responsetext.configure(state="normal")
    inp = entry_1.get()
    entry_1.delete(0, 'end')
    responsetext.delete(1.0, 'end')

    chat_history.append({"role": "user", "content": inp})

    try:
        stream = ollama.chat(
            model='llama3',
            messages=chat_history,
            stream=True,
        )

        assistant_response = ""
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            responsetext.insert('end', content)
            responsetext.see('end')
            responsetext.update_idletasks()
            check_and_expand_window()
            assistant_response += content

        chat_history.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        responsetext.insert('end', f"An error occurred: {e}")

    responsetext.configure(state="disabled")

window = Tk()
window.geometry(f"{initial_width}x{initial_height}")
window.configure(bg="#151517")
window.minsize(initial_width, min_height)

canvas = Canvas(
    window,
    bg="#151517",
    height=initial_height,
    width=initial_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(350.0, 57.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(311.0, 57.0, image=image_image_2)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(302.0, 68.5, image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#1C1A1E",
    fg="#FFFFFF",
    highlightthickness=0,
    font=('Open Sans, Bold', 16),
    highlightcolor="#FFFFFF",
)
entry_1.place(x=27.0, y=38.0, width=550.0, height=39.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=getinput,
    relief="flat",
    bg="#161517",
    activebackground="#161517",
)
button_1.place(x=606.0, y=25.0, width=77.0, height=64.0)

responsetext = Text(
    window,
    bd=0,
    bg="#151517",
    fg="#FFFFFF",
    highlightthickness=0,
    font=('Open Sans, Bold', 16),
    wrap='word'
)
responsetext.place(x=27, y=88, width=650, height=27)
responsetext.configure(state="disabled")

window.resizable(False, True)
window.title("Siri Ollama Bot")
window.attributes('-topmost', True)
window.mainloop()
