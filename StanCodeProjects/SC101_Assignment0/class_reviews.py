"""
File: class_reviews.py
Name: Karen Chang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1

def main():
    """
    This program will ask user to input the class name (either SC001 or SC101) and score.
    And it will calculate the maximum, minimum, and average among all the inputs.
    If user input "-1" for class name, it will show the results.
    """
    num_001 = 0
    num_101 = 0

    while True:
        cla = str(input('Which class: ')).upper()  # Ask user to input the class name

        # User inputs "-1" for the class name
        if cla == str(EXIT):

            # User hadn't input any data before inputting "-1"
            if num_001 == 0 and num_101 == 0:
                print('No class score were entered')

            # Show the result.
            else:
                print(str(divider_001("SC001")))
                if num_001 == 0:
                    print('No score for SC001')
                else:
                    print('Max: ' + str(max_001))
                    print('Mix: ' + str(min_001))
                    print('Avg: ' + str(total_001/num_001))

                print(str(divider_001("SC101")))
                if num_101 == 0:
                    print('No score for SC101')
                else:
                    print('Max: ' + str(max_101))
                    print('Mix: ' + str(min_101))
                    print('Avg: ' + str(total_101/num_101))
            break

        # User inputs class name and score except "-1" directly
        else:
            # The calculation for class SC001
            data = int(input('Score: '))
            if cla == 'SC001':
                num_001 += 1

                # Judgment is the first time user inputs the data
                if num_001 == 1:
                    max_001 = data
                    min_001 = data
                    total_001 = data
                else:
                    max_001 = maximun(max_001,data)
                    min_001 = minimun(min_001,data)
                    total_001 += data

            # The calculation for class SC101
            else:
                num_101 += 1

                # Judgment is the first time user inputs the data
                if num_101 == 1:
                    max_101 = data
                    min_101 = data
                    total_101 = data
                else:
                    max_101 = maximun(max_101,data)
                    min_101 = minimun(min_101,data)
                    total_101 += data


def divider_001(a):
    """
    Draw the divider for class SC001
    :return: the divider with '=' and 'SC001'
    """
    line = ""
    for i in range(13):
        line += '='
    if a == "SC001":
        line += 'SC001'
    else:
        line += 'SC101'
    for i in range(13):
        line += '='
    return line

def maximun(maxi,data):
    """
    :param maxi: The maximum number among all numbers user inputted
    :param data: The number user inputs
    :return: The bigger number between maxi and data
    """
    if maxi < data:
        maxi = data
    return maxi

def minimun(mini,data):
    """
    :param mini: The minimum number among all numbers user inputted
    :param data: The number user inputs
    :return: The smaller number between maxi and data
    """
    if mini > data:
        mini = data
    return mini


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
