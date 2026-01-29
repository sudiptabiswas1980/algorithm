def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    s = s.lower()

    for c in s:
        if 'a' <= c <= 'z':
            if c in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print(f"Vowels: {vowels}, Consonants: {consonants}")
