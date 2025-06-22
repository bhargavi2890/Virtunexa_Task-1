import logging
import sqlite3

# -----------------------
# Set up Logging
# -----------------------
logging.basicConfig(
    filename='calc_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# -----------------------
# Set up SQLite Database
# -----------------------
conn = sqlite3.connect('history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history (operation TEXT, result TEXT)''')

# -----------------------
# Calculator Functions
# -----------------------
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# -----------------------
# Main Calculator Logic
# -----------------------
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting...")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform operation
        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'
        else:
            print("Invalid choice")
            continue

        print("Result:", result)

        # Convert result to string in case of division by zero error
        result_str = str(result)

        # Log to file
        logging.info(f"{num1} {op} {num2} = {result_str}")

        # Save to database
        c.execute("INSERT INTO history VALUES (?, ?)", (f"{num1} {op} {num2}", result_str))
        conn.commit()

# Run the calculator
calculator()

# Close DB connection
conn.close()
