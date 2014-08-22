def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    d = {
            '[ADJ]': listOfAdjs,
            '[VERB]': listOfVerbs,
            '[NOUN]': listOfNouns
            }
    words = story.split()
    new_words = []
    for word in words:
        for k in d:
            if word in d[k]:
                new_words.append(k)
                break
        else:
            new_words.append(word)

    return ' '.join(new_words)
