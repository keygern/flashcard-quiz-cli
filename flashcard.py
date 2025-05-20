class Flashcard:
    def __init__(self, prompt:str, answer:str):
        self.prompt = prompt
        self.answer = answer
    def ask(self):
        user_answer = input(self.prompt +'')
        return user_answer.strip().lower() == self.answer.strip().lower()

