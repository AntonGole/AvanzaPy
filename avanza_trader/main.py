from getpass import getpass
from utils.session import create_session
from utils.balance import get_balance
from utils.order import make_order
from utils.auth import  send_login_request, send_totp_request, generate_totp_code
from config import SECRET

def main():
    session = create_session()
    
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
            security_token = session.cookies.get('AZACSRF')
            
            # Fetch balance
            get_balance(session, security_token)
            
            # Place an order
            #make_order(
            #    session,
            #    security_token,
            #    orderbook_id="878733",
            #    account_id="6407422",
            #    amount="1",
            #    orderbook_name="Avanza Global"
            #)
        else:
            print("TOTP authentication failed.")
    else:
        print("Initial login failed.")

if __name__ == "__main__":
    main()
