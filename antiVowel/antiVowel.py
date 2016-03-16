def anti_vowel(text):
    x=""
    for char in text:
        if char not in "aeiouAEIOU":
          x=x+char
    return x

s=raw_input("Enter the string :")
print anti_vowel(s)    
