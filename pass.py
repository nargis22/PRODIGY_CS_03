def password_complexity(password):
    # Define criteria for password complexity
    criteria = {
        'length': len(password) >= 8,
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password)
    }

    # Count the number of met criteria
    complexity_score = sum(criteria.values())

    return complexity_score

def assess_password_strength(complexity_score):
    if complexity_score == 4:
        return "very strong"
    elif complexity_score == 3:
        return "strong"
    elif complexity_score == 2:
        return "moderate"
    elif complexity_score == 1:
        return "weak"
    else:
        return "very weak"

# Example usage:
password = input("enter password")
complexity_score = password_complexity(password)
strength = assess_password_strength(complexity_score)
print(f"The password '{password}' is {strength}.")