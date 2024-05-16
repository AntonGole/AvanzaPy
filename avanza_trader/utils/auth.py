import pyotp
from config import PERSISTENCE_COOKIE, BASE_URL, HEADERS

def generate_totp_code(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def send_login_request(session, username, password):
    login_url = f"{BASE_URL}/_api/authentication/sessions/usercredentials"
    payload = {"username": username, "password": password}
    headers = HEADERS.copy()
    headers["Cookie"] = PERSISTENCE_COOKIE
    response = session.post(login_url, json=payload, headers=headers)
    return response

def send_totp_request(session, transaction_id, totp_code):
    totp_url = f"{BASE_URL}/_api/authentication/sessions/totp"
    payload = {"totpCode": totp_code, "method": "TOTP"}
    headers = HEADERS.copy()
    headers["Cookie"] = f"{PERSISTENCE_COOKIE}; AZAMFATRANSACTION={transaction_id}"
    response = session.post(totp_url, json=payload, headers=headers)
    return response