"""
Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

Write a space.py program that helps Codey keep track of their target weight by:

Checks which number planet is equal to.
It should then compute their weight on the destination planet.
Here is the table of conversions:

#	Planet	Relative Gravity
1	Venus	0.91
2	Mars	0.38
3	Jupiter	2.34
4	Saturn	1.06
5	Uranus	0.92
6	Neptune	1.19 
"""

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

#stores planet names to a unique key
planetdict = {
    1: "Venus",
    2: "Mars",
    3: "Jupiter",
    4: "Saturn",
    5: "Uranus",
    6: "Neptune",
}
#weight of person
weight = 185
#planet number
planet = 6
#planet name
planetname = ""

#if statement checks for which planet the person is on and calculates there weight based on the planets gravity
if planet == 1:
  #gets planet name
  planetname = planetdict.get(1)
  #calculates the weight on the planet
  weight = weight * 0.91
  #prints your weight on the planet and rounds to 2 decimal points
  print("Your weight on", planetname, "is:", f'{weight: .2f}')

elif planet == 2:
  planetname = planetdict.get(2)
  weight = weight * 0.38
  print("Your weight on", planetname, "is:", f'{weight: .2f}')

elif planet == 3:
  planetname = planetdict.get(3)
  weight = weight * 2.34
  print("Your weight on", planetname, "is:", f'{weight: .2f}')
  
elif planet == 4:
  planetname = planetdict.get(4)
  weight = weight * 1.06
  print("Your weight on", planetname, "is:", f'{weight: .2f}')
  
elif planet == 5:
  planetname = planetdict.get(5)
  weight = weight * 0.92
  print("Your weight on", planetname, "is:", f'{weight: .2f}')

elif planet == 6:
  planetname = planetdict.get(6)
  weight = weight * 1.19
  print("Your weight on", planetname, "is:", f'{weight: .2f}')
else:
    print("Invalid Input")