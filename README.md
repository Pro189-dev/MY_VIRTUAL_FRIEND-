# Chatterbox OS: My Virtual Friend

This is a rule-based conversational interface built entirely in Python. Unlike modern Large Language Models (LLMs), this application contains zero artificial intelligence, neural networks, or machine learning algorithms. It operates strictly on deterministic logic, regex, and string manipulation.

Designed as part of the Hack Club Crescent program, this project features a custom-built, graphical user interface (GUI) using `tkinter`

## Features

*   **Quick Engine:** Instantaneous responses based on hardcoded keyword clusters and logic trees.
*   **Dynamic Configuration:** Users can define their own designation and their virtual friend's name upon initialization.
*   **Embedded Typography:** Utilizes custom Google Fonts (Silkscreen and Audiowide), dynamically loaded into Windows memory at runtime via `ctypes`.
*   **Standalone Executable:** Fully packaged using PyInstaller so it can run on any Windows machine without requiring Python or external font installations.

## How It Works 

When a user transmits a message, the engine sanitizes the input by stripping away all punctuation and converting the string to lowercase. It then scans the standardized string against arrays of predefined keyword clusters (e.g., `school`, `homework`, `stuck`, `game`). 

If a match is detected, the execution flow routes to a specific dictionary key and retrieves a randomized, pre-written response from that category to simulate a fluid conversation. If no keywords match, the system triggers a generic fallback sequence.

## Critical System Limitations

Because this is a rule-based system, it operates with strict boundaries:
*   **No Contextual Awareness:** The program evaluates strings purely on a syntactic level and does not comprehend semantic meaning. 
*   **Absolute Zero Memory:** The system is stateless. Each input is processed in a vacuum, meaning it cannot remember previous messages or reference past topics.
*   **Strict Syntax Dependency:** Severe spelling errors or unrecognized slang will bypass the logic arrays and trigger a fallback response.

## Installation & Usage

**Option 1: Run the Executable (Windows Only)**
1. Navigate to the [Releases](#) tab and download `my_virtual_friend.exe`.
2. Double-click the executable. The custom fonts will temporarily load into memory, and the application will boot in full-screen mode.

**Option 2: Run from Source**
1. Clone this repository:
   git clone [https://github.com/Pro189-dev/my-virtual-friend.git](https://github.com/Pro189-dev/my-virtual-friend.git)
2.Navigate to the project directory:
  cd my-virtual-friend
3.Ensure you have Python installed, then run the script:
  python my_virtual_friend.py
