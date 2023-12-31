from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []
for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    
    question_list.append(Question(q_text, q_answer))

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()