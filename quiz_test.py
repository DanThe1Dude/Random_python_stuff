import random
import sys

from questions_queue import Questions_Queue


question_answer = {"January" : "1", "February" : "2", "March" : "3", "April" : "4", "May" : "5", "June" : "6", "July" : "7", "August" : "8", "September" : "9", "October" : "10", "November" : "11", "December" : "12"}

Settings = {
    "Range": (0, len(question_answer)),
    "Case Sensitive": True,
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
