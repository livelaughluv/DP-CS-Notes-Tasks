print("""User Experience (UX Research)

- MENU -
````````
Please choose one of the options below, and press enter.

1) Wireframe
2) Mockup
3) Prototype
4) Complexity/Simplicity
5) Effectiveness
6) Efficiency
7) Error
8) Learnability
9) Memorability
10) Readability/Comprehensibility
11) Satisfaction
12) The Gestalt Principles
13) Acessability
14) Usability
""")

answer = "empty"

response = "not-there"


while (answer == "empty"):

 userchoice = input("please choose: ")
 answer = "chosen"

if(userchoice == "1"):
   print("a planning diagram to communicate the overall layout. the bones so it is like the html")
elif(userchoice == "2"):
  print("a planning illustration to communicate the final appearance. the pretty look so like css")
elif(userchoice == "3"):
  print("""
  - a planning tool to communicate the functionality
- finished version used for quality assurance before mass-production. 
- the functionality so like javascript """)
elif(userchoice == "4"):
  print("amount of effort to find a solution or get a result")
elif(userchoice == "5"):
  print("comparison of user performance against a predefined level.")
elif(userchoice == "6"):
  print("task completion time after the initial adjusting period")
elif(userchoice == "7"):
  print("number of errors, type of errors, and time needed to recover from errors")
elif(userchoice == "8"):
  print("Time used to accomplish tasks on the first use")
elif(userchoice == "9"):
  print("Time, number of button clicks, pages, and steps used by users when they return to the device after a period of not using it")
elif(userchoice == "10"):
  print("Ability to read the content at an effective and efficient speed")
elif(userchoice == "11"):
  print("Attitude of users toward the product after use")
elif(userchoice == "12"):
  print(""" Definition: principles/laws of human perception that describe how humans group similar elements, recognize patterns and simplify complex images when we perceive objects

Couple of Examples: 
  1.Closure (Reification): We prefer complete shapes, so we automatically fill in gaps between elements to perceive a complete image. That’s how we can see the whole first.
  2.Common Region: We group elements that are in the same closed region.
  3. Figure/Ground (Multi-stability): We dislike uncertainty, so we look for solid, stable items. Unless an image is ambiguous—like Rubin’s Vase, below—we see its foreground first.
  4. Proximity (Emergence): We group closer-together elements, separating them from those farther apart. 
""")
elif(userchoice == "13"):
  print("how usable is the item to specific people that could share a feature that would make it harder for it to work for them: reflection tech with poeple of color, people with disabilities, etc. ")
elif(userchoice == "14"):
  print("how usable is the technology overall baring minority groups")
  
else:
  print("That's not one of the options, silly!")
  answer = "empty"
