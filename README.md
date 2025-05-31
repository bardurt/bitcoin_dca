# Bitcoin DCA Simulation

A Python script that simulates a Bitcoin Dollar Cost Averaging (DCA) investment strategy using historical weekly closing prices. This tool helps visualize how consistent, periodic investments in Bitcoin could have performed over time.

## Overview

This project allows you to:

- Simulate weekly Bitcoin investments over a specified time frame.
- Analyze portfolio performance using forward (historical to present) and backward (present to historical) DCA strategies.
- Visualize total invested amounts, portfolio value, and net gains or losses over time.

## Repository Contents

- `bitcoin.py`: Main script containing functions to perform DCA simulations.
- `btc_price_weekly.csv`: Dataset with historical weekly Bitcoin prices.
- `requirements.txt`: List of Python dependencies required to run the script.
- `README.md`: Project documentation.

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone https://github.com/bardurt/bitcoin_dca.git
   cd bitcoin_dca
   ```

2. **Install the required dependencies:**
   
    ```
    pip install -r requirements.txt
    ```

3. **Run the simulation:**

    ```
    python bitcoin.py [-r] [-usd <amount>]
    ```

    -r — Use reverse simulation (start from present, accumulate backward).

    -usd <amount> — Weekly investment amount (default is 50).

Each run generates a line chart comparing:

- Portfolio Value (in USD)

- Total Invested amount

- Net Gain/Loss over time
    
