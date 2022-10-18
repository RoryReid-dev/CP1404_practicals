"""
Email
Estimate: 20 minutes
Actual:   15 minutes
"""


def main():
    """Create dictionary of emails converting to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name(email):
    """determine name from email address."""
    first_name = email.split('@')[0]
    last_name = first_name.split('.')
    name = " ".join(last_name).title()
    return name


main()
