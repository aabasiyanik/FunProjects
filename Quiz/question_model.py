from data import question_data
import random
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

arr = []
random_num = random.randint(0,11)
while random_num in arr:
    random_num = random.randint(0,11)
arr.append(random_num)
question = question_data.pop(random_num)

new_question = Question(text=question['text'], answer=question['answer'])
print(new_question.answer)