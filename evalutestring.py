
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_range = input("Enter a range of letters (e.g., a-z): ")
#Create a list to store user input that is separated by '-'
split = user_range.split('-')

#Initialize the starting indices of the starting letter and ending letter
startingLetter = alphabet.index(split[0])
endingLetter = alphabet.index(split[1])
result_string = alphabet[startingLetter:endingLetter+1]

#Display result
print(result_string)
