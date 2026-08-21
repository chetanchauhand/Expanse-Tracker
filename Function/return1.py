# Write a function that takes string and return the count vowel and consonents 

def countvowcons(userInput):

    vowel = "aeiou , AEIOU"
    countVowel = 0
    countConsonent  = 0
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowel):
                countVowel+=1
            else:
                countConsonent+=1
    return countVowel , countConsonent
vowel , consonents = countvowcons("Raj Kushwaha")
print(vowel,consonents)