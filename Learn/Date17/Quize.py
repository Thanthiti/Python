class quize:
    def __init__(self, qusetion):

        self.num = 0
        self.question_list = qusetion
        self.score = 0
        pass

    def next_qusetion(self):

        current_question = self.question_list[self.num]
        self.num +=1
        answer = input(f"Q{self.num} : {current_question.quse} : (true/false) : ")
        self.check_answer(answer,current_question.ans)
        pass

    def still_loop(self):
        if(self.num < len(self.question_list)) :
            return True
        else:
            return False
        pass

    def check_answer(self,answer,correct):
        if answer.lower() == correct.lower():
           self.score+=1
        else:
            print("Wrong")

            
        pass

    
    pass
