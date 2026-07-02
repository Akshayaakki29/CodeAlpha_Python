from colorama import Fore, Style, init
from tabulate import tabulate
init(autoreset=True)
print(Fore.MAGENTA + "=" * 55)
print(Fore.YELLOW + "      📈 STOCK PORTFOLIO TRACKER 📈")
print(Fore.MAGENTA + "=" * 55)
stocks = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2900,
    "WIPRO": 270,
    "HDFC": 1800
}
portfolio = []
total = 0
while True:
    stock = input(Fore.CYAN + "\nEnter Stock Name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stocks:
        quantity = int(input("Enter Quantity: "))
        value = stocks[stock] * quantity
        total += value
        portfolio.append([stock, quantity, stocks[stock], value])
    else:
        print(Fore.RED + "Stock not found!")
print("\n")
print(Fore.GREEN + tabulate(portfolio,
      headers=["Stock", "Qty", "Price", "Total"],
      tablefmt="grid"))
print(Fore.YELLOW + "\nTotal Investment Value = ₹", total)