print("""System testing
- MENU -
`````````
Please choose one of the options below, and press enter.
1) debugging
2) validation vs verification
3) testing & types of testing:
  3a. dry-run
  3b. functional
  3c. unit
  3d. integration
  3e. user acceptance
  3f. alpha
  3g. beta
4) types of data used in testing:
  4a. normal
  4b. at the limits
  4c. extreme
  4d. abnormal
""")

answer = "empty"
response = "not-there"

while (answer == "empty"):
  userchoice = input("please choose: ")
  answer = "chosen"
  
  if(userchoice == "1"):
    print("debugging: The systematic process of correcting (and finding) bugs or errors in a program")
  elif(userchoice == "2"):
    print("verification: the process of ensuring that the data input is the same as the original source data. A way of ensuring data verification is through double entry. and validation is the process of evaluating whether data input follows appropriate specifications and is within reasonable limits.")
    
  elif(userchoice == "3a"):
    print("dry-run test: a static test where the software or system is not actually run: when you manually move through the code with pen-and-paper, to determine the expected outcome when the code is executed.")
  elif(userchoice == "3b"):
    print("functional test: a dynamic test where the software or sytem is run, relates to testing individual commands, text input, menu functions, etc. For example, if try to take a photo on your phone's camera app, does it take a picture?")
  elif(userchoice == "3c"):
    print("unit test: relates to separately testing the individual components or parts of the system or software.")
  elif(userchoice == "3d"):
    print("integration test: where the components are testing together within the system or software to verify that everything works correctly with each other.")
  elif(userchoice == "3e"):
    print("user acceptance test: relates to determining if the system satisfies the customer's needs. This is usually done on-premise before the system or software is shipped or trasnfered to the customer. This is more common when a system or software is specifically designed for a specific client, and not a software provided for the general public. ")
  elif(userchoice == "3f"):
    print("alpha test: the software or system is released to those within the company or organization who are not specifically involved in the development or implementation of the product. For example, if you are a developer for Apple's Final Cut Pro software, when a new iPhone model is available, they may ask if you'd like one of the early models that's still in testing. This allows them to get feedback and testing data more similar to how actual customers would use the new phone model.")
  elif(userchoice == "3g"):
    print("beta test: the software system is available to the public (or a group consisting of the public). As this includes the actual public, this is the closest and most realistic testing data a company or organization can get before the product is fully available. At this point, the product should be very stable, and testing may be more related to any unusual cases where the system or software may interact in an unexpected way with other software or systems, or also as a stress test if the system or software has to connect to servers or other internet-based resources.")
  elif(userchoice == "4a"):
    print("normal data: data that passes all validity tests")
  elif(userchoice == "4b"):
    print("data at the limits: data at a threshold; the data is valid, but is at the edge of changing how the system responds, ex. is grade letter is in output and number is 89")
  elif(userchoice == "4c"):
    print("extreme data: data that is a valid type, but not within the acceptable range, for grades if it was 101 and max is 100")
  elif(userchoice == "4d"):
    print("abnormal data: data that is not a valid type")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
