import argparse


def average(grades):
    return sum(grades) / len(grades)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--grades", nargs="+", type=float, help="List of grades")
    parser.add_argument("-f", "--float", type=int, default=2, help="Round")
    args = parser.parse_args()
    
    grades = list(map(float, args.grades))
    decimal_places = args.float

    ave = average(grades)
    print(f"Average = {ave:.{decimal_places}f}")


if __name__ == "__main__":
    main()
