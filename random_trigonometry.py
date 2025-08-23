# This code randomly selects 10 trigonometry questions, then uses a loop and list 
# system to automatically solve all the questions and present them systematically.

import math
import random

questions = []
for _ in range(10):
    q_type = random.choice(["opposite", "adjacent", "hypotenuse"])  # random selection
    if q_type == "opposite":
        value = random.uniform(3, 20)  # random decimal
        angle = random.randint(10, 80)  # random integer angle
    elif q_type == "adjacent":
        value = random.uniform(3, 20)
        angle = random.randint(10, 80)
    else:
        value = random.uniform(5, 25)
        angle = random.randint(10, 80)
    questions.append({"type": q_type, "value": value, "angle": angle})


def hypotenuse_from_opposite(opposite, angle):
    rad = math.radians(angle)
    return opposite / math.sin(rad)

def hypotenuse_from_adjacent(adjacent, angle):
    rad = math.radians(angle)
    return adjacent / math.cos(rad)

def opposite_and_adjacent(hypotenuse, angle):
    rad = math.radians(angle)
    opposite = math.sin(rad) * hypotenuse
    adjacent = math.cos(rad) * hypotenuse
    return opposite, adjacent

for i, question in enumerate(questions, start=1):
    if question["type"] == "opposite":
        hyp = hypotenuse_from_opposite(question["value"], question["angle"])
        print(f"{i}. Question -> Opposite={question['value']}, Angle={question['angle']}, Hypotenuse={hyp:.2f}")
    elif question["type"] == "adjacent":
        hyp = hypotenuse_from_adjacent(question["value"], question["angle"])
        print(f"{i}. Question -> Adjacent={question['value']}, Angle={question['angle']}, Hypotenuse={hyp:.2f}")
    else:
        opp, adj = opposite_and_adjacent(question["value"], question["angle"])
        print(f"{i}. Question -> Hypotenuse={question['value']}, Angle={question['angle']}, Opposite={opp:.2f}, Adjacent={adj:.2f}")
