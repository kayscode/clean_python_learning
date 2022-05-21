# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from taxa_adminitration.taxation import products_price, calculate_tax

    print(calculate_tax(products_price))
    print_hi('PyCharm')

    student_list = [
        {
            'first_name': "james",
            'last_name': "kesler"
        }, {
            'first_name': "wil",
            'last_name': "kesler"
        }, {
            'first_name': "aniston",
            'last_name': "kesler"
        },
    ]

    twice_numbers = [12, 24, 26, 48, 92, 184, 22, 82]

    numbers = map(lambda num: num / 2, twice_numbers)
    for num in numbers:
        print(num)

    list_comprehension = [num / 2 for num in twice_numbers if (num / 2) % 2]
    print('with list0-comprehension -> ', list_comprehension)

    def sorted_odd(number):
        """
            test if a number is odd or not
        :param number:
        :return: boolean
        """
        if (number/2) % 2:
            return True

        return False

    filter_twice_numbers = filter(sorted_odd,twice_numbers)
    print(" filter using filter function : ")
    for num in filter_twice_numbers:
        print(num)


    def filter_by_vowel(name: str) -> bool:
        """
            filter a text if the contain a specific vowel like a.
        """
        if not name.__contains__('a'):
            return True

        return False

    users_list = [
        "samy kayembe",
        "robin kesler",
        "wil kesler"
    ]

    for user_filtered in filter(filter_by_vowel,users_list):
        print(" ".join(["user : ", user_filtered]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
