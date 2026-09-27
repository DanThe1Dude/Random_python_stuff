import random

question_answer = {"a": "1", "b" : "2", "c": "3", "d" : "4", "e" : "5", "f" : "6", "g" : "7", "h" : "8", "i" : "9", "j" : "10", "k" : "11", "l" : "12", "m" : "13"}

Settings = {
    "Range" : 0,
    "Case Sensetive: " : True,
    "Swapped": False,
    "Shuffled" : False,
    "Skip keyword" : "skip",
}

def main():
    items = list(question_answer.items())
    if Settings["Shuffled"]:
        random.shuffle(items)
    #print(f"items: {items}")
    swapped = Settings["Swapped"]
    skip_key_word = Settings["Skip keyword"]
    for key, value in items:
        question = key
        answer = value
        if swapped:
            question, answer = answer, question
        while True:
            attempt = input(f"What is {question}? ")
            if attempt == answer:
                print("correct!")
                break
            elif attempt == skip_key_word:
                print(f"skipping. Answer was {answer}")
                break
            else:
                print("incorrect. Try again.")

main()