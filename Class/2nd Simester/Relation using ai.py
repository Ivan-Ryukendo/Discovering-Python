import re

def validate_emails(emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return [re.match(pattern, email) is not None for email in emails]

# Test the function
emails = ["example@example.com", "invalid_email", "another@example.com"]
print(validate_emails(emails))  # Output: [True, False, True]