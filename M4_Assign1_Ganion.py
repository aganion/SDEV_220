"""
Alicia Ganion
M_4 Programming Assignment - Files and Text Files
March 1, 2026
"""

#17.4
mammoth = "ODE ON THE MAMMOTH CHEESE. Weight over seven thousand pounds. We have seen thee, queen of cheese, Lying quietly at your ease, Gently fanned by evening breeze, Thy fair form no flies dare seize. All gaily dressed soon you'll go To the great Provincial show, To be admired by many a beau In the city of Toronto. Cows numerous as a swarm of bees, Or as the leaves upon the trees, It did require to make thee please, And stand unrivalled, queen of cheese.[Pg 72] May you not receive a scar as We have heard that Mr. Harris Intends to send you off as far as The great world's show at Paris. Of the youth beware of these, For some of them might rudely squeeze And bite your cheek, then songs or glees We could not sing, oh! queen of cheese. We'rt thou suspended from balloon, You'd cast a shade even at noon, Folks would think it was the moon About to fall and crush them soon."

#17.5
import re
c_words = re.findall(r"\b[cC]\w*", mammoth)
print(c_words)

#17.6
four_c_words = re.findall(r"\b[cC]\w{3}\b", mammoth)
print(four_c_words)

#17.7
end_r_words = re.findall(r"\b\w*[rR]\b", mammoth)
print(end_r_words)

#17.8
three_vowels = re.findall(r"[aeiouAEIOU]{3}(?![aeiouAEIOU])", mammoth)
print(three_vowels)

#20.1
import os
current_files_directory = os.listdir(".")
print(current_files_directory)

#20.2
parent_files = os.listdir("..")
print(parent_files)

#20.3
test1 = "This is a test of the emergency text system"
with open("test.txt", "w") as f:
    f.write(test1)

#20.4
with open("test.txt", "r") as f:
    test2 = f.read()

print("Contents of test.txt are:", test2)
print("Are test1 and test2 the same?", test1 == test2)