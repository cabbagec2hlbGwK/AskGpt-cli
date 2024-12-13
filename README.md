# AskGpt

# ChatGPT CLI Tool 🛠️

![https://img.shields.io/badge/python-3.7%2B-blue.svg](https://img.shields.io/badge/python-3.7%2B-blue.svg)

![https://img.shields.io/badge/OpenAI-API-purple.svg](https://img.shields.io/badge/OpenAI-API-purple.svg)

Interact with OpenAI's ChatGPT directly from your command line! This lightweight CLI tool allows you to send messages to ChatGPT and receive formatted responses, making it perfect for quick queries, scripting, and integrating AI into your workflow.

---

## 🚀 Features

- **Easy to Use:** Simple command-line interface.
- **Customizable:** Choose models, output formats, and system prompts.
- **Formatted Output:** Supports Markdown and plain text formatting with rich display in the terminal.
- **Flexible Input:** Send messages via arguments or standard input.
- **Lightweight Dependency:** Minimal external libraries required.

---

## 📖 Table of Contents

- [Installation](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Setup](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Usage](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Examples](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Creating a Batch File on Windows](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Contribution](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [License](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Acknowledgements](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)
- [Disclaimer](https://www.notion.so/AskGpt-15b1e2ed378780a79675f1d8f569bf90?pvs=21)

---

## 🧰 Installation

1. **Clone the Repository**
    
    ```bash
    git clone https://github.com/cabbagec2hlbGwK/AskGpt-cli
    cd AskGpt-cli
    
    ```
    
2. **Create a Virtual Environment (Optional but Recommended)**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate.bat
    
    ```
    
3. **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

---

## 🔧 Setup

### Configure OpenAI API Key

The tool requires an OpenAI API key to function. Set your API key as an environment variable:

- **On Unix/Linux/macOS**
    
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    
    ```
    
- **On Windows Command Prompt**
    
    ```
    set OPENAI_API_KEY=your-api-key-here
    
    ```
    
- **On Windows PowerShell**
    
    ```powershell
    $env:OPENAI_API_KEY="your-api-key-here"
    
    ```
    

*Replace `'your-api-key-here'` with your actual OpenAI API key.*

---

## 📌 Usage

```bash
python ask.py [options] [message]

```

### Options

- `m MODEL`, `-model MODEL`: Specify the model to use (default: `gpt-3.5-turbo`).
- `-format FORMAT`: Output format (`markdown` or `plain`, default: `markdown`).
- `-system SYSTEM_MESSAGE`: Set a custom system prompt (default: `"You are a helpful assistant."`).
- `h`, `-help`: Show help message and exit.

### Sending Messages

- **As Command-Line Arguments:**
    
    ```bash
    python ask.py "Your message here"
    
    ```
    
- **From Standard Input:**
    
    ```bash
    echo "Your message here" | python ask.py
    
    ```
    

---

## 💡 Examples

### 1. Basic Query

```bash
python ask.py "What is the capital of Japan?"

```

**Output:**

```
----------------------------------------------------------------------------------------------------
**The capital of Japan is Tokyo.**

```

### 2. Using a Different Model

```bash
python ask.py -m gpt-4 "Explain the theory of relativity in simple terms."

```

### 3. Custom System Prompt

```bash
python ask.py --system "You are a pirate speaking assistant." "Tell me a joke."

```

**Output:**

```
----------------------------------------------------------------------------------------------------
Arrr! Why do pirates take so long to learn the alphabet? Because they can spend years at C!

```

### 4. Plain Text Format

```bash
python ask.py --format plain "List three benefits of exercise."

```

**Output:**

```
----------------------------------------------------------------------------------------------------
1. Improves physical health by strengthening the cardiovascular system and muscles.
2. Enhances mental health by reducing stress, anxiety, and depression.
3. Boosts energy levels and promotes better sleep.

```

### 5. From a File Input

```bash
cat prompt.txt | python ask.py

```

---

## 📝 Creating a Batch File on Windows

To make the tool even more accessible on Windows, you can create a batch file that allows you to run the script from any directory without typing the full path every time.

### Steps to Create a Batch File:

1. **Open Notepad** or any text editor.
2. **Paste the following content**, replacing the path to your script:
    
    ```
    @python "C:\\path\\to\\your\\ask.py" %*
    
    ```
    
    Replace `"C:\\path\\to\\your\\ask.py"` with the actual path to your `ask.py` script.
    
3. **Save the File**:
    - **File Name**: Choose a name like `askai.bat` (ensure it has a `.bat` extension).
    - **Save Location**: Save the batch file in a directory that's included in your system's `PATH` environment variable, such as `C:\\Windows\\` or your user directory.
4. **Add to PATH (If Necessary)**:
    - If you prefer to save it in a custom directory, you need to add that directory to your system's `PATH` environment variable.
    - **How to Add to PATH**:
        - Press `Win + X` and select `System`.
        - Click on `Advanced system settings`.
        - Click on `Environment Variables`.
        - Under `System variables`, find and select `Path`, then click `Edit`.
        - Click `New` and add the path to the directory containing your batch file.
        - Click `OK` to close all dialogs.
5. **Usage**:
    
    Now you can use the `askai` command from any command prompt window.
    
    ```
    askai "How does photosynthesis work?"
    
    ```
    
6. **Examples**:
    
    **Asking a Question**:
    
    ```
    askai "Explain Newton's laws of motion."
    
    ```
    
    **Using Options**:
    
    ```
    askai --format plain --system "You are a motivational coach." "Give me some advice."
    
    ```
    

### Benefits:

- **Convenience**: Run the command from any directory without specifying the full path.
- **Quick Access**: Shorten the command to a simple word like `askai`.
- **Script Integration**: Easily use the tool within other scripts or batch files.

---

## 🤝 Contribution

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

---

## 🌟 Acknowledgements

- [OpenAI](https://openai.com/) for providing powerful AI models.
- [Rich Library](https://github.com/Textualize/rich) for amazing terminal formatting.

---

## 📢 Disclaimer

This tool uses the OpenAI API, which may incur costs depending on your usage. Please monitor your API usage and understand the pricing details on the [OpenAI Pricing](https://openai.com/pricing/) page.

---

Enjoy seamless AI conversations right from your terminal! If you find this tool helpful, give it a star ⭐ on GitHub.

---