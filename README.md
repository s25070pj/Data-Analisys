# Data Analyzer

Data Analyzer is an application for data analysis using NumPy, Pandas, Matplotlib, and Seaborn libraries. The application allows loading datasets, exploring data, and generating various charts. This project was created as a college assignment.

## Features

- Load CSV files
- Display data in a table
- Filter data by text values
- Filter data by numerical ranges
- Reset filters
- Sort data
- Generate bar, pie, and advanced charts
- Communicate basic insights from data analysis

## Installation

1. Ensure you have the latest version of Python installed.
2. Clone the project repository to your computer.
3. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # for Linux/Mac
   venv\Scripts\activate      # for Windows
Install the required libraries:
bash
Skopiuj kod
pip install -r requirements.txt
Usage
Run the application:
bash
Skopiuj kod
python main.py
Load a CSV file by clicking the "Load CSV" button.
Use the available options to filter and sort data.
Select the chart type from the dropdown menu and click the "Plot" button to generate a chart.
Project Structure
main.py - Main file to run the application
requirements.txt - File with the required libraries
README.md - Project documentation
Explanation of Methods and Programming Solutions
Data Analysis Methods
Data Filtering: Allows users to filter data by text values and numerical ranges. This is useful for large datasets where only specific information is needed.
Data Sorting: Enables sorting data by a selected column, making it easier to analyze and compare values.
Data Visualization
Bar Charts: Used to present the distribution of categorical data.
Pie Charts: Used to present the percentage shares of different categories.
Advanced Charts (Pairplot): Used to visualize relationships between multiple numerical variables simultaneously.
Programming Solutions
Object-Oriented Programming: The application is built using classes, which enhances code organization, reusability, and maintainability.
Design Patterns: The project uses design patterns to improve code readability, flexibility, and maintenance. For instance, the Observer pattern can be used to update views when data changes.
Summary
Data Analyzer is a comprehensive tool for exploring and visualizing data. By utilizing powerful Python libraries, it provides a user-friendly interface for performing various data analysis tasks. This project demonstrates the practical application of programming and data analysis techniques learned during the course.