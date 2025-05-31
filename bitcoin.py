import pandas as pd
import matplotlib.pyplot as plt
import sys


# Simulate accumulation from a point in the past up untill today
def simulate_forward(df, weekly_investment_usd):
    total_rows = len(df)
    results = []

    for run in range(1, total_rows + 1):
        subset = df.iloc[-run:] 

        btc_accumulated = 0
        total_invested_usd = 0

        for _, row in subset.iterrows():
            btc_accumulated += weekly_investment_usd / row['close']
            total_invested_usd += weekly_investment_usd

        valuation_price = subset.iloc[0]['close']
        valuation_date = subset.iloc[0]['timeClose']

        portfolio_value = btc_accumulated * valuation_price
        net_gain_loss = portfolio_value - total_invested_usd

        results.append({
            'Date': valuation_date,
            'Total Invested': total_invested_usd,
            'BTC Accumulated': btc_accumulated,
            'Valuation Price': valuation_price,
            'Portfolio Value': portfolio_value,
            'Net Gain/Loss': net_gain_loss
        })

    results_df = pd.DataFrame(results)
    results_df['Date'] = pd.to_datetime(results_df['Date'])
    results_df = results_df.sort_values('Date')

    plt.figure(figsize=(12, 6))
    plt.plot(results_df['Date'], results_df['Portfolio Value'], label='Forward: Portfolio Value', linewidth=2)
    plt.plot(results_df['Date'], results_df['Total Invested'], label='Forward: Total Invested', linestyle='--')
    plt.plot(results_df['Date'], results_df['Net Gain/Loss'], label='Forward: Net Gain/Loss', linestyle=':')
    plt.xlabel('Date')
    plt.ylabel('USD')
    plt.title(f'BTC DCA Simulation – Forward (${weekly_investment_usd}/week)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Simulate accumulation from a today (latest day in the data set) and go back in time
def simulate_reverse(df, weekly_investment_usd):
    total_rows = len(df)
    results = []

    # We use the most recent entry as the current price
    # data is in descending date order
    valuation_price = df.iloc[0]['close']
    valuation_date = df.iloc[0]['timeClose']

    for run in range(1, total_rows + 1):
        subset = df.iloc[:run] 

        btc_accumulated = 0
        total_invested_usd = 0

        for _, row in subset.iterrows():
            btc_accumulated += weekly_investment_usd / row['close']
            total_invested_usd += weekly_investment_usd

        portfolio_value = btc_accumulated * valuation_price
        net_gain_loss = portfolio_value - total_invested_usd

        results.append({
            'Date': subset.iloc[-1]['timeClose'], 
            'Total Invested': total_invested_usd,
            'BTC Accumulated': btc_accumulated,
            'Valuation Price': valuation_price,
            'Portfolio Value': portfolio_value,
            'Net Gain/Loss': net_gain_loss
        })

    results_df = pd.DataFrame(results)
    results_df['Date'] = pd.to_datetime(results_df['Date'])
    results_df = results_df.sort_values('Date')

    plt.figure(figsize=(12, 6))
    plt.plot(results_df['Date'], results_df['Portfolio Value'], label='Reverse: Portfolio Value', linewidth=2)
    plt.plot(results_df['Date'], results_df['Total Invested'], label='Reverse: Total Invested', linestyle='--')
    plt.plot(results_df['Date'], results_df['Net Gain/Loss'], label='Reverse: Net Gain/Loss', linestyle=':')
    plt.xlabel('Date')
    plt.ylabel('USD')
    plt.title(f'BTC DCA Simulation – Reverse (${weekly_investment_usd}/week)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def parse_args(args):
    reverse = '-r' in args
    usd = 50

    if '-usd' in args:
        try:
            usd_index = args.index('-usd')
            usd = float(args[usd_index + 1])
        except (IndexError, ValueError):
            print("Invalid usage of -usd. Example: -usd 25")
            sys.exit(1)

    return reverse, usd

if __name__ == "__main__":
    df = pd.read_csv('btc_price_weekly.csv', sep=';')

    reverse, weekly_investment_usd = parse_args(sys.argv)

    print(f"Weekly investment amount: ${weekly_investment_usd:.2f}")
    if reverse:
        print("Running reverse simulation...\n")
        simulate_reverse(df, weekly_investment_usd)
    else:
        print("Running forward simulation...\n")
        simulate_forward(df, weekly_investment_usd)
