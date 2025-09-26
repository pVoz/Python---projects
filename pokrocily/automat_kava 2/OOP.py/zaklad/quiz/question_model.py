from data import question_data

class Question:
    
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer



# q_2 = question_data[0]["text"],question_data[0]["answer"]
# print(q_2)
# q_1 = Question(question_data[1],question_data["answer"])

# q_1 = Question("Python vznikol v roku 1991","True")
# q_2 = Question("Operačný systém Linux bol založený Linusem Torvaldem","True")
# print(q_1.text)
# print(q_1.answer)
# print(q_2.text)
# print(q_2.answer)
