# check-pnl-future
![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
![Binance](https://img.shields.io/badge/Binance-0.7.9-orange)
![Rich](https://img.shields.io/badge/Rich-10.2.2-green)
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
