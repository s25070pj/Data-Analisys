import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analyzer")
        self.geometry("1000x600")
        self.data = None
        self.filtered_data = None
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

        # Entry for numerical range filter
        self.min_value_entry = tk.Entry(self)
        self.min_value_entry.pack(pady=5)
        self.min_value_entry.insert(0, "Min value")

        self.max_value_entry = tk.Entry(self)
        self.max_value_entry.pack(pady=5)
        self.max_value_entry.insert(0, "Max value")

        # Button to apply numerical range filter
        self.range_filter_button = tk.Button(self, text="Filter by Range", command=self.apply_range_filter)
        self.range_filter_button.pack(pady=10)

        # Combobox for selecting plot type
        self.plot_type_select = ttk.Combobox(self, state='readonly', values=["Bar", "Pie", "Advanced"])
        self.plot_type_select.pack(pady=10)
        self.plot_type_select.current(0)

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
            self.filtered_data = self.data.copy()  # Initialize filtered_data
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
        self.filtered_data = self.data[self.data[column].astype(str).str.contains(value)]
        self.display_data(self.filtered_data)

    def apply_range_filter(self):
        column = self.column_select.get()
        min_value = self.min_value_entry.get()
        max_value = self.max_value_entry.get()
        if column and min_value and max_value:
            min_value = float(min_value)
            max_value = float(max_value)
            self.filtered_data = self.data[(self.data[column] >= min_value) & (self.data[column] <= max_value)]
            self.display_data(self.filtered_data)

    def apply_sort(self):
        column = self.column_select.get()
        self.filtered_data = self.filtered_data.sort_values(by=column)
        self.display_data(self.filtered_data)

    def plot_data(self):
        column = self.column_select.get()
        plot_type = self.plot_type_select.get()
        if column:
            data_to_plot = self.filtered_data if self.filtered_data is not None else self.data
            if plot_type == "Bar":
                plt.figure(figsize=(10, 6))
                data_to_plot[column].value_counts().plot(kind='bar')
                plt.title(f'Distribution of {column}', fontsize=16)
                plt.xlabel(column, fontsize=14)
                plt.ylabel('Frequency', fontsize=14)
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.show()
            elif plot_type == "Pie":
                plt.figure(figsize=(10, 6))
                data_to_plot[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
                plt.title(f'Distribution of {column}', fontsize=16)
                plt.ylabel('')
                plt.show()
            elif plot_type == "Advanced":
                self.advanced_plot(data_to_plot)

    def advanced_plot(self, data):
        plt.figure(figsize=(10, 6))
        sns.pairplot(data)
        plt.suptitle('Pairplot of Dataset Features', fontsize=16)
        plt.show()


if __name__ == "__main__":
    app = DataAnalyzerApp()
    app.mainloop()
