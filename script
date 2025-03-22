import random
import time
password_list = {}
#persentation
print('Welcome to your passwords manager')
while True:
    time.sleep(1)
    command = input('What do you want to do ? : 1.show passwords list 2.delete a password 3.add a password 4.create a random password')
    #show passwords
    if command == '1':
        if not password_list:
            print('The password list is empty')
        else:
            print(password_list)
    elif command == '2':
        if not password_list:
            print('The password list is empty')
        else:
            print(password_list)
            delete = input('Which password do you want to delete ? ')
            time.sleep(1)
            del password_list[delete]
    elif command == '3':
        app_choice = input('For what platform do you want to add a password ? ')
        time.sleep(1)
        password_choice = input('Type your password : ')
        password_list[app_choice] = password_choice
        print(password_list)
    elif command == '4':
        app_choice2 = input('For what platform do you want to add a password ? ')
        random_m_letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
        random_m_letter2 = random.choice([ 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z'])
        random_b_letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ])
        random_b_letter2 = random.choice(['m','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        random_number = random.choice(['1','2','3','4','5'])
        random_number2 = random.choice(['6','7','8','9','0'])
        random_character = random.choice(['?','!','.'])
        random_character2 = random.choice([',',':','/'])
        time.sleep(1)
        random_password = random_m_letter + random_b_letter + random_character + random_number + random_number2 + random_m_letter2 + random_b_letter2 + random_character2
        print('your password : ', random_password)
        password_list[app_choice2] = random_password
        print(password_list)
