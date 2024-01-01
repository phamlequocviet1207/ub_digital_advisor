def wordtoword(aWord):
    letters = ""
    numbers = ""
    aWord = aWord.rstrip(" ")
    for letter in aWord:
        if letter.isalpha():
            letters += letter
            
        elif letter.isdigit():
            numbers += letter
    letters =letters.upper()
    result = letters + " " + numbers
    return result
    
print(wordtoword("e"))