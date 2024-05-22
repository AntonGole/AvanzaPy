import json
import os
import requests
from getpass import getpass
from config import SECRET
from utils.auth import send_login_request, send_totp_request, generate_totp_code
from config import SESSION_FILE, SESSION_EXPIRY_TIME
import time

def create_session():
    return requests.Session()

def save_session(session):
    with open(SESSION_FILE, 'w') as f:
        cookies = session.cookies.get_dict()
        json.dump(cookies, f)

def load_session(session):
    if not os.path.exists(SESSION_FILE):
        return False
    with open(SESSION_FILE, 'r') as f:
        cookies = json.load(f)
        session.cookies.update(cookies)
    return True

def get_file_modification_time(file_path):
    return os.path.getmtime(file_path)

def get_security_token(session):
    cookies = session.cookies
    for cookie in cookies:
        if cookie.name == 'AZACSRF':
            return cookie.value
    return None

def initialize_session():
    session = create_session()
    security_token = None

    # Check if session file exists and load it
    if os.path.exists(SESSION_FILE):
        print("Loading session from file...")
        session_loaded = load_session(session)
        if session_loaded:
            file_mod_time = get_file_modification_time(SESSION_FILE)
            current_time = time.time()
            if current_time - file_mod_time < SESSION_EXPIRY_TIME:
                print("Session loaded.")
                security_token = get_security_token(session)
            else:
                print("Session expired. Creating a new session.")

    if not security_token:
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")

        # Step 1: Initial login request
        login_response = send_login_request(session, username, password)
        if login_response.status_code == 200:
            login_data = login_response.json()
            transaction_id = login_data['twoFactorLogin']['transactionId']

            # Step 2: Generate TOTP code
            totp_code = generate_totp_code(SECRET)
            print("TOTP Code:", totp_code)

            # Step 3: Send TOTP request
            totp_response = send_totp_request(session, transaction_id, totp_code)
            if totp_response.status_code == 200:
                security_token = get_security_token(session)
                # Save the session to a file
                save_session(session)
                print("Session saved.")
            else:
                print("TOTP authentication failed.")
                return None, None
        else:
            print("Initial login failed.")
            return None, None

    return session, security_token