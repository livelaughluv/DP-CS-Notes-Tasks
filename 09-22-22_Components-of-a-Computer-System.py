print("""Components of a Computer System
- MENU -
`````````
Please choose one of the terms below, and press enter for the definition.
1) Patches
2) Upgrades
3) Updates
4) Releases
5) Hardware
6) Software
7) Peripheral Devices
8) Computer Network
9) Human Resources
10) Dumb Terminal
11) Client
12) Thin Client
13) Thick Client
14) Zero Client
15) Email Server
16) Router
17) DNS Server
18) Firewall
19) Client-server
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("Patches are used by software companies to update applications by fixing known bugs and vulnerabilities. Be aware that patches may introduce new bugs.")
  elif(userchoice == "2"):
    print("Upgrades contain a novel function or characteristic, as well as cumulative bug fixes. Upgrades often require an additional purchase.")
  elif(userchoice == "3"):
    print("Updates improve a product in a minor way, adding some new functionality or fixing a bug. Updates are usually free. Updates may be obtained manually, or may also be automatic through an internet connection..")
  elif(userchoice == "4"):
    print("Releases are final, working versions of software applications. Prior to release, they should undergo alpha and beta testing. A release is a new product, or an upgraded product.")
  elif(userchoice == "5"):
    print("Hardware is the physical components of the system, including chips and processors.")
  elif(userchoice == "6"):
    print("Software is the set of instructions that make the computer system do something useful, called programs.")
  elif(userchoice == "7"):
    print("Peripheral devices are devices that are outside of the computer, which can be input devices, output devices, and storage devices. Input devices allow data to be transmitted ot the computer, such as a keyboard, mouse or a microphone. Output devices allow the computer processor to output information, such as headphones and speakers. Storage devices are any piece of hardware that can store data outside the processor.")
  elif(userchoice == "8"):
    print("A computer network is a set of computer systems that are interconnected and share resources, as well as data. For example: Local Area Network, Wide Area Network, etc. A network typically connects servers and clients together.")
  elif(userchoice == "9"):
    print("Human resources are the people who are part of (or could be part of) an organization, business, or economy.")
  elif(userchoice == "10"):
    print("A dumb terminal is ")
  elif(userchoice == "11"):
    print("A client is ")
  elif(userchoice == "12"):
    print("A thin client is ")
  elif(userchoice == "13"):
    print("A thick client is ")
  elif(userchoice == "14"):
    print("A zero client is ")
  elif(userchoice == "15"):
    print("An email server is ")
  elif(userchoice == "16"):
    print("A router is ")
  elif(userchoice == "17"):
    print("A DNS (Domain Name System) server is ")
  elif(userchoice == "18"):
    print("A firewall is a hardware or software network infrastructure that controls data flow access among network entities. The firewall is mainly used to offer protection and limit access to a network. The ideal firewall system configuration consists of hardware and software components.")
  elif(userchoice == "19"):
    print("A client-server is ")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
