"""
projekt_2.py: 

author: Daniel Ivánek   
email: ivanek.daniel99@gmail.com
discord: Notme#1202
"""
import random
import test
line = "-" * 30



test.uvitani()

def generate_unique_four_digit_number():
    # Generate a random permutation of digits 1 to 9
    digits = random.sample(range(1, 10), 4)

    # Convert the list of digits to a 4-digit integer
    ran_number = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]

    return ran_number

generated_num = generate_unique_four_digit_number()

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


x_count = 0
y_count = 0

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


while x_count != 4:
    selected_num = test.correct_number_check()
    s_num_pr = selected_num
    x_count,y_count = test.compare_numbers(generated_num,selected_num)
    print(f">>> {s_num_pr}")
    if x_count == 1:
        print(f"{x_count} Bull", end=" ")
    else:
        print(f"{x_count} Bulls", end=" ")
    if y_count == 1:
        print(f"{y_count} Cow")
    else:
        print(f"{y_count} Cows")
    print(line)

print(f"Correct, you've guessed the right number")
print(f"Generated number is: {generated_num}")


















