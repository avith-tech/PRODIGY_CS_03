import re


def assess_password_strength(password):
    # Initialize criteria
    criteria = {
        'length': len(password) >= 8,  # Length of at least 8 characters
        'uppercase': bool(re.search(r'[A-Z]', password)),  # At least one uppercase letter
        'lowercase': bool(re.search(r'[a-z]', password)),  # At least one lowercase letter
        'digit': bool(re.search(r'[0-9]', password)),  # At least one digit
        'special_char': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # At least one special character
    }

    # Calculate strength
    strength_score = sum(criteria.values())
    strength_feedback = []

    if criteria['length']:
        strength_feedback.append("Valid. Length is sufficient (8 characters or more).")
    else:
        strength_feedback.append("Invalid. Length should be at least 8 characters.")

    if criteria['uppercase']:
        strength_feedback.append("Valid. Contains at least one uppercase letter.")
    else:
        strength_feedback.append("Invalid. Should include at least one uppercase letter.")

    if criteria['lowercase']:
        strength_feedback.append("Valid. Contains at least one lowercase letter.")
    else:
        strength_feedback.append("Invalid. Should include at least one lowercase letter.")

    if criteria['digit']:
        strength_feedback.append("Valid. Contains at least one digit.")
    else:
        strength_feedback.append("Invalid. Should include at least one digit.")

    if criteria['special_char']:
        strength_feedback.append("Valid. Contains at least one special character.")
    else:
        strength_feedback.append("Invalid. Should include at least one special character.")

    # Determine overall strength
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, strength_feedback


# Main function to interact with the user
def main():
    print("Welcome to the Password Strength Assessment Tool!")
    password = input("Please enter a password to check its strength: ")

    strength, feedback = assess_password_strength(password)

    print("\nPassword Strength:", strength)
    print("Feedback:")
    for message in feedback:
        print(message)


if __name__ == "__main__":
    main()