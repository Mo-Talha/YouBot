from random import choice
import sys
import language_check
tool = language_check.LanguageTool('en-UK')

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
    raw = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        raw += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    matches = tool.check(raw)
    output = language_check.correct(raw, matches)
    print("Parsed output:", output)

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def main(text):
    generateText(remove_non_ascii_1(text), 4, 80)
