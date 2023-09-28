import sys


def average(grades):
    return sum(grades) / len(grades)


def main():
    try:
        grades = list(map(float, sys.argv[1:]))
    except ValueError:
        print("Enter correct numbers!")
        
    ave = average(grades)
    print(f"Average = {ave}")


if __name__ == "__main__":
    main()
