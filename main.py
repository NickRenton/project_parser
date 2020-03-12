from file_manager import add_new_word

def main():
    while True:
        user_input = input('Enter the number:\n')
        try:
             user_input = int(user_input)
        except Exception:
            print('Please enter a number')
            continue
        else:
            if user_input == 0:
                break
            elif user_input == 1:
                add_new_word()
            elif user_input == 2:
                pass
            elif user_input == 3:
                pass
            elif user_input == 4:
                pass
            elif user_input == 5:
                pass
            elif user_input == 6:
                pass
            elif user_input == 7:
                pass
            else:
                print('Please enter a valid number')
                continue

main()
