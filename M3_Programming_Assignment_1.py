"""
Alicia Ganion
2/16/2026
SDEV 220
"""
from typing import OrderedDict


#10.1
def good():
    return ["Harry", "Ron", "Hermione"]

#10.2
def get_odds():
    for odd_num in range(1, 10, 2):
        yield odd_num
i = 0
for num in get_odds():
    i += 1
    if i == 3:
        print(num)

#10.3
def test(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

#10.4
class OopsException(Exception):
    pass
try:
    raise OopsException()
except OopsException:
    print("Caught an oops.")

#12.1
import zoo
zoo.hours()

#12.2
import zoo as menagerie
menagerie.hours()

#12.3
from zoo import hours
hours()

#12.4
from zoo import hours as info
info()

#12.5
plain = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(plain)

from collections import OrderedDict

fancy = OrderedDict(
    [
        ("a", 1),
        ("b", 2),
        ("c", 3),
    ]
)
print(fancy)