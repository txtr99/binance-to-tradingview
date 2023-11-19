# Binance to PINE Script Converter

## Description
This Python script converts Binance trade history, exported as a CSV file, into PINE script format. It's designed for traders who wish to analyze their Binance trades using TradingView's PINE script.  It was created entirely with ChatGPT-4 and is not a robust framework, rather it's just a snippet and was only tested on MacOS.

## Features
- Converts Binance trade history CSV files to PINE script.
- Compatible with macOS and Windows for GUI-based file selection.
- Command-line file path input support for other operating systems.

## Requirements
- Python 3
- Pandas library
- Tkinter library (usually included with Python)

## Usage
Run the script using Python. On macOS and Windows, a file dialog will appear for selecting the CSV file. On other operating systems, you'll be prompted to enter the file path in the console.

Ensure the CSV file contains only 1 symbol before running the script. Also it's design for FUTURES TRADES export.

## Installation
1. Clone the repo, and cd into the directory
2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```
3. Install dependencies
```bash
pip install -r req.txt
```
4. Run the script
```bash
python 00-convert-trades.py
