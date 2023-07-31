"""
projekt_2.py: 
author: Daniel Ivánek   
email: ivanek.daniel99@gmail.com
discord: Notme#1275
"""

import test
import uuid
import time

try_count = 0
x_count = 0
y_count = 0
game_id = str(uuid.uuid4())
start_time = time.time()


test.uvitani()
generated_num = test.generate_unique_four_digit_number()


while x_count != 4:
    selected_num = test.correct_number_check()
    x_count, y_count = test.compare_numbers(generated_num, selected_num)
    test.print_guess_result(selected_num, x_count, y_count)
    try_count += 1

print(f"Correct, you've guessed the right number")
print(f"Generated number is: {generated_num}")
print(f"It takes {try_count} guesses")


end_time = time.time()
duration = end_time - start_time
with open("game_records.txt", mode="a") as txt_file:
    txt_file.write(
        f"\n Game ID: {game_id},    Generated number: {generated_num},      Guesses: {try_count}         Duration: {duration: .0f} seconds"
    )
