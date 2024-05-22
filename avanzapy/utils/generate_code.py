import pyotp

SECRET = 'your_totp_secret_here'

def generate_totp_code(SECRET):
    totp = pyotp.TOTP(SECRET)
    current_code = totp.now()
    print("Your current TOTP code is:", current_code)
    return current_code

if __name__ == "__main__":
    generate_totp_code(SECRET)