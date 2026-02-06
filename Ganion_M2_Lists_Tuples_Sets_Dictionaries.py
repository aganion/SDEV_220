"""
Alicia Ganion
2/4/2026
M2: Lists, Tuples, Sets, and Dictionaries
"""

#8.4
things = ["mozzarella", "cinderella", "salmonella"]
print(things)
#8.5
things[1] = things[1].capitalize()
print(things)
#Yes, it did change the element in the list. That is why things printed as such. Also, lists are mutable.
#8.6
things[0] = things[0].upper()
print(things)
#8.7
del things[2]
print(things)
#8.10
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
#this looks different than the way you showed in class. for x in range() is kind of confusing for me.

#9.6
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": [],
        "emus": []
    },
    "plants": {},
    "other": {}
}
#9.7
print(life.keys())
#9.8
print(life["animals"])
#9.9
print(life["animals"]["cats"])
#9.10
squares = {x: x**2 for x in range(10)}
print(squares)
#9.11
odd = {x for x in range(10) if x % 2 == 1}
print(odd)
#9.14
titles = ["Creature of Habit", "Crewel Fate", "Sharks on a Plane"]
plots = ["A nun turns into a monster", "A haunted yarn shop", "Check your exits"]

movies = dict(zip(titles, plots))
print(movies)