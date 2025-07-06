import random
from art import logo
from art import vs
from project_data import data
#-----------------------------------------#
def get_random_account():
  return random.choice(data)
#-----------------------------------------#
user_1=get_random_account()
user_2=get_random_account()
#-----------------------------------------#
def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"
#-----------------------------------------#
def follower_data(account):
  follower=account["follower_count"]
  return follower
#-----------------------------------------#
def game(user_1,user_2,cnt):
  print(logo)
  follower_1=follower_data(user_1)
  follower_2=follower_data(user_2)
  print(f"Compare A:{format_data(user_1)}")
  print(vs)
  print(f"Compare B:{format_data(user_2)}")
  answer=input("Who has more followers? Type 'A' or 'B':")
  if follower_1>follower_2:
    if answer=="A" or answer=="a":
      cnt+=1
      print(f"You're right! Current score: {cnt}.")
      user_1=user_2
      user_2=get_random_account()
      print(f"You're right! Current score: {cnt}.")
      return game(user_1,user_2,cnt)
    else:
      print(f"Sorry, that's wrong. Final score:{cnt}")
  else:
    if answer=="B" or answer=="b":
      cnt+=1
      print(f"You're right! Current score: {cnt}.")
      user_1=user_2
      user_2=get_random_account()
      print(f"You're right! Current score: {cnt}.")
      return game(user_1,user_2,cnt)
    else:
      print(f"Sorry, that's wrong. Final score:{cnt}")
#-----------------------------------------#
game(user_1,user_2,0)