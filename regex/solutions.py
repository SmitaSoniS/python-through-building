#LC1. Check whether the word "Python" exists in the string "I am learning Python for Data Science".
w = "Python"
s = "I am learning Python for Data Science"
print(w in s)

#LC2. Find the first occurrence of "Python" in "I am learning Python for Data Science".
w = "Python"
s = "I am learning Python for Data Science"
print(s.find(w))

#LC3. Given the string "Python is great. I love Python. Python is easy.", find all occurrences of "Python".
#solve again
s = "Python is great. I love Python. Python is easy."
w = "Python"
start = 0
while True:
    index = s.find(w,start)
    if index == -1:
        break
    print(index)
    start = index +len(w)

#LC4. Given the string "Python is great. I love Python. Python is easy.", count how many times "Python" appears.
s = "Python is great. I love Python. Python is easy."
w = "Python"
word_count = s.count(w)
print(word_count)

#LC5. Given the string "Python is easy. Python is powerful.", replace every occurrence of "Python" with "Java".
#LC6. Given the string "Machine Learning with Python is fun.", check whether the exact phrase "Learning with Python" exists.
#LC7. Given the string "Python python PYTHON", perform a case-sensitive search for "Python".

#LC8. Given the string "apple|banana|mango|orange", split it using the delimiter "|".


#Update from here on
#CC1. Given the string "Order123Invoice456", extract all digits.

#CC2. Given the string "Order123Invoice456", extract all alphabetic characters.

#CC3. Given the string "PyTHon123AI", extract all uppercase letters.

#CC4. Given the string "PyTHon123AI", extract all lowercase letters.

#CC5. Given the string "Python@123!", extract all alphanumeric characters.

#CC6. Given the string "Python@123!", count the number of digits, letters, and special characters.

#CC7. Given the string "User123Account456", remove all digits.

#CC8. Given the string "Python@AI#2026!", remove all special characters.

#CC9. Given the string "abc123 xyz hello45 world", extract all words containing digits.

#CC10. Check whether the string "Python123" contains only alphanumeric characters.

#Character Sets

#CS1. Given the string "Artificial Intelligence", extract all vowels.

#CS2. Given the string "Artificial Intelligence", extract all consonants.

#CS3. Given the string "A1B2C3D4EF56789", extract all hexadecimal characters.

#CS4. Given the string "Artificial Intelligence", extract only lowercase vowels.

#CS5. Given the string "AI Revolution", extract only uppercase vowels.

#CS6. Given the string "abcXYZ123", extract characters from the range a–f.

#CS7. Given the string "Python Programming", extract all characters except vowels.

#CS8. Given the string "apple banana cherry avocado apricot", extract words beginning with "a".

#CS9. Given the string "Python123@AI!", extract every character except digits.

#CS10. Given the string "AB12xy@#", extract only uppercase letters and digits.

#Special Characters

#SC1. Given the string "Python AI\tML\nData", extract all whitespace characters.

#SC2. Given the string "Python AI ML", remove extra whitespace.

#SC3. Given the string "Python AI ML Data Science", extract all words.

#SC4. Given the string "Python@AI#2026!", extract all non-word characters.

#SC5. Given the string "Hello, World! Welcome.", extract all punctuation marks.

#SC6. Given the string "Python AI ML", replace multiple spaces with a single space.

#SC7. Given the string "John\nAlice\nBob", extract each record.

#SC8. Given the string "Python\tAI\nML", remove all tabs and newlines.

#SC9. Given the string "C:\\Users\\Smita\\Documents", extract escaped backslashes.

#SC10. Given the string "Python@@@###123!!!", remove unnecessary special characters.

#Quantifiers

#Q1. Given the string "11122 3334444", extract repeated digits.

#Q2. Given the string "aaabbccccdde", extract repeated alphabetic characters.

#Q3. Check whether "colour" and "color" both match the same pattern.

#Q4. Validate whether "ABCD" contains exactly 4 characters.

#Q5. Validate whether "Python" contains between 5 and 10 characters.

#Q6. Given the string "aaaabbbcc", match one or more consecutive "a" characters.

#Q7. Given the string "bbb aaa", match zero or more "a" characters.

#Q8. From the string "<tag>Python</tag><tag>AI</tag>", compare greedy and non-greedy matching.

#Q9. Given the string "hello hello world world world", extract repeated consecutive words.

#Q10. Validate whether "aaabbb" contains repeated character groups.

#Anchors

#A1. Check whether "Python is awesome" starts with "Python".

#A2. Check whether "report.pdf" ends with ".pdf".

#A3. Validate whether the string is exactly "Python".

