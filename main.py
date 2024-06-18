import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analyzer")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=20)

        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill='both')

        self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.display_data(self.data)
            self.status.config(text=f"Loaded {file_path}")

    def display_data(self, data):
        self.tree.delete(*self.tree.get_children())
        self.tree["column"] = list(data.columns)
        self.tree["show"] = "headings"
        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
        for _, row in data.iterrows():
            self.tree.insert("", "end", values=list(row))


if __name__ == "__main__":
    app = DataAnalyzerApp()
    app.mainloop()
