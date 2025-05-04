![thumbnail](https://github.com/user-attachments/assets/8de0144b-5401-41dc-8747-0f738ee5394b)

<div align="center">
  <h1><b><code>RedBERT</code> Summarize & Sentiment Analyzer</b></h1>
  <p><strong>RedBERT</strong> is a desktop NLP tool that summarizes and analyzes text sentiment using powerful BERT-based models inside a beautiful red-themed GUI.</p>

  <p>
    <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment">Repository</a> ·
    <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/releases">Download EXE</a> ·
    <a href="mailto:dev.smq@gmail.com">Contact</a> ·
  </p>

  <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/releases">
    <img src="https://custom-icon-badges.demolab.com/github/v/tag/s-m-quadri/redbert-summarize-sentiment?label=Version&labelColor=302d41&color=f2cdcd&logoColor=d9e0ee&logo=tag&style=for-the-badge" alt="Release Version"/>
  </a>
  <a href="https://www.codefactor.io/repository/github/s-m-quadri/redbert-summarize-sentiment"><img src="https://img.shields.io/codefactor/grade/github/s-m-quadri/redbert-summarize-sentiment?label=CodeFactor&labelColor=302d41&color=8bd5ca&logoColor=d9e0ee&logo=codefactor&style=for-the-badge" alt="GitHub Readme Profile Code Quality"/></a>
  <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/issues">
    <img src="https://custom-icon-badges.demolab.com/github/issues/s-m-quadri/redbert-summarize-sentiment?label=Issues&labelColor=302d41&color=f5a97f&logoColor=d9e0ee&logo=issue&style=for-the-badge" alt="Issues"/>
  </a>
  <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/pulls">
    <img src="https://custom-icon-badges.demolab.com/github/issues-pr/s-m-quadri/redbert-summarize-sentiment?label=PRs&labelColor=302d41&color=ddb6f2&logoColor=d9e0ee&logo=git-pull-request&style=for-the-badge" alt="Pull Requests"/>
  </a>
  <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/graphs/contributors">
    <img src="https://custom-icon-badges.demolab.com/github/contributors/s-m-quadri/redbert-summarize-sentiment?label=Contributors&labelColor=302d41&color=c9cbff&logoColor=d9e0ee&logo=people&style=for-the-badge" alt="Contributors"/>
  </a>

  <p>
    <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml">Report Bug</a> · 
    <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml">Request Feature</a> · 
    <a href="https://github.com/s-m-quadri/redbert-summarize-sentiment/discussions/new?category=q-a">Ask Question</a>
  </p>
</div>


# 🔴 RedBERT: Summarize & Sentiment Analysis GUI

A desktop application to **summarize** and analyze the **sentiment** of any text using state-of-the-art **BERT** models from HuggingFace — all in a clean, themed **Tkinter GUI**.

### ✨ Features

- 🔍 **Text Summarization** powered by `BART` (HuggingFace Transformers)
- 😊 **Sentiment Analysis** using `distilBERT`
- 🖥️ Desktop GUI built with `Tkinter` (Python standard GUI library)
- 🎨 Custom red-themed interface with live status updates
- ✅ Clean layout with non-editable summary, real-time feedback
- 📦 One-click `.exe` build available in the [Releases](../../releases) section

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
