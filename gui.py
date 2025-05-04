import tkinter as tk
from tkinter import scrolledtext
import threading
import logic
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Theme colors
BG_COLOR = "#ffe0e0"
TEXT_COLOR = "#4d0000"
BUTTON_COLOR = "#b30000"
ENTRY_BG = "#fff5f5"
HIGHLIGHT = "#ff9999"
STATUS_BG = "#990000"
STATUS_FG = "white"

FONT = ("Arial", 11)
TITLE_FONT = ("Arial", 22, "bold")
SUBTITLE_FONT = ("Arial", 12, "italic")
SECTION_LABEL = ("Arial", 11, "bold")

# GUI logic
def start_processing():
    text = input_field.get("1.0", tk.END).strip()
    if not text:
        update_status("Error: Input is empty.", "red")
        return

    summary_output.config(state='normal')
    summary_output.delete("1.0", tk.END)
    summary_output.config(state='disabled')
    sentiment_output.config(text="")
    update_status("Processing...", "orange")

    def task():
        try:
            summary = logic.summarize_text(text)
            sentiment_result = logic.analyze_sentiment(summary)

            summary_output.config(state='normal')
            summary_output.insert(tk.END, summary)
            summary_output.config(state='disabled')

            sentiment_output.config(text=f"Sentiment: {sentiment_result}", fg=TEXT_COLOR)
            update_status("Success!", "green")
        except Exception as e:
            update_status(f"Error: {e}", "red")

    threading.Thread(target=task).start()

def update_status(message, color):
    status_bar.config(text=message, fg=STATUS_FG, bg=STATUS_BG if color == "green" else "#cc0000")

# Main GUI window
app = tk.Tk()
app.title("BERT Summarizer + Sentiment Analyzer")
app.iconbitmap(resource_path("icon.ico"))
app.configure(bg=BG_COLOR)
app.geometry("800x600")
app.resizable(False, False)

# Title
tk.Label(app, text="BERT Text Analyzer", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(20, 0))
tk.Label(app, text="Summarize and evaluate text sentiment instantly", font=SUBTITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(0, 15))

# Input
tk.Label(app, text="Input Text:", font=SECTION_LABEL, bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor='w', padx=20)
input_field = scrolledtext.ScrolledText(app, height=10, width=90, font=FONT, bg=ENTRY_BG, highlightbackground=HIGHLIGHT)
input_field.pack(pady=5, padx=20)

# Process button
tk.Button(app, text="Process", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg="white", command=start_processing).pack(pady=10)

# Summary
tk.Label(app, text="Summary:", font=SECTION_LABEL, bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor='w', padx=20, pady=(5, 0))
summary_output = scrolledtext.ScrolledText(app, height=7, width=90, font=FONT, bg=ENTRY_BG, highlightbackground=HIGHLIGHT)
summary_output.pack(pady=(0, 5), padx=20)
summary_output.config(state='disabled')

# Sentiment
sentiment_output = tk.Label(app, text="", font=("Arial", 12, "bold"), bg=BG_COLOR)
sentiment_output.pack(pady=(5, 10))

# Status bar at bottom
status_bar = tk.Label(app, text="Ready", bd=1, relief=tk.SUNKEN, anchor='w', font=("Arial", 10, "bold"),
                      bg=STATUS_BG, fg=STATUS_FG)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Launch
app.mainloop()
