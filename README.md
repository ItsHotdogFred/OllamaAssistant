# Siri Ollama Bot

Siri Ollama Bot is a Python-based chatbot application with a graphical user interface. It uses the Ollama API to interact with the Llama 3 language model, providing a user-friendly interface for conversational AI interactions.

## Features

- Graphical User Interface (GUI) built with Tkinter
- Integration with Ollama API for Llama 3 model interactions
- Real-time streaming of AI responses
- Markdown-style formatting for chat messages, including:
  - Headers (H1 to H4)
  - Bold and italic text
  - Code blocks and inline code
- Dynamic window resizing based on content
- Chat history management

## Requirements

- Python 3.x
- Ollama
- Tkinter
- Pathlib

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/siri-ollama-bot.git
   cd siri-ollama-bot
   ```

2. Install the required dependencies:
   ```
   pip install ollama
   ```

3. Ensure you have Tkinter installed. It comes pre-installed with most Python distributions.

4. Make sure you have Ollama set up and running on your system.

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. The GUI window will appear. Type your message in the input field and press the send button or hit Enter.

3. The AI's response will appear in the text area below, with real-time updates as the response is generated.

4. The window will automatically resize if the response is longer than the current view.

## Customization

- You can modify the `ASSETS_PATH` variable to point to your custom assets directory.
- Adjust the initial window size by changing `initial_width` and `initial_height` variables.
- Modify the Ollama model by changing the `model` parameter in the `ollama.chat()` function call.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- This project uses the Ollama API for AI interactions.
- The GUI is built using Python's Tkinter library.
