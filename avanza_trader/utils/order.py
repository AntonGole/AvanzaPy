from config import BASE_URL, HEADERS

def make_fund_order(session, security_token, orderbook_id, account_id, amount, orderbook_name):
    url = f"{BASE_URL}/_api/fund-guide/fund-order-page/buy"
    payload = {
        "orderbookId": orderbook_id,
        "accountId": account_id,
        "amount": amount,
        "orderbookName": orderbook_name
    }
    headers = HEADERS.copy()
    headers["X-Securitytoken"] = security_token
    response = session.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_json = response.json()
        if response_json.get("orderRequestStatus") == "SUCCESS":
            print(f"Order successful: Order ID {response_json.get('orderId')}")
        else:
            print(f"Order failed: {response_json.get('message')}")
    else:
        print(f"Failed to make order. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    return response

import uuid

def make_stock_order(session, security_token, orderbook_id, account_id, price, volume, side="BUY"):
    url = f"{BASE_URL}/_api/trading-critical/rest/order/new"
    payload = {
        "isDividendReinvestment": False,
        "requestId": str(uuid.uuid4()),  # Generate a unique requestId
        "orderRequestParameters": None,
        "price": price,
        "volume": volume,
        "openVolume": None,
        "accountId": account_id,
        "side": side,
        "orderbookId": orderbook_id,
        "validUntil": None,
        "condition": "NORMAL",
        "metadata": {
            "orderEntryMode": "STANDARD",
            "hasTouchedPrice": "false"
        }
    }
    headers = HEADERS.copy()
    headers["X-Securitytoken"] = security_token
    response = session.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_json = response.json()
        if response_json.get("orderRequestStatus") == "SUCCESS":
            print(f"Order successful: Order ID {response_json.get('orderId')}")
        else:
            print(f"Order failed: {response_json.get('message')}")
    else:
        print(f"Failed to make order. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    return response
