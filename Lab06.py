# Agustin Zurlo Redi encode() method
def menu():
    global option
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")
    option = int(input("Please enter an option: "))
    return option


def encode():
    global new_password
    new_password = str("")
    password = str(input("Please enter your password to encode: "))
    if len(password) != 8 or any(char.isalpha() for char in password):
        print("Password must be 8 digits long and can only contain numbers.")
        encode()
    else:
        for char in password:
            new_char = (int(char) + 3) % 10
            new_password = new_password + str(new_char)
        print("Your password has been encoded and stored!\n")
    return new_password

def decode():
    decoded_pass = ''
    for num in new_password:
        new_num = str((int(num)-3) % 10)
        decoded_pass += new_num
    print(f'The encoded password is {new_password}, and the original password is {decoded_pass}.')
    return 


if __name__ == '__main__':
    option = int()
    new_password = str("")
    menu()
    while True:
        if option < 1 or option > 3:
            print("Error. Input must be '1', '2', or '3'\n")
            menu()
            continue
        elif option == 1:
            encode()
            menu()
        elif option == 2:
            decode()
            menu()
        elif option == 3:
            break
