# Program to count the number of vowels in a string

s = "prepinsta"
vowel = 0

for i in range(len(s)):
    if s[i] in ('a', 'e', 'i', 'o', 'u'):
        vowel += 1

print(vowel)