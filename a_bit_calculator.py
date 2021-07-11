#!/usr/bin/env python

import os
import platform

while True:
    format = ""

    # Get format
    while True:
        print("\n============================")
        print("== ABC | A BIT CALCULATOR ==")
        print("============================")

        print("\nUnit to convert from:\n[1] Bit\n[2] Byte\n[3] KByte\n[4] MByte\n[5] GByte\n[6] TByte\n>> ", end = "")

        if (format == ""):
            format = input()
        else:
            print(format)

        if not (not str(format).isdigit() or (int(format) < 1) or (int(format) > 6)):
            format = int(format)

    # Get value
            try:
                value = float(input("\nValue to convert: \n>> "))
                break
            except:
                print("\n== Invalid input: Please enter a number ==")
                input("[Enter]")
                clear()
        else:
            print("\n== Invalid input: Please enter a number between 1 and 6 ==")
            input("[Enter]")
            format = ""
            clear()

    # Calculate value to bit
    if format > 1:
        value = value * 8 * 1024**(format - 2)

    # Output
    print("\nThese are the converted values:")
    print(f">> Bit  : " + "{:,}".format(value))
    print(f">> Byte : " + "{:,}".format(value / 1024**0 / 8))
    print(f">> KByte: " + "{:,}".format(value / 1024**1 / 8))
    print(f">> MByte: " + "{:,}".format(value / 1024**2 / 8))
    print(f">> GByte: " + "{:,}".format(value / 1024**3 / 8))
    print(f">> TByte: " + "{:,}".format(value / 1024**4 / 8))

    # Repeat the program
    repeat = input("\nDo you want to convert another number? [y/n]\n>> ")
    clear()

    if repeat != "y":
        break

def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin":
        os.system('clear')
