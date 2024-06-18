import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analyzer")
        self.geometry("1000x600")
        self.create_widgets()

    def create_widgets(self):
        # Button to load CSV
        self.load_button = tk.Button(self, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Combobox for selecting column to sort/filter
        self.column_select = ttk.Combobox(self, state='readonly')
        self.column_select.pack(pady=10)

        # Entry for filter value
        self.filter_entry = tk.Entry(self)
        self.filter_entry.pack(pady=10)
        self.filter_entry.insert(0, "Filter value")

        # Button to apply filter
        self.filter_button = tk.Button(self, text="Filter", command=self.apply_filter)
        self.filter_button.pack(pady=10)

        # Button to apply sorting
        self.sort_button = tk.Button(self, text="Sort", command=self.apply_sort)
        self.sort_button.pack(pady=10)

        # Button to plot data
        self.plot_button = tk.Button(self, text="Plot", command=self.plot_data)
        self.plot_button.pack(pady=10)

        # Treeview to display data
        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill='both')

        # Status bar
        self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.display_data(self.data)
            self.column_select['values'] = list(self.data.columns)
            self.column_select.current(0)
            self.status.config(text=f"Loaded {file_path}")

    def display_data(self, data):
        self.tree.delete(*self.tree.get_children())
        self.tree["column"] = list(data.columns)
        self.tree["show"] = "headings"
        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
        for _, row in data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def apply_filter(self):
        column = self.column_select.get()
        value = self.filter_entry.get()
        filtered_data = self.data[self.data[column].astype(str).str.contains(value)]
        self.display_data(filtered_data)

    def apply_sort(self):
        column = self.column_select.get()
        sorted_data = self.data.sort_values(by=column)
        self.display_data(sorted_data)

    def plot_data(self):
        column = self.column_select.get()
        if column:
            plt.figure(figsize=(10, 6))
            self.data[column].value_counts().plot(kind='bar')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()


if __name__ == "__main__":
    app = DataAnalyzerApp()
    app.mainloop()
