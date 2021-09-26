master_pwd = input('Enter your master password: ')


def add():
    name = input('Account name: ')
    passwd = input('Enter the password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + passwd + '\n')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passd = data.split('|')
            print('User:', user, 'Passwd: ', passd)


while True:

    mode = input('Do you want to add or view password? Press q to quit: ')

    if mode == 'q':
        break
    if mode == 'add':
        add()

    elif mode == 'view':
        view()

    else:
        continue
