import random
class FruitQuizz:
    def __init__(self):
        self.fruits = {"apple":"red", "banana" : "yellow" , "pear" : "green"}
    def Quizz (self):
        while (True):
            fruit,color = random.choice(list(self.fruits.items()))
            print("What is the color of an {}" .format(fruit))
            user_input = input ()
            if (user_input.lower()==color):
                print("correct answer")
            else:
                print("Incorrect answer")
            option = int (input("Enter 0 if you want to play again otherwse enter 1 "))
            if option: 
                break 
print("Welcome to the Fruit Quizz")
fq = FruitQuizz()
fq.Quizz()