# 04. Extract Emails
user = (^|\s)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*\b
host = \@[a-z]+((\-)[a-z]+)*\.[a-z]+((\.)[a-z]+)*
import re

data = input()
pattern = r"(^|\s)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*\b\@[a-z]+((\-)[a-z]+)*\.[a-z]+((\.)[a-z]+)*"

valid_emails = re.finditer(pattern, data)

for email in valid_emails:
    print(email.group())