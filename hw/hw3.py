"""
Charlie Tran
COSC 1306
Homework #3
"""

list = ["AAPL.csv", "AMZN.csv", "GOOG.csv", "MSFT.csv", "TSLA.csv"]


def get_stock_info():
    stock_prices = []  # Create a list for stock prices
    # loop over all the index values that contain stock data
    for index in range(1, len(data)):
        stock_info = data[index].split(",")  # Split the string into pieces
        stock_prices.append([stock_info[0], float(stock_info[2]), float(
            stock_info[3])])  # Extract the data, high, and low prices

    best_profit = 0  # Start with zero profit as the lowest acceptable value
    purchase_date = ""
    purchase_date_price = 0
    sell_date = ""
    sell_date_price = 0

    for buy in range(len(stock_prices)-1):  # Try out buying on each day
        for sell in range(buy+1, len(stock_prices)):  # Try selling on each subsequent day
            profit = stock_prices[sell][1] - \
                stock_prices[buy][2]  # Compute the profit
            if profit > best_profit:  # If the profit is better than the best
                best_profit = profit  # make it the new best
                purchase_date = stock_prices[buy][0]
                purchase_date_price = stock_prices[buy][2]
                sell_date = stock_prices[sell][0]
                sell_date_price = stock_prices[sell][1]

    purchase_date_price = round(purchase_date_price, 2)
    sell_date_price = round(sell_date_price, 2)
    best_profit = round(best_profit, 2)
    value_ratio = round(sell_date_price / purchase_date_price, 3)

    print()
    print("Reading data ...")
    print("****************************************")
    print("The maximum profit is", best_profit,
          "per share")  # Check the final results
    print()
    print("Buy on", purchase_date, "at the price of", purchase_date_price)
    print("Sell on", sell_date, "at the price of", sell_date_price)
    print()
    print("Change in value ratio is", value_ratio)
    print("****************************************")
    print()


while True:
    data = []

    file_name = input("Please enter the data file name: ")

    if file_name not in list:
        print()
        print("Reading data ...")
        print("The file does not exist. Please check the name and try again.")
    if file_name in list:
        with open(file_name, "r") as file:  # Open the file for reading
            for line in file.readlines():   # Extract all the lines and loop through one at a time
                # Remove the new line character at the end of each line
                data.append(line.strip())
        get_stock_info()
    if file_name == "":
        print("Thank you and Good Bye!")
        break
