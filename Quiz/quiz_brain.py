import random
class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
        q_list = random.shuffle(q_list)

    def next_question(self):
        qq_text = self.questions_list[self.question_number].text
        qq_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        is_Valid = True
        while is_Valid:
            user_answer = input(f"Q.{self.question_number}: {qq_text} (True/False)?: ")
            if user_answer.lower() not in ['true', 'false']:
                print("Please type in 'True' or 'False'")
            else:
                is_Valid = False

        self.check_answer(user_answer, qq_answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        if self.question_number == len(self.questions_list):
            print(f"You've completed the quiz\nYour final score was: {self.score}/{len(self.questions_list)} | {round((100*self.score)/len(self.questions_list), 2)}%")