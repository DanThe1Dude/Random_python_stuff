import random
import sys

from questions_queue import Questions_Queue

question_answer = {"a": "1", "b" : "2", "c": "3", "d" : "4", "e" : "5", "f" : "6", "g" : "7", "h" : "8", "i" : "9", "j" : "10", "k" : "11", "l" : "12", "m" : "13"}

Settings = {
    "Range": (0, len(question_answer)),
    "Case Sensetive": True,
    "Swapped": False,
    "Shuffled": False,
    "Skip keyword": "skip",
    "Exit keyword": "exit",
}


def main():
    swapped = Settings["Swapped"]
    skip_key_word = Settings["Skip keyword"]
    exit_key_word = Settings["Exit keyword"]
    items = list(question_answer.items())[Settings["Range"][0] : Settings["Range"][1]]
    questions = Questions_Queue()
    
    if Settings["Shuffled"]:
        random.shuffle(items)
    
    questions.add_questions(items)
    # print(f"items: {items}")
    while not questions.is_finished():
        question, answer = questions.next_question()
        # could impliment a looping feature,
        # possibly with more advanced features where incorrect questions are placed into the middle and correct ones are placed at the end.
        # although this would require linked lists to be implimented otherwise it would take O(n) but with linked lists it would be O(1)
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
            elif attempt == exit_key_word:
                sys.exit()
            else:
                print("incorrect. Try again.")
    print(questions)


main()
