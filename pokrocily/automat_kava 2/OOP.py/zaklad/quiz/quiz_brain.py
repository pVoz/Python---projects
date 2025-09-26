from data import question_data
class QuizzBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_li = q_list
    
    def next_question(self):
        current_question = self.question_li[self.question_number] # tutok je objekt(1 otázka)
        self.question_number += 1
        user_answer = input(f"Otázka č. {self.question_number}: {current_question.text} (True/False): ")
        self.chceck_answer(user_answer,current_question.answer)
        return user_answer
    
    def chceck_answer(self,us_answer,correct_answer):
        if us_answer.lower() == correct_answer.lower():
            print("Uhádli ste! ")
            self.score += 1
        else:
            print("Zlá odpoveď")
        print(f"Správna odpoved je {correct_answer}")
        print(f"Vaše skóre je {self.score} / {self.question_number}")
                  
    def has_questions(self):
        if self.question_number < len(self.question_li):
            return True
        else:
            return False
        