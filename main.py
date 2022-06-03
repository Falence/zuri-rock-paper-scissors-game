import random

# Possible options
options = ['R', 'P', 'S']


while True:
    # Get user option
    user_option = input('Enter your option: ').upper()

    # Generate CPU option
    cpu_option = random.choice(options)
    print(cpu_option)

    if user_option not in options:
        print("Invalid input! --> R (ROCK), P (PAPER) & S (SCISSORS)")
        continue
    elif user_option == cpu_option:
        print(f"Player ({user_option}) : CPU ({cpu_option})")
        print("IT'S A DRAW!!!")
        print("---------------------", "RESTARTING GAME", "---------------------")
    elif user_option == 'R':
        if cpu_option == 'S':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("Player WINS!")
            break
        elif cpu_option == 'P':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("CPU WINS!")
            break
    elif user_option == 'P':
        if cpu_option == 'R':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("Player WINS!")
            break
        elif cpu_option == 'S':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("CPU WINS!")
            break
    elif user_option == 'S':
        if cpu_option == 'P':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("Player WINS!")
            break
        elif cpu_option == 'R':
            print(f"Player ({user_option}) : CPU ({cpu_option})")
            print("CPU WINS!")
            break
