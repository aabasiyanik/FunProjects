import random
class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.questions_list = q_list
        q_list = random.shuffle(q_list)

    def next_question(self):
        qq_text = self.questions_list[self.question_number].text
        qq_answer = self.questions_list[self.question_number].answer
        user_answer = input(f"Q.{self.question_number + 1}: {qq_text} (True/False)?: ")
        self.check_answer(user_answer, qq_answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")