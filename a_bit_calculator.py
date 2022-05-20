#!/usr/bin/env python


import os
import platform


def main():
    format  = get_format()
    value   = get_value(format)
    print_output(value)

    main() if ask_for_repeation() else exit_program()


# region GET FORMAT
def get_format():
    while True:
        print_format_UI()
        format = input()

        if not verify_format(format):
            continue

        return int(format)


def print_format_UI():
    print_header()
    print("\nUnit to convert from:\n[1] Bit\n[2] Byte\n[3] KByte\n[4] MByte\n[5] GByte\n[6] TByte\n>> ", end=" ")


def verify_format(format):
    if format.isdigit() and (1 <= int(format) <= 6):
        return True

    print("\n== Invalid input: Please enter a number between 1 and 6 ==")
    input("[Enter]")
    return False
# endregion


# region GET VALUE
def get_value(format):
    while True:
        print_value_UI(format)
        value = input()

        if not verify_value(value):
            continue

        return unify_value_into_bit(float(value), format)


def print_value_UI(format):
    print_header()
    print(f"\nSelected format: {format}\n\nValue to convert:\n>> ", end=" ")


def verify_value(value):
    if value.isdigit():
        return True

    print("\n== Invalid input: Please enter a number ==")
    input("[Enter]")
    return False


def unify_value_into_bit(value, format):
    return value if format == 1 else value * 8 * 1024**(format - 2)
# endregion


def print_output(result):
    print("\nThese are the converted values:")
    print(f">> Bit  : " + "{:,}".format(result))
    print(f">> Byte : " + "{:,}".format(result / 1024**0 / 8))
    print(f">> KByte: " + "{:,}".format(result / 1024**1 / 8))
    print(f">> MByte: " + "{:,}".format(result / 1024**2 / 8))
    print(f">> GByte: " + "{:,}".format(result / 1024**3 / 8))
    print(f">> TByte: " + "{:,}".format(result / 1024**4 / 8))


def print_header():
    clear_console()
    print("\n============================")
    print("== ABC | A BIT CALCULATOR ==")
    print("============================")


def clear_console():
    current_system = platform.system()
    
    if current_system == "Linux":
        os.system('clear')
    elif current_system == "Windows":
        os.system('cls')
    elif current_system == "Darwin":
        os.system('clear')


def ask_for_repeation():
    repeat = input("\nDo you want to convert another number? [y/n]\n>> ")
    return True if repeat == "y" else False


def exit_program():
    clear_console()
    exit(0)


if __name__ == "__main__":
    main()