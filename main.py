#!/usr/bin/env python
# made with love by wahyuarief

import base64, os

rechoice = ''
while rechoice != 'n':
    print("1. Encode Base16")
    print("2. Decode Base16")
    print("3. Encode Base32")
    print("4. Decode Base32")
    print("5. Encode Base64")
    print("6. Decode Base64")
    choice = int(input("Choice: "))
    
    if choice == 1:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b16encode(string)

    elif choice == 2:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b16decode(string)

    elif choice == 3:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b32encode(string)

    elif choice == 4:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b32decode(string)

    elif choice == 5:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b64encode(string)

    elif choice == 6:
        string = raw_input("\nYour string: ")
        print "~> " + base64.b64decode(string)

    else:
        break

    rechoice = raw_input("\nRechoice? (y/n) ")
    os.system('clear')
