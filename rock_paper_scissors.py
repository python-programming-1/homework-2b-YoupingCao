import random
user_score = 0
computer_score = 0
continued = True


while (continued):
  print("make a move! (r/s/p)")

  user_choice = input()
  computer_choice= random.choice(['r', 's', 'p'])

  if user_choice == 'r':
    if computer_choice == 'r':
      print("You chose rock and the computer chose rock. It is a tie")
    elif computer_choice == 's':
      print("You chose rock and the computer chose scissor. You win!")
      user_score = user_score + 1
    else:
      print("You chose rock and the computer chose paper.You lose!")
      computer_score = computer_score + 1
  elif user_choice == 's':
    if computer_choice == 's':
      print("You chose scissor and the computer chose scissor. It is a tie")
    elif computer_choice == 'p':
      print("You chose scissor and the computer chose paper. You win!")
      user_score = user_score + 1
    else:
      print("You chose scissor and the computer chose rock.You lose!")
      computer_score = computer_score + 1
  elif user_choice == 'p':
    if computer_choice == 'p':
      print("You chose paper and the computer chose paper. It is a tie")
    elif computer_choice == 'r':
      print("You chose paper and the computer chose rock. You win!")
      user_score = user_score + 1
    else:
      print("You chose paper and the computer chose scissor.You lose!")
      computer_score = computer_score + 1
  else:
    print("Invalid input, please try again")
    continue


  y_or_no = True
  while(y_or_no):
    print("Do you want to play again, y for yes, n for no, and sc for score?") ##y for yes and n for no, sc for score
    user_select = input()
    if (user_select == 'n'):
      print("Thanks bye")
      continued = False
      y_or_no = False
    elif(user_select =='y'):
      y_or_no = False
    elif(user_select == 'sc'):
      print("Human: " + str(user_score) + ", Computer: " + str(computer_score))
