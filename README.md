# check-pnl-future

![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
![Binance](https://img.shields.io/badge/Binance-0.7.9-orange)
![Rich](https://img.shields.io/badge/Rich-10.2.2-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Binance Check PNL Future per coin from last 30 days , is a Python script that interacts with the Binance API to fetch and display information about cryptocurrency trades.

## Features

- Fetches recent trades from Binance
- Supports a list of symbols as input, either as a comma-separated string or from a file
- Option to use the most recently traded symbol
- Displays a graph of the income for each symbol

## Requirements

- Binance API key and secret (you can edit in code)
- Libraries: binance, rich, matplotlib, argparse, os
  
```bash
pip install binance-python rich matplotlib argparse
```

## Usage

```bash
python3 checkcoin.py -i SYMBOLS
```

Where SYMBOLS is a comma-separated list of symbols or a path to a file containing a comma-separated list of symbols.

Options
--log: Show log
--recent: Use the most recent traded symbol
--graph: Display a graph of the income for each symbol

Example
```bash
python3 checkcoin-custom.py -i BTC,ADA
```
or
```bash
python3 checkcoin-custom.py -i symbols.txt
```
Where symbols.txt is a file containing BTC,ADA.

## Disclaimer
This script uses the Binance API. Please ensure that your API key and secret are correct and have the necessary permissions. Also, ensure that your system time is correct, as the Binance API requires the timestamp in each request to be within a certain range of the current time.
