from pathlib import Path
import ollama
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, font
import re

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

def apply_markdown_formatting(text):
    def process_code_blocks(match):
        code = match.group(1).strip()
        code = re.sub(r'<', '&lt;', code)
        code = re.sub(r'>', '&gt;', code)
        code = code.replace('\n', '<br>')
        return f'<codeblock>{code}</codeblock>'

    text = re.sub(r'```(.*?)```', process_code_blocks, text, flags=re.DOTALL)

    parts = re.split(r'(<codeblock>.*?</codeblock>)', text, flags=re.DOTALL)

    for i, part in enumerate(parts):
        if not part.startswith('<codeblock>'):
            # Headers (now supporting up to 4 levels)
            part = re.sub(r'^####\s+(.*?)$', r'<h4>\1</h4>', part, flags=re.MULTILINE)
            part = re.sub(r'^###\s+(.*?)$', r'<h3>\1</h3>', part, flags=re.MULTILINE)
            part = re.sub(r'^##\s+(.*?)$', r'<h2>\1</h2>', part, flags=re.MULTILINE)
            part = re.sub(r'^#\s+(.*?)$', r'<h1>\1</h1>', part, flags=re.MULTILINE)

            # Bold
            part = re.sub(r'\*\*(.*?)\*\*', r'<bold>\1</bold>', part)
            # Italic
            part = re.sub(r'\*(.*?)\*', r'<italic>\1</italic>', part)
            # Inline code
            part = re.sub(r'`(.*?)`', r'<code>\1</code>', part)

            parts[i] = part

    return ''.join(parts)

def insert_formatted_text(widget, text):
    widget.delete(1.0, 'end')
    formatted_text = apply_markdown_formatting(text)

    # Define tags for different styles
    widget.tag_configure("bold", font=('Open Sans', 16, 'bold'))
    widget.tag_configure("italic", font=('Open Sans', 16, 'italic'))
    widget.tag_configure("code", font=('Open Sans', 14), background="#1d2231", foreground="#ffffff")
    widget.tag_configure("codeblock", font=('Open Sans', 14), background="#1d2231", foreground="#ffffff")

    # Configure header styles
    widget.tag_configure("h1", font=('Open Sans', 24, 'bold'), spacing3=10)
    widget.tag_configure("h2", font=('Open Sans', 20, 'bold'), spacing3=8)
    widget.tag_configure("h3", font=('Open Sans', 18, 'bold'), spacing3=6)
    widget.tag_configure("h4", font=('Open Sans', 16, 'bold'), spacing3=4)  # New h4 style

    # Split the text into paragraphs
    paragraphs = re.split(r'(\n{2,})', formatted_text)

    for paragraph in paragraphs:
        if paragraph.strip() == '':
            widget.insert('end', paragraph)
            continue

        if paragraph.startswith('<codeblock>') and paragraph.endswith('</codeblock>'):
            code_content = paragraph[11:-12]  # Remove <codeblock> tags
            lines = code_content.split('<br>')
            for line in lines:
                widget.insert('end', line + '\n', 'codeblock')
        else:
            lines = paragraph.split('\n')
            for line in lines:
                if line.startswith('<h1>'):
                    content = line[4:-5]
                    widget.insert('end', content + '\n', 'h1')
                elif line.startswith('<h2>'):
                    content = line[4:-5]
                    widget.insert('end', content + '\n', 'h2')
                elif line.startswith('<h3>'):
                    content = line[4:-5]
                    widget.insert('end', content + '\n', 'h3')
                elif line.startswith('<h4>'):  # New h4 handling
                    content = line[4:-5]
                    widget.insert('end', content + '\n', 'h4')
                else:
                    parts = re.split(r'(</?(?:bold|italic|code)>)', line)
                    current_tags = []
                    for part in parts:
                        if part == '<bold>':
                            current_tags.append('bold')
                        elif part == '</bold>':
                            current_tags.remove('bold')
                        elif part == '<italic>':
                            current_tags.append('italic')
                        elif part == '</italic>':
                            current_tags.remove('italic')
                        elif part == '<code>':
                            current_tags = ['code']
                        elif part == '</code>':
                            current_tags = []
                        else:
                            widget.insert('end', part, tuple(current_tags))
                widget.insert('end', '\n')

def getinput():
    global chat_history
    reset_window_size()
    responsetext.configure(state="normal")
    inp = entry_1.get()
    entry_1.delete(0, 'end')
    responsetext.delete(1.0, 'end')

    # Append the user's message to the chat history
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
            insert_formatted_text(responsetext, assistant_response + content)
            responsetext.see('end')
            responsetext.update_idletasks()
            check_and_expand_window()
            assistant_response += content

        # Append the assistant's message to the chat history
        chat_history.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        insert_formatted_text(responsetext, f"An error occurred: {e}")

    responsetext.configure(state="disabled")

def check_and_expand_window():
    current_height = window.winfo_height()
    text_height = responsetext.winfo_reqheight()
    response_area_height = current_height - 88  # Subtract the height of the upper part

    if text_height > response_area_height:
        new_height = current_height + expansion_step
        window.geometry(f"{initial_width}x{new_height}")
        canvas.configure(height=new_height)
        responsetext.place(x=27, y=88, width=650, height=new_height - 88)

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
