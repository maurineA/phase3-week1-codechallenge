def consonant_values (s):
    def sub_string(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)
    
    #remove vowels
    consonant_str = ''.join(char for char in s if char not in 'aeiou')

    #split into substring consonant
    consonant_substrings = consonant_str.split('a') 

    #calculate the consonant substring and maximum
    return max(sub_string(sub) for sub in consonant_substrings)

print(consonant_values("zodiacs"))
print(consonant_values("strength"))