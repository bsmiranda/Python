import os

restaurants = ['Pizza', 'Sushi']

def display_program_name():
    print('EXPRESS RESTAURANT')

def display_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Activate restaurant')
    print('4. Exit\n')

def finalize_app():
    display_subtitle('Finish app')

def return_to_main_menu():
    input('\nEnter a key to return to the menu ')
    main()

def invalid_option():
    print('Invalid option!\n')
    return_to_main_menu()

def display_subtitle(text):
    os.system('clear')
    print(text)
    print()

def register_new_restaurant():
    display_subtitle('Registration of new restaurants')
    restaurant_name = input('Enter the name of the restaurant you wish to register: ')
    restaurants.append(restaurant_name)
    print(f'The restaurant {restaurant_name} was successfully registered!')
    
    return_to_main_menu()


def list_restaurants():
    display_subtitle('Listing restaurants')
    for restaurant in restaurants:
        print(f'.{restaurant}')
    return_to_main_menu()

def chose_option():
    try:
        chosen_option = int(input('Choose an option: '))
        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print('Activate restaurant')
        elif chosen_option == 4:
            finalize_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    display_program_name()
    display_options()
    chose_option()

if __name__ == '__main__':
    main()