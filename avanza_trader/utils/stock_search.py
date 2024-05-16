from utils.stock_data import save_stock_dict_to_json, load_stock_dict_from_json, search_stock_by_id, search_stock_by_name
from config import STOCKS_FILE
from utils.fetch_stocks import fetch_data

def search_stocks(session):
    fetch_data_input = input("Do you want to fetch new stock data? (y/n): ").strip().lower()
    if fetch_data_input == 'y':
        fetch_data(session, STOCKS_FILE)

    loaded_stock_dict = load_stock_dict_from_json(STOCKS_FILE)
    print(f"Total number of stocks: {len(loaded_stock_dict)}")

    while True:
        search_term = input('Type a name or ID (or "exit" to quit): ').strip()
        if search_term.lower() == "exit":
            break
        if search_term in loaded_stock_dict:
            found_name = search_stock_by_id(loaded_stock_dict, search_term)
            print(f"Found by ID {search_term}: {found_name}")
        else:
            found_id, found_name = search_stock_by_name(loaded_stock_dict, search_term)
            if found_name:
                print(f"Found by Name {search_term}: {found_id} - {found_name}")
            else:
                print(f"No match found for {search_term}")
