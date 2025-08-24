guess_word = "India"
guess = " "
guess_count = 0
guess_limit = 4
out_of_guess = False 

print("----Welcome to a Simple Guess Game----")
print("----You will get 4 chances to GUESS the correct word----")
print("----Let's Begin----")
while guess != guess_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter Your Guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("YOU LOST")
else:
    print("YOU WIN")


# TEST CASES
# ----Welcome to a Simple Guess Game----
# ----You will get 4 chances to GUESS the correct word----
# ----Let's Begin----
# Enter Your Guess: HshSks
# Enter Your Guess: hbassnkms
# Enter Your Guess: djsnjNS
# Enter Your Guess: SBSBJSB
# YOU LOST

# ----Welcome to a Simple Guess Game----
# ----You will get 4 chances to GUESS the correct word----
# ----Let's Begin----
# Enter Your Guess: DXBSI
# Enter Your Guess: India 
# YOU WIN
