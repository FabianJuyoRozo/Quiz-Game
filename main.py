from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [

]

for x in question_data:
    question_object = Question(q_text=x["question"], q_answer=x["correct_answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"You have complete the quiz, you got {quiz.score}/{len(question_bank)}")

