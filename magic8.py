import random

#takes user input and store user's name
name = input("Enter name: ")

#declare question variable
question = ""
#takes user input and stores user's question if question is blank it will ask again
while question == "":
    question = input("Please enter a \"Yes\" or \"No\" qustion you would like to ask the magic eight ball: ")

#declare the answer to the question
answer = ""

#generates random number
random_number = random.randint(1,9)
  
#outputs an answer to the question based on the random value
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful." 
else:
    print("Error!")
    print(random_number)

#prints user's name if provided and question
if name != "":
    print(name, "asks: ", question)
else:
    print("Question: ", question)

#prints 8-balls answer
print("Magic 8-Ball's answer: ", answer)