#Magic8Ball.py
#Name: Connor Pell  
#Date: 9/7/2025
#Assignment: lab2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  answers = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
]

  print("Magic 8 Ball")
    #Prompt the user for their question.
  question = input("What would you like to ask the Magic 8 Ball?      ")
    #Answer question randomly with one of the options from your earlier list.
  if question:
    rand_answer = random.random() * len(answers)
    rand_answer = int(rand_answer)
    print(answers[rand_answer])
  else:
      print("The Magic 8 Ball heard no question, and produced no answers.")

if __name__ == '__main__':
  main()
