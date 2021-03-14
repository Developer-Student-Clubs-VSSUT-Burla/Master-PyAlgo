"""
Two strings are anagrams if they are made of the same letters
arranged differently (ignoring the uppercase and lowercase).
Example-
    Silent and Listen
    Triangle and Integral
    This is a string and is this a string

For more info check out @    
wiki: https://en.wikipedia.org/wiki/Anagram


In-build functions or methods used-
.strip() is used to remove all the leading and trailing spaces
.lower() is used to convert all the letters in lowercase
.join()  is used to make a string from the list of alphabets returned by sorted()
sorted() is used to sort the alphabets present in string
"""

def check_anagrams(first_str: str, second_str: str) -> bool:
    
    return (
        "".join(sorted(first_str.lower())).strip()
        == "".join(sorted(second_str.lower())).strip()
    )


if __name__ == "__main__":

    #Taking input from the user
    str1 = input("Enter the first string ").strip()
    str2 = input("Enter the second string ").strip()

    status = check_anagrams(str1, str2)
    print(f"{str1} and {str2} are {'' if status else 'not '}anagrams.")


"""
Input - Triangle
        Integral
Output- Triangle and Integral are anagrams.

Input - Paper
      - Paint
Output- Paper and Paint are not anagrams.
"""
