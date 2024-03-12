#wap to check the occurence of vowels in a string, in python using Dictionary

word = input("Enter the word: ")
word = word.lower()
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for i in word:
    if i in vowel_counts:
        vowel_counts[i] += 1
for vowel, count in vowel_counts.items():

    print(f"Occurrence of {vowel}: {count}")


