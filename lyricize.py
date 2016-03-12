from random import choice
import sys

text = """
​
TEXT HERE
​
"""

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next_letter = text[i+order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print (output)

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])


if __name__ == "__main__":
    generateText(remove_non_ascii_1(text), int(sys.argv[1]), int(sys.argv[2]))