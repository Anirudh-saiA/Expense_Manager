# Expense_Manager
This is a Expense manager
A simple Expense Manager application built with Python, Pandas, and Matplotlib to track income and expenses over time. The application stores transactions in a CSV file and provides an option to visualize income vs. expenses using a graph.

Features

Add Transactions: Record income and expenses with date, amount, category, and description.

View Transactions: Filter transactions within a date range and view a summary.

Data Persistence: Transactions are stored in finance_data.csv.

Graphical Representation: Plot income and expense trends over time.

Automatic CSV Initialization: Creates finance_data.csv if not present.

Installation

Prerequisites

Ensure you have Python 3.x installed. Install the required dependencies using:

pip install pandas matplotlib
Usage

Clone the repository and navigate to the project directory:

git clone https://github.com/yourusername/expense-manager.git
cd expense-manager

Run the application:

python main.py

How It Works

Adding Transactions:

Enter the transaction date, amount, category (Income/Expense), and description.

Viewing Transactions:

Enter a date range to view filtered transactions and summary.

Optionally, display a graphical representation of income vs. expenses.

Exit the Application:

Choose option 3 to quit.

Example Menu

1. Add a new transaction
2. View transactions and summary within a date range
3. Exit
Enter your choice (1-3):

File Structure

📂 expense-manager
├── main.py  # Main application file
├── data_entry.py  # Functions for user input handling
├── finance_data.csv  # Stores transaction data
├── README.md  # Documentation

Future Enhancements

Category-wise Analysis: Breakdown of expenses by category.

Monthly Summaries: Aggregate transactions by month.

GUI Support: Develop a Tkinter or Flask-based interface.

License

This project is open-source and available under the MIT License.

Contributing

Feel free to fork the repo, submit pull requests, or suggest improvements!
