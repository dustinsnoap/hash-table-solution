# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# $%$Start
import string

english_frequency = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]

# Frequency Analysis

freq = {}
total_chars = 0
ciphertext = ""

# Count all the characters
with open('ciphertext.txt') as f:
    for line in f:
        for char in line:
            if char in string.ascii_uppercase:
                if char not in freq:
                    freq[char] = 0

                freq[char] += 1
                total_chars += 1

        ciphertext += line  # Save for decoding later

# Compute the percentage frequency. (Technically we don't need to do
# this because we're just going to sort it later, and we can do that by
# either frequency or total letter count.)
for c in freq:
    freq[c] /= total_chars
    freq[c] *= 100

# Sort by ascending frequency
freq_items = list(freq.items())

freq_items.sort(key=lambda e: e[1], reverse=True)

# Make the key
decode_key = {}

for i in range(26):
    decode_key[freq_items[i][0]] = english_frequency[i]

# Print the key
#print(decode_key)

# Decode the text
for c in ciphertext:
    if c in decode_key:
        print(decode_key[c], end="")
    else:
        print(c, end="")
# $%$End