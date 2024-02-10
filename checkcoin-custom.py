from binance.client import Client
from rich.progress import Progress
from rich import print
from rich.table import Table
from rich.console import Console
import datetime
import time
import matplotlib.pyplot as plt
import argparse
import os

##### edit here #####
api_key = ''
api_secret = ''

client = Client(api_key, api_secret)

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)

def read_symbols(value):
    if os.path.isfile(value):
        with open(value, 'r') as file:
            symbols = file.read().replace('\n', '').split(',')
    else:
        symbols = value.split(',')
    return [symbol.strip() for symbol in symbols]

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=read_symbols, help='Comma-separated list of symbols or path to a file containing symbols')
parser.add_argument('--log', help='show log', default=False, action='store_true')
parser.add_argument('--recent', action='store_true', help='Use the most recent traded symbol')
parser.add_argument('--graph', action='store_true', help='Display a graph of the income for each symbol')
args = parser.parse_args()

if args.recent:
    recent_trades = client.futures_account_trades()
    last_traded_symbol = recent_trades[0]['symbol']
    symbols = [last_traded_symbol]
else:
    symbols = args.i

symbols_income = {}
progress = Progress()
num_date_ranges = (end_date - start_date).days // 7 + 1
total_steps = len(symbols) * num_date_ranges

with progress:
    task = progress.add_task("[cyan]Processing symbols", total=total_steps)
    for symbol in symbols:
        if "USDT" not in symbol.upper():
            symbol += "USDT"
        coin_profit = 0.0
        coin_loss = 0.0

        current_date = start_date
        while current_date <= end_date:
            next_date = current_date + datetime.timedelta(days=7)
            if next_date > end_date:
                next_date = end_date

            start_timestamp_ms = int(datetime.datetime.timestamp(current_date) * 1000)
            end_timestamp_ms = int(datetime.datetime.timestamp(next_date) * 1000)

            if args.log:
                print(f"Fetching trades for {symbol} from {current_date} to {next_date}")
            trades = client.futures_account_trades(symbol=symbol, startTime=start_timestamp_ms, endTime=end_timestamp_ms)

            time.sleep(1)

            for trade in trades:
                pnl = float(trade['realizedPnl'])
                if pnl > 0:
                    coin_profit += pnl
                else:
                    coin_loss += pnl

            current_date = next_date + datetime.timedelta(seconds=1)
            progress.update(task, advance=1)

        coin_income = coin_profit + coin_loss
        symbols_income[symbol] = coin_income

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Symbol", style="dim", width=12)
table.add_column("Income", justify="right")

sorted_symbols_income = dict(sorted(symbols_income.items(), key=lambda item: item[1], reverse=True))

colors = ["yellow", "cyan"]

for index, (symbol, income) in enumerate(sorted_symbols_income.items()):
    symbol_color = colors[index % len(colors)]
    income_color = "green" if income >= 0 else "red"
    table.add_row(f"[{symbol_color}]{symbol}", f"[{income_color}]{income:.2f}")

console.print(table)

total_profit = sum([income for income in symbols_income.values() if income > 0])
total_loss = sum([income for income in symbols_income.values() if income < 0])
total_income = sum(symbols_income.values())

console.print(f"[yellow]Total Profit: {total_profit:.2f}")
console.print(f"[red]Total Loss: {total_loss:.2f}")
console.print(f"[magenta]Total Income: {total_income:.2f}")

if args.graph:
    plt.bar(sorted_symbols_income.keys(), sorted_symbols_income.values())
    plt.xlabel('Symbol')
    plt.ylabel('Income')
    plt.title('Income for each symbol')
    plt.savefig('income_graph.png')
    plt.show()
