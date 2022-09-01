print("""4th INDUSTRIAL REVOLUTION

The 4th Industrial Revolution is blah blah blah

- MENU -
`````````
Please choose one of the options below, and press enter.

1) Why are you here at school?
2) What is the purpose of school?
3) Are you getting out of it, what you should be getting out of it?
4) As technology has continually changed both culture and work, and new technologies are continually developed, there is alway new interest in how technology can work for us. What are your thoughts in response to this video? How might these new technologies affect education?
5) Have you discovered what you love?
6) Have you had the opportunity to grow in this area?
7) Was it at school? Or was it outside of school?
8) Do you think you will you have the opportunity to discover what you love, and become great at it after you finish your secondary education?
9) Should we change how our school systems work?
10) How would you want to change it?
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("I am here at school because I want to gain knowledge so that I may have a good career in later life. On a more basic level, attendance is mandatory.")
  elif(userchoice == "2"):
    print("The purpose of school is to educate young minds. It prepares students for life after school, in which they have to use their knowledge to get a good job and learn discipline.")
  elif(userchoice == "3"):
    print("I am getting information and life skills out of school. I am learning subject-specific knowledge  useful for my future career. I am also learning skills such as teamwork, organization, time management, and leadership, all of which will help me in later life.")
  elif(userchoice == "4"):
    print("In response to this video, my thoughts are that technology will be immensely beneficial. It is much more accurate and precise than humans, but there are most definitely drawbacks. I remember seeing a title in the video that read, “We Now Have an AI Therapist, and She’s Doing Her Job Better than Humans Can.” In this instance, a piece of technology is replacing a human and excelling, which is useful for the patients. However, if robots continue to be better than humans, humans might be replaced in most aspects of life. When that happens, thousands of people will lose their jobs and people lose interaction with other people on a daily basis.")
  elif(userchoice == "5"):
    print("Yes, I have discovered that I love aerospace engineering and rocketry. The subject fascinates me, but I have not encountered many opportunities to immerse myself in the topic at school.")
  elif(userchoice == "6"):
    print("I have had the opportunity to grow in this area, but it was not offered at school.")
  elif(userchoice == "7"):
    print("The opportunity was outside of school, and I had to go out of my way to discover it.")
  elif(userchoice == "8"):
    print("Absolutely! Many colleges offer aerospace engineering classes and as the career is in high demand, I am sure that I will be able to get an internship or co-op before finishing college.")
  elif(userchoice == "9"):
    print("I think that we should change our school systems to include more STEM opportunities.")
  elif(userchoice == "10"):
    print("The fine arts are fairly well offered in schools, but I have not yet found a school that offers year-round rocketry or engineering in any form, whether it be a class or a club.")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
