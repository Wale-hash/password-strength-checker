import re

def check_password_strength(password: str) -> str:
    """Check the strength of a given password."""

    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many conditions failed
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    # Strength levels
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    print(f"Password Strength: {check_password_strength(pwd)}")
