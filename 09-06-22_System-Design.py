print("""System Design
- MENU -
`````````
Please choose one of the options below, and press enter.
1) On-Premise Software
2) SaaS
3) System Life Cycle
4) Functional Testing
""")

answer = "empty"
response = "not-there"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("""On-Premise Software is software that is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud. On-premises software is sometimes referred to as “shrinkwrap” software, and off-premises software is commonly called “software as a service” ("SaaS") or “cloud computing”.

On-premise software or systems typically require having on-staff IT professionals. If there is an issue that local staff can't solve, it may require remote access with the software/system provider, or may even require IT Support or a Software Engineer to travel to help resolve the issue. This can result in further expenses as well as lost time. For small companies, on-premise software or systems may have a lot of unexpected costs when issues occur. However, with SaaS, you may have additional costs too, such as legal costs related to contracts.""")
  elif(userchoice == "2"):
    print("""Software as a Service is a software licensing and delivery model in which software is licensed on a subscription basis and is centrally hosted. It is sometimes referred to as "on-demand software", and was formerly referred to as "software plus services" by Microsoft.

By 'centrally hosted', what we mean is that the software is not run on the local computer system, but instead uses the internet to connect to servers from the software manufacturer. It is on the software manufacturer's servers that the software is run, managed, and maintained. An everyday example would be Google Docs. An example in the business would be the widely used enterprise software by German software company SAP SE.

SaaS applications are also known as Web-based software, on-demand software and hosted software. The term "software as a service" (SaaS) is considered to be part of the nomenclature of cloud computing, along with infrastructure as a service (IaaS), platform as a service (PaaS), desktop as a service (DaaS), managed software as a service (MSaaS), mobile backend as a service (MBaaS), datacenter as a service (DCaaS), and information technology management as a service (ITMaaS). SaaS apps are typically accessed by users using a thin client, e.g. via a web browser.

It is not uncommon to see software that is installed locally, but also requires the internet for verification of licensing. What determines if a software is On-premises or is SaaS is based on where the processing to run the software predominately occurs. Please choose one of the options below for further elaboration.
    
    2a) Advantages
    2b) Disadvantages""")
    while (response == "not-there"):
      userchoice = input()
      response = "there"
    if(userchoice == "2a"):
      print("""Lower initial costs, likely faster implementation

Maintenance and updates by software manufacturer

No staff needed to maintain the system 

Software manufacturer likely provides more support

On-site natural disasters do not put data at risk""")
    elif(userchoice == "2b"):
      print("""Continued subscription fees may ultimately be more expensive than On-premises software or custom designed software for large companies

Potential data-risk from software manufacturer

Potential differing time zones, maintenance and support may not be at convenient times

Specialized or unusual needs of a specific client may not be a priority of the software manufacturer

Because host is not the user itself, user feedback is harder to get

System change may be required sooner than ideal if the service is discontinued, the company seeks new functionality that the manufacturer is not interested in adding, or the manufacturer goes out of business""")
    else:
      print("That's not one of the options, silly!")
      answer = "not-there"
  elif(userchoice == "3"):
    print("It requires 7 phases: planning, requirement analysis, design, implementation/coding, testing, deployment, and maintenance.")
  elif(userchoice == "4"):
    print("A type of testing that seeks to establish whether each application feature works as per the software requirements. You test for mainline functions, basic usability, accessibiliity, and error condition.")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
