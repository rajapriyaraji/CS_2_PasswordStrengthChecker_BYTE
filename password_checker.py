import re

def check_password_strength(password):
    score = 0
    reasons = []

    if len(password) >= 8:
        score += 1
        reasons.append("Good length")
    else:
        reasons.append("Password should contain at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
        reasons.append("Contains uppercase letter")
    else:
        reasons.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
        reasons.append("Contains lowercase letter")
    else:
        reasons.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
        reasons.append("Contains a number")
    else:
        reasons.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        reasons.append("Contains special character")
    else:
        reasons.append("Add at least one special character")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    print("\nPassword Strength:", strength)

    print("\nAnalysis:")
    for reason in reasons:
        print("-", reason)


password = input("Enter your password: ")
check_password_strength(password)