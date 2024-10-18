def main():
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


def is_valid(s):
        if len(s) == 1:
            return False
        if len(s) < 7 and s[0].isalpha() and s[1].isalpha() and s.isalnum() == True:
            # Length, Alphanumeric, First 2 letters, Minimum 2 letters start ARE CHECKED
            # Code below checks if first number starts with 0
            for num,letter in enumerate(s): #to find index of numberstart and the letter
                thereisnumber = None
                if letter.isnumeric() == True:
                    thereisnumber = True
                    startofnum = letter
                    indexofnum = num
                    if startofnum == '0':
                        return False
                        break
                    else:
                        break
            ## To check the remaining characters if there are alphabets
            if thereisnumber == True:
                for n in s[indexofnum:]:
                    if n.isalpha() == True:
                        return False

            return True
        else:
            return False


main()
