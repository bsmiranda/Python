import os

def display_program_name():
    print('EXPRESS RESTAURANT')

def display_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Activate restaurant')
    print('4. Go out\n')

def finalize_app():
    os.system('clear')
    print('Finalizing the app')

def choose_options():
    chosen_option = int(input('Choose an option: '))

    if chosen_option == 1:
        print('1. Register restaurant')
    elif chosen_option == 2:
        print('2. List restaurant')
    elif chosen_option == 3:
        print('3. Activate restaurant')
    else:
        finalize_app()

def main():
    display_program_name()
    display_options()
    choose_options()

if __name__ == '__main__':
    main()