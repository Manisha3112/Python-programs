# Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

# Rules for converting a word to pig latin are as follows:

# 1. If word starts with a consonant, move all continuous consonants at the beginning to the end
#    and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

# 2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

# You job is to write a program that takes a sentence from command line and convert that to pig latin and
# print it back to console in a loop (till you hit Ctrl+C).

# e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
# Note that punctuation and capitalization has to be preserved

# You must write helper sub routines to make your code easy to read and write.

# Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
# by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
# (first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
# final word too (Erethay)
sentence=input("ENTER A SENTENCE:")
split=sentence.split(" ")
for elements in split:
        punctuation=""
        if(elements[len(elements)-1] in [',','.']):
            punctuation=elements[len(elements)-1]
        elements=elements.replace(",","")
        elements=elements.replace(".","")
        lower=elements.lower()
        for i in range(len(lower)):
            if(lower[i]=='a' or lower[i]=='e' or lower[i]=='i' or lower[i]=='o' or lower[i]=='u'):
                index=i
                break
        temp_sentence=lower[index:len(lower)]+lower[0:index]+"ay"+punctuation
        if(elements[0].isupper()):
            temp_sentence=temp_sentence.capitalize()
        print(temp_sentence,end=" ")        