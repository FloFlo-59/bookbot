def number_words(text):
    words = text.split()
    total_words = len(words)
    print (total_words, f"words found in the document")

def number_characters(text):
    list_characters = []
    for i in text:
        character = i.lower()
        list_characters.append(character)
        #print(list_characters)
    dictionnary ={item: list_characters.count(item) for item in set(list_characters)}
    print(dictionnary)