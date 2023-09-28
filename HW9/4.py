import argparse
import random

def choose_random(start, end):
    if start > end:
        raise ValueError("The start must be smaller than the end!")
    else:
        random_number = random.randint(start, end)
        return random_number

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, help="Start of range")
    parser.add_argument("-e", "--end", type=int, help="End of range")
    parser.add_argument("-g", "--guess", type=int, help="Time to guess")
    args = parser.parse_args()

    random_number = choose_random(args.start, args.end)
    
    for time in range(args.guess):
        try:
            guess = int(input("Guess number: "))
            
            if guess > random_number:
                print("Enter Lower Number!")
                
            elif guess == random_number:
                print("Your guess is correct, the selected number is",random_number)
                break
            else:
                print("Enter Higher Number!")
                
        except ValueError:
            print("Please enter integer number!")
    
    else:
        print("You tried",args.guess,"times, the selected number is",random_number)
    
if __name__ == "__main__":
    main()
