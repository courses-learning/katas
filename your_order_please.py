"""Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers."""


def order(sentence):

    sentence = sentence.split()
    output = []

    for i in range(len(sentence)):
        for word in sentence:
            if str(i+1) in word:
                output.append(word)

    return " ".join(output)
