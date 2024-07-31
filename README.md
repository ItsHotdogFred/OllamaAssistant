# Siri Ollama Bot GUI

A graphical user interface for interacting with the Ollama AI model, built using Python and Tkinter. This version features dynamic window resizing for a better user experience.

## Features

- Clean and minimalist interface
- Integration with Ollama AI model
- Chat history for contextual conversations
- Dynamic window resizing for better readability of longer responses
- Simple text display without markdown formatting

## Recent Changes

- Implemented dynamic window resizing: The window now expands automatically as the AI's response grows longer.
- Removed markdown formatting: Responses are displayed as plain text for simplicity.
- Added minimum window height to ensure UI elements are always visible.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Ollama installed and running on your system
- Required Python packages: `tkinter`, `ollama`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/siri-ollama-bot-gui.git
   ```

2. Navigate to the project directory:
   ```
   cd siri-ollama-bot-gui
   ```

3. Install the required Python packages:
   ```
   pip install ollama
   ```

   Note: `tkinter` usually comes pre-installed with Python. If it's not available, you may need to install it separately.

## Usage

1. Ensure that the Ollama service is running on your system.

2. Run the script:
   ```
   python siri_ollama_bot.py
   ```

3. The GUI window will appear. Enter your question or prompt in the input field and click the send button or press Enter.

4. The AI's response will appear in the text area below the input field. The window will automatically resize as the response grows longer.

## Customization

You can customize the appearance and behavior of the GUI by modifying the following variables in the script:

- `initial_width`: Initial width of the window
- `initial_height`: Initial height of the window
- `min_height`: Minimum height of the window
- `expansion_step`: Number of pixels to expand the window height by when needed

## How Dynamic Windowing Works

1. The `check_and_expand_window()` function is called after each chunk of the AI's response is received.
2. It compares the required height of the text with the available space in the window.
3. If the text overflows, the window height is increased by `expansion_step` pixels.
4. The canvas and response text area are resized accordingly.

This process ensures that the entire response is always visible, providing a smooth user experience.

## Contributing

Contributions to the Siri Ollama Bot GUI are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Ollama](https://github.com/jmorganca/ollama) for the AI model integration
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework
