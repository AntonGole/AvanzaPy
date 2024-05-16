from utils.order import make_fund_order, make_stock_order
from utils.print_utils import print_accounts, print_total_value, print_total_development
from session.session_utils import initialize_session
from utils.stock_search import search_stocks
from utils.stock_data import search_stock_by_id, search_stock_by_name, load_stock_dict_from_json
from config import STOCKS_FILE

def main():
    session, security_token = initialize_session()
    if not session or not security_token:
        print("Failed to initialize session.")
        return

    while True:
        print("\nSelect an option:")
        print("1. Print Accounts")
        print("2. Print Total Value")
        print("3. Print Total Development")
        print("4. Search Stocks")
        print("5. Buy a Stock")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print_accounts(session, security_token)
        elif choice == "2":
            print_total_value(session, security_token)
        elif choice == "3":
            print_total_development(session, security_token)
        elif choice == "4":
            search_stocks(session)
        elif choice == "5":
            buy_stock(session)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def buy_stock(session):
    search_term = input("Enter the stock ID or name to buy: ").strip()
    stock_dict = load_stock_dict_from_json(STOCKS_FILE)

    if search_term in stock_dict:
        stock_name = search_stock_by_id(stock_dict, search_term)
        print(f"Found Stock - ID: {search_term}, Name: {stock_name}")
    else:
        stock_id, stock_name = search_stock_by_name(stock_dict, search_term)
        if stock_name:
            print(f"Found Stock - ID: {stock_id}, Name: {stock_name}")
        else:
            print(f"No match found for {search_term}")

if __name__ == "__main__":
    main()
