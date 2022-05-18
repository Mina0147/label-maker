from calc import calculate_unit_price
from inputs import user_input
from outputs import to_console


def main():
    data = user_input()
    calculated_data = calculate_unit_price(data)
    to_console(calculated_data)


if __name__ == '__main__':
    main()
