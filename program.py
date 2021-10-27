#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list


def average_calculator(marks):
    total_mark = 0
    for counter in range(0, len(marks)):
        total_mark = total_mark + marks[counter]
    average = total_mark / (counter + 1)
    return average


def main():
    # this function uses a list

    marks = []
    mark = None

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")

    while True:
        integer = input("What is your mark (as %): ")
        try:
            mark = int(integer)
            if mark > 100 and mark != -1 or mark < 0 and mark != -1:
                print("Invalid input")
            elif mark == -1:
                break
            else:
                marks.append(mark)
        except Exception:
            print("Invalid input")
    average = average_calculator(marks)
    print("The average is {0:,.0f}%".format(average))


if __name__ == "__main__":
    main()
