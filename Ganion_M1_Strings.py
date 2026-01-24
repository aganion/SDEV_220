#A.Ganion SDEV 220 - January 23, 2026

#4.1
text_song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

fixed_song = text_song.replace("moray", "Moray")

#4.2
var_one = "roast beef"
var_two = "ham"
var_three = "head"
var_four = "clam"

poem = f"""My kitty cat likes {var_one},
My kitty cat likes {var_two},
My kitty cat fell on his {var_three},
And now thinks he's a {var_four}."""

#4.3
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""

#4.4
salutation = "Hello"
name = "Mariana"
product = "espresso machine"
amount = "$550"
verbed = "crashed"
room = "closet"
animals = "cats"
percent = "82"
spokesman = "Carly"
job_title = "Customer Support Assistant"

letter = f"""Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""

#4.5 using f-strings to print the winning names at the state fair

award_one = "prize duck"
award_two = "gourd"
award_three = "spitz"
name_one = "Boat"
name_two = "Horse"
name_three = "Train"

winner_one = f"The winner of the {award_one} is {name_one}y Mc{name_one}face."
winner_two = f"The winner of the {award_two} is {name_two}y Mc{name_two}face."
winner_three = f"The winner of the {award_three} is {name_three}y Mc{name_three}face"
