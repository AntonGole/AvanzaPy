# Avanza Trader

A Python project for automated stock trading using the unofficial Avanza API.

## Setup

1. **Clone the repository**:
    ```
    git clone https://github.com/AntonGole/avanza_trader.git
    cd avanza_trader
    ```

2. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Configuration**:
    - Ensure the `SESSION_FILE` and `STOCKS_FILE` paths in `config.py` are correct.
    - Make sure to get your TOTP Secret as described below.

## Getting Your TOTP Secret

1. **Navigate to Avanza Settings**:
    - Go to [Avanza - Profile Settings](https://www.avanza.se/min-profil/installningar/sajtinstallningar.html/inloggning/anvandarnamn) or manually:
    - Follow the steps: **Profil** -> **Inställningar** -> **Sajtinställningar** -> **Inloggning och utloggning** -> **Användarnamn** -> **Tvåfaktorsinloggning**
    - If you have already set up two-factor authentication, select **Återaktivera tvåfaktorsinloggning**
    - Then select **Aktivera** -> **Annan app för tvåfaktorsinloggning**
    - Click on **Kan du inte skanna QR-koden?** to reveal the TOTP Secret.

2. **Set the TOTP Secret in `config.py`**:
    - Copy the revealed TOTP Secret and paste it into `config.py`:
    ```
    SECRET = 'your_totp_secret_here'
    ```

3. **Generate a TOTP Code Manually**:
    - Run the `generate_code.py` script to generate a TOTP code:
    ```
    python utils/generate_code.py
    ```
    - This script will print the current TOTP code using the provided TOTP Secret.


## Running the Application

1. **Run the application**:
    ```
    python main.py
    ```

2. **Follow the interactive prompts**:
    - **Print Accounts**: Displays information about your accounts.
    - **Print Total Value**: Shows the total value of your portfolio.
    - **Print Total Development**: Displays the total development of your portfolio over time.
    - **Search Stocks**: Allows you to search for stocks by ID or name.
    - **Buy a Stock**: Prompts you to enter a stock ID or name to see the stock details.
    - **Exit**: Exits the application.

## Project Structure

- `main.py`: Entry point of the application with the interactive menu.
- `config.py`: Configuration file containing API URLs, headers, and file paths.
- `session/`: Contains session management utilities.
    - `session_utils.py`: Functions for creating, saving, and loading sessions.
- `utils/`: Utility modules for various functionalities.
    - `fetch_accounts.py`: Functions to fetch account information.
    - `fetch_stocks.py`: Functions to fetch stock information.
    - `stock_data.py`: Functions to save and load stock data.
    - `stock_search.py`: Function for searching stocks.
    - `print_utils.py`: Functions for showing account info, total value, and development information.
    - `auth.py`: Functions for handling authentication.
    - `order.py`: Functions to place orders.
- `data/`: Directory for storing JSON data files (e.g., `stocks.json`).

## Usage

1. **Initialize the session**:
    - If a valid session is found in the `session.json` file, it will be loaded.
    - If no valid session is found, you will be prompted to log in.

2. **Interactive Menu**:
    - The main script provides an interactive menu for different actions such as printing account details, checking total value, printing total development, searching for stocks, and viewing stock details for potential purchase.

## Example

```
$ python main.py
Loading session from file...
Session loaded.

Select an option:
1. Print Accounts
2. Print Total Value
3. Print Total Development
4. Search Stocks
5. Buy a Stock
6. Exit
Enter your choice (1-6):
```

Select an option by entering the corresponding number and follow the prompts to perform actions.

## Note

This project uses an unofficial API, and usage may be subject to change. Ensure you comply with Avanza's terms of service.
