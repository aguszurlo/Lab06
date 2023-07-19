# Mateo Budan encode() method
def encode(password):
    encoded_pass = ''
    for num in password:
        new_num = str((int(num)+3) % 10)
        encoded_pass += new_num
    return encoded_pass

if __name__ == '__main__':
    stored_password = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            stored_password = encode(password)
            print('Your password has been encoded and stored!\n')
        if choice == 3:
            break



