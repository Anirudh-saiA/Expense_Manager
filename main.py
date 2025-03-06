import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_data, get_description
import matplotlib.pyplot as plt  # FIXED IMPORT

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": float(amount),  # Ensure amount is numeric
            "category": category.strip().capitalize(),  # Standardize category format
            "description": description.strip(),
        }

        file_is_empty = False
        try:
            with open(cls.CSV_FILE, "r") as csvfile:
                file_is_empty = csvfile.read().strip() == ""
        except FileNotFoundError:
            pass  # File will be created when opened in append mode

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            if file_is_empty:
                writer.writeheader()
            writer.writerow(new_entry)

        print("Entry added successfully!")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        try:
            df = pd.read_csv(cls.CSV_FILE)

            if df.empty:
                print("No transactions available.")
                return None

            # Convert "date" column to datetime format
            df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT, errors='coerce')

            # Ensure "amount" column is numeric (handle commas and spaces)
            df["amount"] = pd.to_numeric(df["amount"].astype(str).str.replace(",", "").str.strip(), errors="coerce")

            # Standardize "category" column (strip spaces, capitalize)
            df["category"] = df["category"].astype(str).str.strip().str.capitalize()

            # Debugging: Print unique categories to check formatting
            print("Unique categories in the dataset:", df["category"].unique())

            # Convert input start_date and end_date to datetime
            start_date = datetime.strptime(start_date, cls.FORMAT)
            end_date = datetime.strptime(end_date, cls.FORMAT)

            # Filter data within the date range
            mask = (df["date"] >= start_date) & (df["date"] <= end_date)
            filtered_df = df.loc[mask]

            if filtered_df.empty:
                print(f"No transactions found between {start_date.strftime(cls.FORMAT)} and {end_date.strftime(cls.FORMAT)}.")
                return None

            # Debugging: Print filtered transactions
            print("\n--- Filtered Transactions ---")
            print(filtered_df.to_string(index=False))

            # Fix category name capitalization
            filtered_df["category"] = filtered_df["category"].str.capitalize()

            # Calculate summary (handling lowercase category names)
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            # Print summary
            print("\n--- Summary ---")
            print(f"Total Income: ₹{total_income:.2f}")
            print(f"Total Expense: ₹{total_expense:.2f}")
            print(f"Net Savings: ₹{(total_income - total_expense):.2f}")

            return filtered_df

        except FileNotFoundError:
            print("No transactions found. CSV file does not exist.")
            return None

def add():
    CSV.initialize_csv()
    date = get_data("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    if df is None or df.empty:
        print("No data available for plotting.")
        return

    df["date"] = pd.to_datetime(df["date"])  # Convert to datetime
    df.set_index("date", inplace=True)  # Set index for resampling

    # Resample data by day and fill missing values with 0
    income_df = df[df["category"] == "Income"].resample("D").sum().fillna(0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().fillna(0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g", marker="o")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r", marker="o")

    plt.xlabel("Date")  # FIXED LABEL SPELLING
    plt.ylabel("Amount")  # FIXED LABEL SPELLING
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_data("Enter the start date (dd-mm-yyyy): ")
            end_date = get_data("Enter the end date (dd-mm-yyyy): ")   
            df = CSV.get_transactions(start_date, end_date)
            if df is not None and not df.empty:
                if input("Do you want to see a plot? (y/n) ").lower() == "y":
                    plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
