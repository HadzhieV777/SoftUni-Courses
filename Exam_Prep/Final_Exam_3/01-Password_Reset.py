01. Password Reset
password = input()
commands = input()

while not commands == "Done":
    command = commands.split()[0]

    if command == "TakeOdd":
        new_raw_password = ""
        for x in range (len(password)):
           if x % 2 == 1:
               new_raw_password += password[x]
        password = new_raw_password
        print(password)

    elif command == "Cut":
        index = int(commands.split()[1])
        length = int(commands.split()[2])
        first_part = password[:index]
        last_part = password[index + length:]
        password = first_part + last_part
        print(password)

    elif command == "Substitute":
        substring = commands.split()[1]
        substitute = commands.split()[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    commands = input()

print(f"Your password is: {password}")