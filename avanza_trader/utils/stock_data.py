import json

def save_stock_dict_to_json(stock_dict, filename):
    with open(filename, 'w') as f:
        json.dump(stock_dict, f, indent=4)

def load_stock_dict_from_json(filename):
    with open(filename, 'r') as f:
        stock_dict = json.load(f)
    return stock_dict

def search_stock_by_id(stock_dict, stock_id):
    return stock_dict.get(stock_id)

def search_stock_by_name(stock_dict, stock_name):
    for id, name in stock_dict.items():
        if name.lower() == stock_name.lower():
            return id, name
    return None, None