from question_model import Question
from data import question_data 
from quiz_brain import QuizzBrain

question_list = []

for one_question in question_data:
    question_t = one_question["text"]
    question_a = one_question["answer"]
    new_question = Question(question_t,question_a)
    question_list.append(new_question)
    
# print(question_list[0].text)
# print(question_list[0].answer)
quiz = QuizzBrain(question_list)
while quiz.has_questions():         # == True:
    quiz.next_question()
print("Dokončili ste kvíz")
print(f"Vaše celkové skóre je : {quiz.score} / {quiz.question_number}")