import random
import os

def read_file(filename):
    with open(r"data\responses.txt", "r",) as file:
        content = file.read().replace("\n", ". ")
    return content

def read_book_file(filename):
    with open(r"data\book.txt", "r",) as file:
        content = file.read().replace("\n\n", " ")
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

def generate_message(chain):
    first_word = random.choice(list(chain.keys()))
    message = first_word.capitalize()
    count = 10
    while len(message.split(' ')) < count:
        if first_word.endswith((".", "\n")):
            return message[:-1]
            break
        next_word = random.choice(chain[first_word])
        first_word = next_word
        message += ' ' + next_word
    return message

def generate_book_message(chain):
    first_word = random.choice(list(chain.keys()))
    message = first_word.capitalize()
    count = random.randrange(0,10)
    while True:
        next_word = random.choice(chain[first_word])
        first_word = next_word
        message += ' ' + next_word

if __name__ == "__main__":
    content = read_file("book.txt")
    while input().lower() != "bye":
        chain = build_chain(content)
        print(generate_book_message(chain))