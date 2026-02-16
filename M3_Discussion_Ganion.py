"""
Alicia Ganion
M3_Discussion
"""

class User:
    def __init__(self, fname, lname, birthday, email):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.email = email

    def describe_user(self):
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"Birthday: {self.birthday}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello {self.fname}!")

user1 = User("Alicia", "Ganion", "April 2, 1994", "aganion@ivytech.edu")
user2 = User("Nancy", "Drew", "April, 28, 1930", "nancy.drew@nomail.com")
user3 = User("Diana", "Spencer", "July 1, 1964", "diana.spencer@nomail.com")
user4 = User("Sandra", "Oh", "July 20, 1971", "sandra.oh@nomail.com")
user5 = User("Jodie", "Comer", "March 11, 1993", "jodie.comer@nomail.com")

for user in [user1, user2, user3, user4, user5]:
    greeting = user.greet_user()
    describe_user = user.describe_user()