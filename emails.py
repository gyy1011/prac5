def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        verification = input("Is your name {}? (Y/N)".format(name))
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_name[email] = name
        email = input(("Email: "))
    for email, name in email_name.items():
        print("{} ({})".format(name, email))
def get_name():
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name

if __name__ == '__main__':
    main()