class Pangram:
    def check(self, str):
        inputted = list()
        str = str.lower()
        # since set is used one alphabet will be present only once
        str = set(str)
        for i in str:
            # Using ascii we check if the character is within ato z or not
            if ord(i) in range(ord('a'), ord('z')+1):
                inputted.append(i)
        if len(inputted) == 26:  # If the count is 26 therefore all aplhabets are present
            print("The String is a Pangram")
        else:
            print("The String is not a Pangram")


p = Pangram()
s = input("Enter the string :\n")
p.check(s)
