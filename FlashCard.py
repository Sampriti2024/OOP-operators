class FlashCard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+ "("+self.meaning+")"
    
Flash = []
print("WELCOME TO THE FLASHCARD APPLICATION")
while (True):
    word = input ("Enter the word")
    meaning = input ("Enter tyhe meaning")
    Flash.append (FlashCard(word,meaning))
    option = int (input("Enter 0, if you want to add another flashcard. Otherwise enter 1 ")) 
    if option:
        break
print("Your flashcard")
for i in Flash:
    print(">", i)
