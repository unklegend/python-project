from random import *



user_pass = input("enter your password :")



password = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",

                "v", "w", "x", "y", "z", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";",

                "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", "?", "0", "1", "2", "3", "4", "5",

                "6", "7", "8", "9" , "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",

                "V", "W", "X", "Y", "Z"]



guess = ""



while (guess != user_pass):



        guess = ""



        for letter in range(len(user_pass)):

            guess_letter = password[randint(0,91)]



            guess = str(guess_letter) + str(guess)



            print(guess)



print("your password is ", guess)# this coding will shows the entered password.
print("Enter Thanks below\n")

n1 = input("Enter here")

if n1==("thanks"):

    print("Thanks to you :)")

else:

    print("Thanks toh bool deta :(")

