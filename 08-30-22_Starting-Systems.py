print("""Starting Systems
- MENU -
`````````
Please choose one of the options below, and press enter.
1) System
2) Legacy Systems
3) Planning
4) Feasibility
5) Change Management
6) Business Merger
7) Real World Example
8) Hypothetical Example
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("A system is a full IT system of all related parts, including the people and the immediate environment. The system may include training employees and/or users, as well as maintaining and protecting data or hardware.")
  elif(userchoice == "2"):
    print("Legacy systems are old and outdated computer systems. New systems replace legacy systems, but many companies still use legacy systems in tandem with new systems. ")
  elif(userchoice == "3"):
    print("Planning and implementing new systems involves discussing new hardware, changing potential locations of technology, new policies, new training and upskilling, and potentially hiring and firing employees as well.")
  elif(userchoice == "4"):
    print("A feasibility study is used to assess whether a proposed project should be undertaken and it does this by looking at feasibility in five specific areas, using the acronym TELOS. T stands for Technical feasibility, which looks at the hardware and software within an organization. E stands for Economic feasibility, which relates to money and the funds that have been allocated to the project. L stands for Legal feasibility, which is about the conficts between the proposed system and local laws and regulations. O stands for Operational feasibility, which relates to the people and the participants within the organization and their reaction to the change of systems. S stands for Schedule, which means the timing and implementation of the system.")
  elif(userchoice == "5"):
    print("Change management means shifting, hiring, or letting go employees or whole departments, or maybe changing a system's process or the work it does. It should maximize benefits and minimize negatives, for all stakeholders, including the employees.")
  elif(userchoice == "6"):
    print("A business merger is an aggreement that unites two existing companies into one new company.")
  elif(userchoice == "7"):
    print("The real world example is of a post office and how they handle reading terrible handwriting on envelopes.")
  elif(userchoice == "8"):
    print("An encyclopedia company currently uses door-to-door and person-to-person style salespersons to find potential customers and take orders. The orders are then taken to a company office and are then input by a secretary. The company has decided that the salespeople will instead input the orders themselves, using their own personal technology.")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
