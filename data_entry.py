from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_data(prompt, allow_default=False):
    date_str = input(prompt)

    # Return today's date if default is allowed and input is empty
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return get_data(prompt, allow_default)  # Recursive call with return

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount ,ust be a non negative and non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
def get_category():
    category = input("Enter the category('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid catergory. Please enter 'I' for Income or 'E' for Expense.")


def get_description():
    return input("Enter the description(optional)")

