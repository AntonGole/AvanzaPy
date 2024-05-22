from bs4 import BeautifulSoup
import re
from config import BASE_URL, FETCH_HEADERS, FETCH_PARAMS
from utils.stock_data import save_stock_dict_to_json

def fetch_total_hits(session):
    url = f"{BASE_URL}/frontend/template.html/marketing/advanced-filter/advanced-filter-template"
    response = session.get(url, params=FETCH_PARAMS, headers=FETCH_HEADERS)

    if response.status_code == 200:
        print("Successfully fetched total hits data.")
        soup = BeautifulSoup(response.text, 'html.parser')
        table_container = soup.find('div', {'class': 'tableScrollContainer'})
        if table_container:
            table = table_container.find('table', {'class': 'u-standardTable'})
            if table:
                data_aza_save = table.get('data-aza-save', '')
                match = re.search(r'vm\.totalNumberOfHits=(\d+)', data_aza_save)
                if match:
                    total_hits = int(match.group(1))
                    return total_hits
                else:
                    print("Failed to extract totalNumberOfHits from data-aza-save attribute.")
                    return None
            else:
                print("Failed to find the table element in the response.")
                return None
        else:
            print("Failed to find the tableScrollContainer in the response.")
            return None
    else:
        print(f"Failed to fetch total hits. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None

def fetch_stocks(session, total_hits):
    stocks = {}
    batch_size = 200
    for start_index in range(0, total_hits, batch_size):
        params = FETCH_PARAMS.copy()
        params["parameters.startIndex"] = str(start_index)
        params["parameters.maxResults"] = str(batch_size)
        
        url = f"{BASE_URL}/frontend/template.html/marketing/advanced-filter/advanced-filter-template"
        response = session.get(url, params=params, headers=FETCH_HEADERS)

        if response.status_code == 200:
            print(f"Successfully fetched batch starting at index {start_index}.")
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', {'class': 'u-standardTable'})
            if table:
                rows = table.find_all('tr', {'class': 'row'})
                for row in rows:
                    name_tag = row.find('a', {'class': 'ellipsis'})
                    if name_tag:
                        stock_name = name_tag.text.strip()
                        buy_button = row.find('a', {'class': 'buyBtn'})
                        if buy_button and 'href' in buy_button.attrs:
                            href = buy_button['href']
                            order_id = href.split('/kop/')[-1]
                            stocks[order_id] = stock_name
        else:
            print(f"Failed to fetch stocks for batch starting at index {start_index}. Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            return None
    return stocks

def fetch_data(session, filename):
    total_hits = fetch_total_hits(session)
    if total_hits:
        print(f"Total hits: {total_hits}")
        stock_dict = fetch_stocks(session, total_hits)
        if stock_dict:
            print(f"Total number of stocks: {len(stock_dict)}")
            print("First 100 Stock Names and IDs:")
            for stock_id, stock_name in list(stock_dict.items())[:100]:
                print(f"{stock_id}: {stock_name}")
            save_stock_dict_to_json(stock_dict, filename)
            print(f"Stock data saved to {filename}")
