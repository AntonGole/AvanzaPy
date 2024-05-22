import json
from config import BASE_URL, HEADERS

def fetch_account_summary(session, security_token):
    url = f"{BASE_URL}/_api/account-performance/overview/total-values"
    payload = ["dcabfff", "dcabfgd", "geahecc"]
    headers = HEADERS.copy()
    headers["X-Securitytoken"] = security_token
    response = session.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()
        
        total_value = response_json.get('totalValue', {}).get('totalValue', {}).get('value')
        total_development = response_json.get('totalDevelopment', {})
        accounts_data = []

        accounts = response_json.get('accounts', [])
        for account in accounts:
            info = account.get('info', {})
            account_id = info.get('id')
            account_name = info.get('name')
            account_type = info.get('type')
            total_value = account.get('totalValue', {}).get('totalValue', {}).get('value')
            buying_power = account.get('buyingPower', {}).get('total', {}).get('value')

            account_data = {
                "id": account_id,
                "name": account_name,
                "account_type": account_type,
                "total_value": total_value,
                "buying_power": buying_power
            }
            accounts_data.append(account_data)
        
        return accounts_data, total_value, total_development
    else:
        print(f"Failed to get balance. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None, None, None