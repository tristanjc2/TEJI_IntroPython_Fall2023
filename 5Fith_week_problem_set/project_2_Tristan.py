start_range = 1
end_range = 100
guess = 0

while guess != "yes":
    guess = (start_range + end_range) // 2
    print("Is your number",guess,"?")
    guess_num = input("higher, lower, yes: ")
    if guess_num == "higher":
        start_range = (guess + end_range) // 2
        start_range = guess + 1
    elif guess_num == "lower":
        end_range = (guess + start_range) // 2
        end_range = guess
    else:
        print("You guessed the number!")
        break