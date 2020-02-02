""" Write a function that takes in a string of one or more words, and returns
the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of only
letters and spaces. Spaces will be included only when more than one word is
present."""

def spin_words(sentence):
    sentence = sentence.split()

    for i in range(len(sentence)):
        if len(sentence[i]) > 4:
            sentence[i] = sentence[i][::-1]


    sentence = " ".join(sentence)
    return sentence
