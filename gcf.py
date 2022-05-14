#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, calculating the GCF(greatest common factor) of two numbers


def main():
    # This function calculates GCF

    # input
    print(
        "This function calculates the GCF of two numbers, and it only accepts integers."
    )
    number_a_string = input("Enter the first number: ")
    number_b_string = input("Enter the second number: ")

    # process & output
    print("")
    try:
        number_a_integer = int(number_a_string)
        number_b_integer = int(number_b_string)
        number_a = abs(number_a_integer)
        number_b = abs(number_b_integer)
        while number_a - number_b != 0:
            absolute = abs(number_a - number_b)
            if number_a > number_b:
                number_a = absolute
            else:
                number_b = absolute
        greatest_common_factor = number_a
        print(
            "The Greatest Common Factor of {0} and {1} is {2}.".format(
                number_a_integer, number_b_integer, greatest_common_factor
            )
        )
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