#A4. Given multiple lines of text, match complete lines beginning with "ERROR".

#A5. Find standalone occurrences of "cat" in "cat catalog scatter".

#A6. Extract the first word from each line in a multi-line string.

#A7. Extract the last word from each line in a multi-line string.

#A8. Validate records in the format "Name,Age,City".

#A9. Match only standalone occurrences of "AI".

#A10. Match "AI" but ignore "AIML" and "OpenAI".

#Groups

#G1. Extract the first and last names from "Smita Soni".

#G2. Extract the area code from "(022)-9876543210".

#G3. Extract the username from "smita.soni@gmail.com".

#G4. Extract the extension from "report.pdf".

#G5. Extract day, month, and year from "17-07-2026".

#G6. Convert "Smita Soni" into "Soni, Smita".

#G7. Convert dates from "17-07-2026" to "2026/07/17".

#G8. Extract nested groups from "((Python))".

#G9. Extract date components using named groups.

#G10. Parse records like "ID:101 Name:Smita Salary:1800000".

#Alternation

#ALT1. Find "Python" or "Java" in a sentence.

#ALT2. Match files ending in .pdf, .docx, or .txt.

#ALT3. Match dates in either 17-07-2026 or 17/07/2026 format.

#ALT4. Split "apple,banana;orange|grapes" using multiple separators.

#ALT5. Match any of the keywords "AI", "ML", or "DL".

#ALT6. Validate phone numbers with or without country code.

#ALT7. Match phone numbers beginning with +91 or 0.

#ALT8. Extract either email addresses or phone numbers from text.

#Backreferences

#BR1. Detect repeated consecutive words in "hello hello world".

#BR2. Detect repeated consecutive characters in "aaabbbccc".

#BR3. Remove duplicate consecutive words from "AI AI is is powerful".

#BR4. Match repeated groups in "abcabc".

#BR5. Validate mirrored patterns like "abc|cba".

#BR6. Validate matching HTML tags like "<b>Text</b>".

#BR7. Match values enclosed within matching quotes.

#BR8. Replace duplicate consecutive words with a single occurrence.

#Lookarounds

#LA1. Extract words immediately followed by digits from "item123 product456".

#LA2. Extract digits immediately followed by letters from "123abc 456xyz".

#LA3. Extract words not followed by punctuation.

#LA4. Extract numbers not preceded by the currency symbol $.

#LA5. Extract values between square brackets in "[Python] [AI]".

#LA6. Validate a password containing at least one uppercase letter, one lowercase letter, one digit, and one special character.

#LA7. Extract values between <tag> and </tag>.

#LA8. Validate IDs only when preceded by "ID:".

#LA9. Find overlapping occurrences of "ana" in "banana".

#LA10. Extract IDs appearing after "EMP-".

#Python re Module

#RE1. Use re.search() to find "Python" in "I am learning Python".

#RE2. Use re.match() to check whether "Python" appears at the beginning of "Python is easy".

#RE3. Use re.fullmatch() to validate that the input is exactly "Python123".

#RE4. Use re.findall() to extract all email addresses from a paragraph.

#RE5. Use re.finditer() to locate every occurrence of "Python".

#RE6. Use re.sub() to replace all dates from DD-MM-YYYY to YYYY/MM/DD.

#RE7. Use re.subn() to replace "Python" with "Java" and report the number of replacements.

#RE8. Use re.split() to split "apple,banana;orange" using both commas and semicolons.

#RE9. Compile a regex pattern to validate Indian PIN codes and reuse it on multiple inputs.

#RE10. Escape the special characters in "price (₹100)" before searching.

#Real-World Validation

#RV1. Validate the email address "smita.soni@gmail.com".

#RV2. Validate the Indian phone number "+91-9876543210".

#RV3. Validate the URL "https://www.example.com".

#RV4. Validate the Indian PIN code "400001".

#RV5. Validate the date "17-07-2026".

#RV6. Validate the IPv4 address "192.168.1.100".

#RV7. Validate the PAN number "ABCDE1234F".

#RV8. Validate the password "Python@123".

#RV9. Extract hashtags from "Learning #Python #AI #DataScience".

#RV10. Extract mentions from "Thanks @smita and @john".

#RV11. Parse log entries like "2026-07-17 10:30:25 ERROR Connection failed".

#RV12. Extract timestamps from application logs.

#RV13. Remove all HTML tags from "<h1>Hello</h1><p>Welcome</p>".

#RV14. Extract the href attribute from "<a href='https://example.com'>Visit</a>".

#RV15. Extract key-value pairs from the configuration string "host=localhost;port=5432;user=admin".