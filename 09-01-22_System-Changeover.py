print("""System Changeover
- MENU -
`````````
Please choose one of the options below, and press enter.
1) System Changeover
2) Implementation Methods
3) Data Migration
4) Business M&A
""")

answer = "empty"
response = "not-there"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("A system changeover is the process used to switch from one system to another. The larger the environment, the more problematic and complicated a system changeover may be. Depending on the company or organization, a system changeover can result in significatn consequences (medical facilities, power plants, communication providers). For these reasons, there are a variety of strategies to facilitate system changeover. A system changeover can involve the entire system or just part of the company's operations. Planning should be done prior to implementation to attempt to reduce negative effects of the changeover.")
  elif(userchoice == "2"):
    print("""Differing implementation methods have differing trade-offs and risks, the 'best method' is always situationally dependent. Please choose one of the options below for further elaboration.
    
    2a) Parallel
    2b) Big Bang/Direct/Immediate
    2c) Pilot
    2d) Phased""")
    while (response == "not-there"):
      userchoice = input()
      response = "there"
    if(userchoice == "2a"):
      print("In this implementation method, both systems work in parallel for a short period of time. This method also allows measuring output of the new system before the older system is taken offline. If the new system's functionality is not satisfactory, the company can still rely on the old system while trying to iron out any issues with the new system. This method can be expensive and taxing, as you are running both systems at the same time. This may require additional computer or network resources, additional man hours, and financial expenses to keep both running at the same time. If the two systems are drastically different, this can be extremely ineffecient for however long the changeover takes.")
    elif(userchoice == "2b"):
      print("In this implementation method, as soon as preperations are made, one system is entirely discontinued, and the other brought online. This method is the least taxing on computer and network resources, but requires frontloading training prior to the changeover. Additionally, any data that needs to be transfered from one system to the other may need a tertiary system or external location while the changeover occurs.")
    elif(userchoice == "2c"):
      print("This implementation method has a smaller portion of an organization or company change to the new system, called the pilot group or pilot site. This is fairly common in larger organizations and companies that have multiple divisions or sites. This implementation method can allow time to test the new system and iron-out issues with lower risk before it is implemented to the whole organization. Once the new system is succesful for the pilot group, changeover method for the rest of the organization can be planned. The pilot group can serve as a model when the the new system is adopted.")
    elif(userchoice == "2d"):
      print("This implementation method sees the company or organization convert one module or part of the system at a time over a period of time. This may mean the new system and old system may need to be similar enough for data or processes to go back and forth between the two. Training time is extended and the process overall will generally take longer as each phase of the new system is implemented seperately. These phases of implementation may be based on certain processes or functions across the whole organization, or may be based around departments or teams within the organization.")
    else:
      print("That's not one of the options, silly!")
      answer = "not-there"
  elif(userchoice == "3"):
    print("""When implementing a new system, there is a good chance you will also have to account for needing to transfer data from one system to another. This may include changing formats, types of storage, and computer systems. Please choose one of the options below for further elaboration.
    
    3a) Phases in Data Migration
    3b) Issues in Data Migration""")
    while (response == "not-there"):
      userchoice = input()
      response = "there"
    if(userchoice == "3a"):
      print("""Data migration should go through a series of stages; Plan, Migrate, & Validate.

Plan: The planning process should include determining the requirement of the migration. Future environment, development, and documentation of migration plan should all be considered.

Migrate: During this phase, the plan is communicated, all needed software and hardware is otained, installed and configured, and the process of actual transference occurs.

Validate: In this phase, tests check that data is in the same state before and after the migration. It is recommended that tests are run pre-migration as well as post migration to have a benchmark prior to the process.""")
    elif(userchoice == "3b"):
      print("There may be complications in transfering, whether changing mediums, like going from paper files to digital ones. There may aslo be incompatibility of data types in digital formats, like data stored in pdfs to go into a csv spreadsheet format, or data stored in floats trying to be input into integer formats. Other issues may arise if the data migration process times out, fails, or encounters other errors. Incompatibilities may also occur if data is misinterpretted, which for example could occur if incoporating systems from other regions, for example if an intenrational system is expectating dates to be imported as dd/mm/yyyy instead of mm/dd/yyyy or is expecting remperature data in celsius instead of farenheit.")
    else:
      print("That's not one of the options, silly!")
      answer = "not-there"
  elif(userchoice == "4"):
    print("""When two or more business entities merge, whether an actual merger, or more of an acquisition, there will likely be changes to the systems as the two entities integrate into one. Please choose one of the options below for further elaboration.
    
    4a) Merger vs. Acquisition
    4b) System Integration following M&A""")
    while (response == "not-there"):
      userchoice = input()
      response = "there"
    if(userchoice == "4a"):
      print("Merging or acquiring may seek to reduce costs by controlling more of the process, reducing competition, or other factors. Ultimately, the merger should result in a competitive advantage for the new merged organization/company.")
    elif(userchoice == "4b"):
      print("""As a result of merging, related to systems, one of the following strategies for integration will be chosen:
Both systems may be kept, with development to have the same functionality. Running both systems in parallel has high maintance costs.

Both systems may be replaced with a new system. This may result in a new system that meets the new company/organization's needs better overall, but will have higher increased initial costs, including new training for all employees.

Select the best system components from each and merge them. This provides some familarity for original employees from both, but may result in a longer period to become adjusted to the entire system due to operating by habit in some parts instead of a total change.

Select the better of the two systems, and drop the other system entirely. Those use to the dropped system may show resistance to change, and there may be policy issues. However, those already familiar with the chosen system can be resources since they are already experienced with it.""")
    else:
      print("That's not one of the options, silly!")
      answer = "not-there"
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
