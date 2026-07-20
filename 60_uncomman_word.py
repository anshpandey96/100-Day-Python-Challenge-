def uncommon_words(str1, str2):
    # Split both strings into sets of words
    set1 = set(str1.split())
    set2 = set(str2.split())
    
    # Find symmetric difference (words that are in one set but not both)
    uncommon = set1.symmetric_difference(set2)
    
    # Convert to list and return
    return list(uncommon)

# Example usage
string1 = "This is the first string"
string2 = "This is the second string"

result = uncommon_words(string1, string2)
print("Uncommon words:", result)