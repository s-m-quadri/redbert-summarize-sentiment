# 🔴 RedBERT: Summarize & Sentiment Analysis GUI

A desktop application to **summarize** and analyze the **sentiment** of any text using state-of-the-art **BERT** models from HuggingFace — all in a clean, themed **Tkinter GUI**.

### ✨ Features

- 🔍 **Text Summarization** powered by `BART` (HuggingFace Transformers)
- 😊 **Sentiment Analysis** using `distilBERT`
- 🖥️ Desktop GUI built with `Tkinter` (Python standard GUI library)
- 🎨 Custom red-themed interface with live status updates
- ✅ Clean layout with non-editable summary, real-time feedback
- 📦 One-click `.exe` build available in the [Releases](../../releases) section

### 📷 Screenshot

> *Coming soon – or add one here!*

### 🚀 Getting Started

#### ✅ Prerequisites

- Python `3.11.0` (used during development)
- Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
````

#### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 🖥️ Run the App

```bash
python gui.py
```

### 🛠️ Packaging into `.exe`

To build the standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller setup.spec
```

> The `.exe` will be available in `dist/Red Bert.exe`
> Or simply download it from the [Releases](../../releases) tab.

### 📁 Project Structure

```
redbert-summarize-sentiment/
│
├── gui.py               # Main GUI frontend
├── logic.py             # NLP logic (summarization + sentiment)
└── setup.spec           # PyInstaller configuration
```

### 🧠 Built With

* [Transformers (HuggingFace)](https://huggingface.co/transformers/)
* [PyTorch](https://pytorch.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [PyInstaller](https://pyinstaller.org/)

### 📜 License

This project is licensed under the **GNU General Public License v3.0** – see the [LICENSE](LICENSE) file for details.


### ⭐️ Support

If you find this helpful, please consider giving it a ⭐️ or sharing it!