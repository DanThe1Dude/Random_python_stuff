from my_queue import Queue
from node import Node

Question = tuple[str, str]


class Questions_Queue:
    def __init__(self) -> None:
        self._queue = Queue()
        self.correct : int = 0
        self.incorect : int = 0
        self.questions_num : int = 0

    def __repr__(self) -> str:
        return f"{self.correct}/{self.questions_num}"

    def add_question(self, question : Question) -> None:
        self._queue.add_to_head(Node(question))
        self.questions_num += 1

    def add_questions(self, questions : list[Question]) -> None:
        for question in questions:
            self.add_question(question)

    def next_question(self) -> Question:
        result = self._queue.pop_head()
        if result:
            return result
        else:
            raise TypeError("Queue contained something that wasn't valid format")

    def mark_correct(self) -> None:
        self.correct += 1

    def mark_incorrect(self) -> None:
        self.incorect += 1

    def is_finished(self):
        return self._queue.head is None
