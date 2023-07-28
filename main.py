"""
projekt_2.py: 

author: Daniel Ivánek   
email: ivanek.daniel99@gmail.com
discord: Notme#1202
"""
import random
import test

# Pseudocode
# Program pozdraví užitele a vypíše úvodní text
# Vytvor promennou pro nahodne 4 mistne cislo(Musi byt unikatni a nezacinat 0)
# Hrac zada cislo.
# IF cislo kratsi nez 4 cisla OR cislo obsahuje duplicity OR cislo zacina nulou OR cislo obsahuje neciselne znaky:
#   upozorni hrace at zada korektni cislo
# Vyhodnotit vygenerovane cislo s cislem uzivatele
# IF cislo == cislo:
#       Ukonci program// VYHRA
# ELIF Podminky hry.

test.uvitani()
generated_number = test.generate_unique_four_digit_number()
selected_num = test.correct_number_check()


for digit in str(selected_num):
    if digit in str(generated_number):
        print(f"Contains {digit} in {generated_number}") 
    

 





