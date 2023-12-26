import os

restaurants = [{'name': 'Sushi Saque', 'category': 'japanese food', 'active': False},
               {'name': 'Sapori', 'category': 'italian food', 'active': False},
               {'name': 'Chimarron', 'category': 'barbecue', 'active': False}]

def display_program_name():
    print('EXPRESS RESTAURANT\n')

def display_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Toggle restaurant status')
    print('4. Exit\n')

def finalize_app():
    display_subtitle('Finalize app')

def return_to_main_menu():
    input('\nType any key to return to the menu: ')
    main()

def invalid_option():
    print('Invalid option!\n')
    return_to_main_menu()

def display_subtitle(text):
    os.system('clear')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def register_new_restaurant():
    '''This role is responsible for registering a new restaurant

    Inputs:
    - Name of restaurant
    - Category

    Outputs:
    - Adds a new restaurant to the restaurant list
    '''

    display_subtitle('Registration of new restaurants')
    name_of_restaurant = input('Enter the name of the restaurant you want to register: ')
    category = input(f'Enter the name of the restaurant category {name_of_restaurant}: ')
    data_of_restaurant = {'name':name_of_restaurant, 'category': category, 'active': False}
    restaurants.append(data_of_restaurant)
    print(f'The restaurant {name_of_restaurant} has been successfully registered.')

    return_to_main_menu()

def list_restaurants():
    '''This function lists existing restaurants'''
    display_subtitle('Listing restaurants')
    print(f'{'Name of restaurant'.ljust(22)} | {'Category'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        category = restaurant['category']
        active = 'activated' if restaurant['active'] else 'disable'
        print(f'- {restaurant_name.ljust(20)} | {category.ljust(20)} | {active}')

    return_to_main_menu()

def toggle_restaurant_status():
    '''This function is responsible for switching restaurants between active or deactivated'''
    display_subtitle('Changing restaurant status')
    restaurant_name = input('Enter the name of the restaurant you want to change the status of: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'The restaurant {restaurant_name} it has been activated successfully' if restaurant['active'] else f'The restaurant {restaurant_name} it has been successfully deactivated.'
            print(message)
        
    if not restaurant_found:
        print('The restaurant was not found')
    
    return_to_main_menu()

def choose_option():
    '''This function contains decisions based on user choice'''
    try:
        chosen_option = int(input('Choose an option: '))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            toggle_restaurant_status()
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
    choose_option()

if __name__ == '__main__':
    main()