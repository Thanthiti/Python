from data_17_2 import question_data
from question_model import question
from Quize import quize

question_bank = []

for data in question_data:

    new = question(data["text"], data["answer"])
    question_bank.append(new)

Q = quize(question_bank)
while Q.still_loop():
    Q.next_qusetion()


print(Q.score)
print(len(Q.question_list))
