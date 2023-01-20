#!/bin/python3

# unused function for testing function 
def str_reverse(s):
    return s[::-1]

def main():
    txt_string = input("Enter a string : ")
    print(f"The string '{txt_string}' is {len(txt_string)} chars long!")

if __name__ == "__main__":
    main()