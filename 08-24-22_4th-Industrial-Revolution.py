print("""4th INDUSTRIAL REVOLUTION

The 4th Industrial Revolution is blah blah blah

- MENU -
`````````
Please choose one of the options below, and press enter.

1) Question and Answer 1
2) Question and Answer 2
3) Question and Answer 3
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("PROMPT 1")
  elif(userchoice == "2"):
    print("PROMPT 2")
  elif(userchoice == "3"):
    print("PROMPT 3")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
