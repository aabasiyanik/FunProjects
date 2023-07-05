from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    
    question_list.append(Question(q_text, q_answer))

