# 1. Valid Usernames
import re

usernames_string = input().split(", ")

for username in usernames_string:
    if 3 < len(username) < 16:
        if re.match("^[A-Za-z0-9_-]*$", username):
            print(username)