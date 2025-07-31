is_valid = False

while not is_valid:
    username = input("Enter username: ")
    if not 5 < len(username) < 15:
        print("Username must be between 5 and 15 characters.")
    elif ' ' in username:
        print("Username must not contain spaces.")
    elif not username[0].isalpha():
        print("Username must start with a letter.")
    elif '__' in username:
        print("Username must not have consecutive underscores.")
    elif not username[-1].isalpha():
        print("Username must end with a letter.")
    else:
        print(f"Welcome {username}!")
        is_valid = True
