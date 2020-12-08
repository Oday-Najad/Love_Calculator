
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1=name1.lower()
name2=name2.lower()

both_names = name1+name2

t= both_names.count("t")
r= both_names.count("r")
u= both_names.count("u")
e= both_names.count("e")

true_occurance= t+r+u+e
true_occurance = str(true_occurance)

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

love_occurance = l+o+v+e
love_occurance = str(love_occurance)

result = true_occurance+love_occurance
result = int(result)

if result<10 or result>90:
  print(f"Your score is {result}, you go together like coke and mentos.")

elif result>=40 and result<=50:
  print(f"Your score is {result}, you are alright together.")

else:
  print(f"Your score is {result}.")
  
