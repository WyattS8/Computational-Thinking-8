Skiing_points = 0
Snowbording_points = 0


answer = input("When playing non snow sports do you like A), sports that focus on upper body strength, or B) lower body? ")
if answer == "B":
    Skiing_points += 1
elif answer == "A":
    Snowbording_points += 1


answer = input("Do you like things that are, A) easier to learn but harder to master, or B) Harder to learn but easier to master? ")
if answer == "A":
    Skiing_points += 1
elif answer == "B":
    Snowbording_points += 1


answer = input("Do you prefer A) going faster in a straight line, or B) doing more turns? ")
if answer == "A":
    Skiing_points += 1
elif answer == "B":
    Snowbording_points += 1


answer = input("When you are stuck on flat snow would you rather A) walk, or B) keep going? ")
if answer == "A":
    Snowbording_points += 1
elif answer == "B":
    Skiing_points += 1


answer = input("Would you rather A) have verry uncomfortable boots, or B) have more comfortable boots? ")
if answer == "A":
    Skiing_points += 1
elif answer == "B":
    Snowbording_points += 1


# end of quiz:
if Snowbording_points > Skiing_points:
    print ("You are a snowborder person")
elif Skiing_points > Snowbording_points:
    print ("you are a skiier person")