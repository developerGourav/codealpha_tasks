import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stock data {symbol: {'shares': int, 'avg_cost': float}}

    def add_stock(self, symbol, shares, cost_per_share):
        """Adds a stock or updates existing holding."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            # Update existing stock (calculate new average cost)
            total_shares = self.portfolio[symbol]['shares'] + shares
            total_cost = (self.portfolio[symbol]['shares'] * self.portfolio[symbol]['avg_cost']) + (shares * cost_per_share)
            self.portfolio[symbol]['shares'] = total_shares
            self.portfolio[symbol]['avg_cost'] = total_cost / total_shares
        else:
            # Add new stock
            self.portfolio[symbol] = {'shares': shares, 'avg_cost': cost_per_share}
        print(f"Added {shares} shares of {symbol} at ${cost_per_share:.2f} per share.")

    def remove_stock(self, symbol, shares):
        """Removes shares from a stock holding."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                self.portfolio[symbol]['shares'] -= shares
                print(f"Removed {shares} shares of {symbol}. Remaining: {self.portfolio[symbol]['shares']}")
        else:
            print(f"Error: {symbol} not found in portfolio.")

    def show_portfolio(self):
        """Displays the current portfolio with real-time data."""
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        print("\n--- Current Portfolio ---")
        total_investment = 0
        current_portfolio_value = 0

        # Create a list for display
        data = []

        for symbol, info in self.portfolio.items():
            shares = info['shares']
            avg_cost = info['avg_cost']
            
            # Fetch real-time price
            ticker = yf.Ticker(symbol)
            try:
                # fast_info is often faster than history for current price
                current_price = ticker.fast_info['last_price']
            except:
                print(f"Could not fetch data for {symbol}. Using buy price.")
                current_price = avg_cost

            current_value = shares * current_price
            investment_value = shares * avg_cost
            gain_loss = current_value - investment_value
            gain_loss_percent = (gain_loss / investment_value) * 100 if investment_value > 0 else 0

            total_investment += investment_value
            current_portfolio_value += current_value

            data.append([
                symbol, shares, f"${avg_cost:.2f}", f"${current_price:.2f}", 
                f"${current_value:.2f}", f"${gain_loss:.2f} ({gain_loss_percent:.2f}%)"
            ])

        # Display using pandas for a neat table
        df = pd.DataFrame(data, columns=["Symbol", "Shares", "Avg Cost", "Current Price", "Total Value", "Gain/Loss"])
        print(df.to_string(index=False))
        
        print("-" * 60)
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"Current Value:    ${current_portfolio_value:.2f}")
        print(f"Total Profit/Loss: ${current_portfolio_value - total_investment:.2f}")
        print("-" * 60)

def main():
    tracker = StockPortfolio()
    
    while True:
        print("\n--- Stock Portfolio Tracker Menu ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            symbol = input("Enter Stock Symbol (e.g., AAPL, GOOGL, TSLA): ")
            try:
                shares = int(input("Enter number of shares: "))
                price = float(input("Enter buy price per share: "))
                tracker.add_stock(symbol, shares, price)
            except ValueError:
                print("Invalid input. Please enter numbers for shares and price.")
        
        elif choice == '2':
            symbol = input("Enter Stock Symbol to remove: ")
            try:
                shares = int(input("Enter number of shares to remove: "))
                tracker.remove_stock(symbol, shares)
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            tracker.show_portfolio()

        elif choice == '4':
            print("Exiting Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()