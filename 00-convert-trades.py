import pandas as pd
import datetime
import os
import sys
import tkinter as tk
from tkinter import filedialog

def convert_date_to_unix(date_str):
    """
    Converts a date string in the format 'YYYY-MM-DD HH:MM:SS' to a Unix timestamp.
    
    Parameters:
    date_str (str): The date string to convert.
    
    Returns:
    int: The Unix timestamp in milliseconds.
    """
    dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    unix_timestamp = int(dt.timestamp()) * 1000  # Convert to milliseconds
    return unix_timestamp

def binance_to_pine_script(csv_file_path):
    """
    Reads a Binance trade history CSV file and converts it into a PINE script format.
    
    Parameters:
    csv_file_path (str): Path to the Binance CSV file.
    
    Returns:
    str: The generated PINE script as a string.
    """
    data = pd.read_csv(csv_file_path)

    pine_script = [
        "// Auto-generated PINE Script",
        "// Conversion of Binance Trade History",
        "@version=4",
        "strategy(\"Converted Binance Trades\", overlay=true, initial_capital=10000.0, commission_type=strategy.commission.percent, commission_value=0.2)",
        ""
    ]

    for index, row in data.iterrows():
        timestamp = convert_date_to_unix(row['Date(UTC)'])
        operation = 1 if row['Side'] == 'BUY' else 0
        order_line = f"strategy.order(\"{index}\", {operation}, {row['Quantity']}, {row['Price']}, when = time_close == {timestamp})"
        close_line = f"strategy.close(\"{index}\", when = time_close == {timestamp + 10000})"
        pine_script.append(order_line)
        pine_script.append(close_line)
        pine_script.append("")

    return "\n".join(pine_script)

def main():
    """
    Main function to execute the script.
    """
    if sys.platform.startswith('darwin') or sys.platform.startswith('win'):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select Binance Export CSV File", filetypes=[("CSV files", "*.csv")])
    else:
        file_path = input("Enter the path to your Binance export CSV file: ")

    if file_path:
        pine_script_content = binance_to_pine_script(file_path)
        output_file_path = os.path.splitext(file_path)[0] + "_PINEScript.txt"
        
        with open(output_file_path, 'w') as file:
            file.write(pine_script_content)

        print(f"PINE script saved to {output_file_path}")
    else:
        print("No file selected or provided.")

if __name__ == "__main__":
    main()
