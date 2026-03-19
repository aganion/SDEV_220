"""
Alicia Ganion
M5_Program_Testing
March 18, 2026

My favorite PC game growing up was Nancy Drew. I used that as a springboard to
come up with this idea.

Essentially, we are trying to accuse a suspect. The user can accuse if the following occurs:
-User has at least three pieces of evidence AND uncovered a motive
OR
-User has caught them at the scene of the crime
"""

def accuse_suspect(num_evidence, motive, scene_of_crime):
    return(num_evidence >= 3 and motive) or scene_of_crime

