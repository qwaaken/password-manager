import random
import time

password_list = {}

# Présentation
print('Welcome to your password manager')

while True:
    time.sleep(1)
    command = input(
        'What do you want to do?\n'
        '1. Show passwords list\n'
        '2. Delete a password\n'
        '3. Add a password\n'
        '4. Create a random password\n'
        'Choose an option: '
    )

    # Afficher les mots de passe
    if command == '1':
        if not password_list:
            print('The password list is empty')
        else:
            print('Here is your password list:')
            for platform, password in password_list.items():
                print(f'Platform: {platform} - Password: {password}')

    # Supprimer un mot de passe
    elif command == '2':
        if not password_list:
            print('The password list is empty')
        else:
            print('Here is your password list:')
            for platform in password_list.keys():
                print(f'- {platform}')
            delete = input('Which platform\'s password do you want to delete? ')
            time.sleep(1)
            if delete in password_list:
                del password_list[delete]
                print(f'Password for "{delete}" has been deleted.')
            else:
                print(f'No password found for "{delete}".')

    # Ajouter un mot de passe
    elif command == '3':
        app_choice = input('For what platform do you want to add a password? ')
        time.sleep(1)
        password_choice = input('Type your password: ')
        password_list[app_choice] = password_choice
        print(f'Password for "{app_choice}" has been added.')

    # Générer un mot de passe aléatoire
    elif command == '4':
        symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        app_choice2 = input('For what platform do you want to add a password? ')
        length = int(input('Password length: '))
        password = ''
        for i in range(length):
            password += random.choice(symbols)
        print('Here is your password:', password)
        password_list[app_choice2] = password
        print('Here is your full list:', password_list)
        time.sleep(1)

    # Option invalide
    else:
        print('Invalid option. Please choose a number between 1 and 4.')
