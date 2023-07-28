
import random

### Uvitaci fce
def uvitani():
    print("""
          Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
        """  )
    
### Generovani random number fce
def generate_unique_four_digit_number():
    # Generate a random permutation of digits 1 to 9
    digits = random.sample(range(1, 10), 4)

    # Convert the list of digits to a 4-digit integer
    ran_number = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]

    return ran_number


### Kontrola zadaneho cisla fce

def correct_number_check():
    smycka = True
    while smycka:
        players_number = input("Guess the number: ")
        if not players_number.isdigit():
            print("You entered non-numeric value.")
            continue
        elif str(players_number[0]) == "0":
            print("Number starts with 0.")
            continue
        elif len(set(list(str(players_number)))) != 4:
            print("Number has less/more than 4 digits or includes duplicates")
        else:
            smycka = False
   
    print("hope it works")
    return players_number    




if __name__ == "__main__":
    print("Hello, World!")
