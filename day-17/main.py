class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1


user_1 = User(user_id="001", username="angela")

print(user_1.followers)

user_2 = User(user_id="002", username="tom")
print(user_2.followers)

user_2.follow(user_1)
print(user_2.followers)
print(user_1.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

