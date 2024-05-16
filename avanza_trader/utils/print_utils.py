from utils.fetch_accounts import fetch_account_summary

def print_accounts(session, security_token):
    accounts, _, _ = fetch_account_summary(session, security_token)
    if accounts is not None:
        for account in accounts:
            print("\n" + "-"*40)
            print(f"Account ID: {account['id']}")
            print(f"Name: {account['name']}")
            print(f"Account Type: {account['account_type']}")
            print(f"Total Value: {account['total_value']} SEK")
            print(f"Buying Power: {account['buying_power']} SEK")
            print("-"*40 + "\n")

def print_total_value(session, security_token):
    _, total_value, _ = fetch_account_summary(session, security_token)
    if total_value is not None:
        print(f"\nTotal Value: {total_value} SEK\n")

def print_total_development(session, security_token):
    _, _, total_development = fetch_account_summary(session, security_token)
    if total_development is not None:
        print("Total Development:")
        for period, development in total_development.items():
            absolute_value = development.get('absolute', {}).get('value')
            relative_value = development.get('relative', {}).get('value')
            print(f"  {period}:")
            print(f"    Absolute Value = {absolute_value} SEK")
            print(f"    Relative Value = {relative_value}%")
            print()
