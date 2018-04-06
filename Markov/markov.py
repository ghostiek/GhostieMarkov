import random
import os

def read_file(filename):
    with open(os.getcwd() + os.sep.join([os.sep + "data", "responses.txt"]), "r") as file:
        content = file.read().replace("\n", ". ")
    return content

def build_chain(content, chain={}):
    words = content.split(" ")
    index = 1
    for word in words[1:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain

def generate_message(user_message, chain):
    first_key = random.choice(user_message.content.split(' '))
    if first_key in chain:
        first_word = random.choice(list(chain[first_key]))
    else:
        first_word = random.choice(list(chain.keys()))
    message = first_word.capitalize()
    count = 20
    while len(message.split(' ')) < count:
        if first_word.endswith((".", "\n")):
            return message[:-1]
        next_word = random.choice(chain[first_word])
        first_word = next_word
        message += ' ' + next_word
    return message