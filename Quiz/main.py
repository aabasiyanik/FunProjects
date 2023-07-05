from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

new_question = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    
    new_question.append(Question(q_text, q_answer))

