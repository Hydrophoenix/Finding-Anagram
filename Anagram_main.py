# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("Enter a word: ")
anagram = input("Enter a second word: ")



def find_anagram(word, anagram):
    
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


anagram_check = find_anagram(word, anagram)
print(anagram_check)

