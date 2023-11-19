import pandas as pd
import datetime
import tkinter as tk
from tkinter import filedialog

def convert_date_to_unix(date_str):
    """Converts a date string in the format 'YYYY-MM-DD HH:MM:SS' to a Unix timestamp."""
    dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    unix_timestamp = int(dt.timestamp()) * 1000  # Convert to milliseconds
    return unix_timestamp

def binance_to_pine_script(csv_file_path):
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Start of the PINE script
    pine_script = [
        "// Auto-generated PINE Script",
        "// Conversion of Binance Trade History",
        "@version=4",
        "strategy(\"Converted Binance Trades\", overlay=true, initial_capital=10000.0, commission_type=strategy.commission.percent, commission_value=0.2)",
        ""
    ]

    # Iterate over each row and create PINE script lines
    for index, row in data.iterrows():
        # Convert date to Unix timestamp
        timestamp = convert_date_to_unix(row['Date(UTC)'])

        # Determine the operation type (buy or sell)
        operation = 1 if row['Side'] == 'BUY' else 0

        # Create the strategy order and close lines
        order_line = f"strategy.order(\"{index}\", {operation}, {row['Quantity']}, {row['Price']}, when = time_close == {timestamp})"
        close_line = f"strategy.close(\"{index}\", when = time_close == {timestamp + 10000})"  # Placeholder for close time

        # Add lines to the script
        pine_script.append(order_line)
        pine_script.append(close_line)
        pine_script.append("")

    return "\n".join(pine_script)

# GUI for file selection
root = tk.Tk()
root.withdraw()  # Hides the small tkinter window

# Open file dialog and get the file path
file_path = filedialog.askopenfilename(title="Select Binance Export CSV File", filetypes=[("CSV files", "*.csv")])
if file_path:
    pine_script_content = binance_to_pine_script(file_path)
    print(pine_script_content)  # Or save this content to a file as needed
else:
    print("No file selected.")
