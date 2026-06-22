#S1. Reverse a string without slicing
def reverse_string(org_str):
    l = len(org_str)
    m = -1
    for i in range(l):
        reversed = "".join(org_str[m])
        m-=1
        print(reversed)
reverse_string('smita')

#S2. Check whether a string is palindrome
#S3. Count vowels and consonants separately
#S4. Find longest word in a sentence
#S5. Reverse words in a sentence without using split reverse shortcut
#S6. Count frequency of each character manually
#S7. Find duplicate characters in a string
#S8. Find first non-repeating character
#S9. Remove duplicate characters while preserving order
#S10. Check whether two strings are anagrams
#S11. Generate all substrings of a string
#S12. Implement split() manually
#S13. Implement join() manually
#S14. Compress string (aaabbcc → a3b2c2)
#S15. Find longest common prefix in list of strings

#L1. Reverse list without reverse()
def reverse_list(lst):
    lst_copy = lst.copy()
    l = len(lst)
    n = -1
    for i in range(l):
        lst[i]=lst_copy[n]
        n-=1
    print(lst)

#L2. Find second largest number
def second_largest_entry(l):
    l.sort()
    second_largest = l[-2]
    print(second_largest)

#L3. Move all zeroes to end
#L4. Remove duplicates manually
#L5. Remove duplicates from sorted list
#L6. Rotate list by k positions
#L7. Find duplicate elements in list
#L8. Find intersection of two lists
#L9. Merge two sorted arrays
#L10. Split list into chunks of size k
#L11. Implement append manually
#L12. Implement pop manually
#L13. Implement insert manually
#L14. Find missing number in array
#L15. Flatten nested list recursively

#D1. Count character frequency using dictionary
#D2. Count occurrences of elements in list
#D3. Create dictionary from two lists
#D4. Find key with maximum value
#D5. Count word frequency in paragraph
#D6. Merge dictionaries manually
#D7. Sort dictionary by values
#D8. Invert dictionary keys and values
#D9. Group words by their length
#D10. Group anagrams using dictionary

#SET1. Remove duplicates from list using set
#SET2. Find common elements between two lists
#SET3. Check whether one set is subset of another
#SET4. Find elements unique to each array
#SET5. Implement union manually
#SET6. Implement intersection manually
#SET7. Implement symmetric difference manually

#T1. Convert nested tuple into list
#T2. Unpack nested tuples
#T3. Swap variables using tuples only
#T4. Sort list of tuples by second element

#F1. Write iterative factorial
#F2. Write recursive factorial
#F3. Implement Fibonacci iteratively
#F4. Implement Fibonacci recursively
#F5. Return multiple values from function
#F6. Sort list using lambda
#F7. Write function using *args
#F8. Write function using **kwargs
#F9. Write function with default arguments
#F10. Write higher order function
#F11. Build nested function
#F12. Implement map() manually
#F13. Implement filter() manually
#F14. Implement reduce() manually
#F15. Build closure function

#C1. Create list using list comprehension
#C2. Create dictionary using dict comprehension
#C3. Create set using set comprehension
#C4. Filter even numbers using comprehension
#C5. Replace loop logic with comprehension
#C6. Flatten nested list using comprehension