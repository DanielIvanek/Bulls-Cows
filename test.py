
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
    



def generate_unique_four_digit_number():
    first_digit = random.randint(1, 9)
    other_digits = random.sample([x for x in range(10) if x != first_digit], 3)

    ran_number = first_digit * 1000 + other_digits[0] * 100 + other_digits[1] * 10 + other_digits[2]

    return ran_number





    
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


def compare_numbers(generated_num, selected_num):
    generated_str = str(generated_num)
    selected_str = str(selected_num)
    x_count = 0
    y_count = 0
    
    checked_indices = set()

    for digit in range (len(generated_str)):
        if generated_str[digit] == selected_str[digit]:
            x_count += 1
            checked_indices.add(digit)
    for digit in range(len(generated_str)):
        if digit not in checked_indices and generated_str[digit] in selected_str:
            y_count += 1
    return x_count,y_count








if __name__ == "__main__":
    print("Hello, World!")


# def compare_numbers(generated_num, selected_num):
#     generated_str = str(generated_num)
#     selected_str = str(selected_num)
#     x_count = 0
#     y_count = 0
    
#     checked_indices = set()

#     for digit in range (len(generated_str)):
#         if generated_str[digit] == selected_str[digit]:
#             x_count += 1
#             checked_indices.add(digit)
#     for digit in range(len(generated_str)):
#         if digit not in checked_indices and generated_str[digit] in selected_str:
#             y_count += 1
#     return x_count,y_count


# def correct_number_check():
#     smycka = True
#     while smycka:
#         players_number = input("Guess the number: ")
#         if not players_number.isdigit():
#             print("You entered non-numeric value.")
#             continue
#         elif str(players_number[0]) == "0":
#             print("Number starts with 0.")
#             continue
#         elif len(set(list(str(players_number)))) != 4:
#             print("Number has less/more than 4 digits or includes duplicates")
#         else:
#             smycka = False
   
#     print("hope it works")
#     return players_number

# def generate_unique_four_digit_number():
#     # Generate a random permutation of digits 1 to 9
#     digits = random.sample(range(1, 10), 4)

#     # Convert the list of digits to a 4-digit integer
#     ran_number = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]

#     return ran_number