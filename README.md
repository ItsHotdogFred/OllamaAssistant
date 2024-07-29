# Ollama Bot GUI

A simple graphical user interface for interacting with the Ollama AI model, built using Python and Tkinter.

## Features

- Clean and minimalist interface
- Integration with Ollama AI model
- Chat history for contextual conversations
- Expandable window for better readability of longer responses

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

4. The AI's response will appear in the expanded text area below the input field.

## Customization

You can customize the appearance and behavior of the GUI by modifying the following variables in the script:

- `initial_width`: Initial width of the window
- `initial_height`: Initial height of the window
- `expanded_height`: Height of the window when expanded to show the AI's response

## Contributing

Contributions to the Siri Ollama Bot GUI are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Ollama](https://github.com/jmorganca/ollama) for the AI model integration
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework
