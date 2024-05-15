import json
from config import BASE_URL, HEADERS

def get_balance(session, security_token):
    url = f"{BASE_URL}/_api/account-performance/overview/total-values"
    payload = ["dcabfff", "dcabfgd", "geahecc"]
    headers = HEADERS.copy()
    headers["X-Securitytoken"] = security_token
    response = session.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_json = response.json()
        total_value = response_json.get('totalValue', {}).get('totalValue', {}).get('value')
        if total_value is not None:
            print(f"Total Value: {total_value} SEK")
        else:
            print("Total value not found in the response.")
    else:
        print(f"Failed to get balance. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    return response
