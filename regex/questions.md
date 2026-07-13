# Regular Expressions (Regex) Questions

This section focuses on mastering regular expressions through hands-on problem solving.

Questions are grouped by topic and difficulty level, progressing from fundamental pattern matching to advanced text processing, extraction, and validation.

Use the question IDs to map solutions consistently across solution files.

---

# Literal Characters

## Level 1 — Fundamentals

* LC1. Check whether a word exists in a string.
* LC2. Find the first occurrence of a word.
* LC3. Find all occurrences of a word.
* LC4. Count occurrences of a word.
* LC5. Replace a word with another word.

## Level 2 — Intermediate

* LC6. Match an exact phrase.
* LC7. Perform case-sensitive matching.
* LC8. Split a string using a literal delimiter.

---

# Character Classes

## Level 1 — Fundamentals

* CC1. Extract all digits.
* CC2. Extract all alphabets.
* CC3. Extract uppercase letters.
* CC4. Extract lowercase letters.
* CC5. Extract alphanumeric characters.

## Level 2 — Intermediate

* CC6. Count digits, alphabets, and special characters.
* CC7. Remove all digits.
* CC8. Remove all special characters.
* CC9. Extract words containing digits.
* CC10. Validate an alphanumeric string.

---

# Character Sets

## Level 1 — Fundamentals

* CS1. Match vowels.
* CS2. Match consonants.
* CS3. Match hexadecimal characters.
* CS4. Match lowercase vowels only.
* CS5. Match uppercase vowels only.

## Level 2 — Intermediate

* CS6. Match characters within a range.
* CS7. Exclude specific characters.
* CS8. Extract words beginning with selected characters.
* CS9. Match characters except digits.
* CS10. Build custom character sets.

---

# Special Characters

## Level 1 — Fundamentals

* SC1. Extract whitespace.
* SC2. Remove extra whitespace.
* SC3. Match words.
* SC4. Match non-word characters.
* SC5. Extract punctuation.

## Level 2 — Intermediate

* SC6. Normalize multiple spaces.
* SC7. Extract newline-separated records.
* SC8. Remove tabs and newlines.
* SC9. Match escaped characters.
* SC10. Clean noisy text.

---

# Quantifiers

## Level 1 — Fundamentals

* Q1. Match repeated digits.
* Q2. Match repeated alphabets.
* Q3. Match optional characters.
* Q4. Match exactly n characters.
* Q5. Match between n and m characters.

## Level 2 — Intermediate

* Q6. Match one or more occurrences.
* Q7. Match zero or more occurrences.
* Q8. Compare greedy and non-greedy matching.
* Q9. Extract repeated words.
* Q10. Validate repeated character patterns.

---

# Anchors

## Level 1 — Fundamentals

* A1. Check whether a string starts with a word.
* A2. Check whether a string ends with a word.
* A3. Validate an exact string.
* A4. Match complete lines.
* A5. Match words at boundaries.

## Level 2 — Intermediate

* A6. Extract first word from each line.
* A7. Extract last word from each line.
* A8. Validate line-based records.
* A9. Match standalone words only.
* A10. Exclude partial word matches.

---

# Groups

## Level 1 — Fundamentals

* G1. Extract first and last names.
* G2. Extract area code from phone numbers.
* G3. Extract username from email.
* G4. Extract file extension.
* G5. Extract date components.

## Level 2 — Intermediate

* G6. Rearrange names using groups.
* G7. Replace captured groups.
* G8. Extract nested groups.
* G9. Use named groups.
* G10. Parse structured records.

---

# Alternation

## Level 1 — Fundamentals

* ALT1. Match one of several words.
* ALT2. Match different file extensions.
* ALT3. Match multiple date formats.
* ALT4. Match different separators.
* ALT5. Match multiple keywords.

## Level 2 — Intermediate

* ALT6. Validate multiple acceptable formats.
* ALT7. Match alternative prefixes.
* ALT8. Extract alternative patterns.

---

# Backreferences

## Level 1 — Fundamentals

* BR1. Detect repeated words.
* BR2. Detect repeated characters.
* BR3. Remove duplicate consecutive words.
* BR4. Match repeated groups.
* BR5. Validate mirrored patterns.

## Level 2 — Intermediate

* BR6. Validate repeated HTML tags.
* BR7. Match paired delimiters.
* BR8. Replace duplicate groups.

---

# Lookarounds

## Level 1 — Fundamentals

* LA1. Match words followed by digits.
* LA2. Match digits followed by words.
* LA3. Match words not followed by punctuation.
* LA4. Match digits not preceded by currency symbols.
* LA5. Extract values without delimiters.

## Level 2 — Intermediate

* LA6. Password validation using lookarounds.
* LA7. Extract values between delimiters.
* LA8. Validate context-dependent patterns.
* LA9. Match overlapping patterns.
* LA10. Extract embedded identifiers.

---

# Python re Module

## Level 1 — Fundamentals

* RE1. Use search() to find a pattern.
* RE2. Use match() for prefix matching.
* RE3. Use fullmatch() for validation.
* RE4. Use findall() to extract matches.
* RE5. Use finditer() to iterate through matches.

## Level 2 — Intermediate

* RE6. Replace text using sub().
* RE7. Count replacements using subn().
* RE8. Split text using split().
* RE9. Improve performance using compile().
* RE10. Escape special characters.

---

# Real-World Validation Problems

## Level 1 — Fundamentals

* RV1. Validate an email address.
* RV2. Validate a phone number.
* RV3. Validate a URL.
* RV4. Validate a PIN code.
* RV5. Validate a date.

## Level 2 — Intermediate

* RV6. Validate an IPv4 address.
* RV7. Validate a PAN number.
* RV8. Validate a password.
* RV9. Extract hashtags.
* RV10. Extract mentions.

## Level 3 — Advanced

* RV11. Parse log files.
* RV12. Extract timestamps.
* RV13. Remove HTML tags.
* RV14. Extract HTML attributes.
* RV15. Extract key-value pairs from configuration files.