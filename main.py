from art import logo, vs
from game_data import data
import random

print(logo)
score = 0


def random_person():
    random_number = random.randint(0, 50)
    person = data[random_number]
    name = person['name']
    description = person['description']
    country = person['country']
    followers = person['follower_count']
    return name, description, country, followers


person_a = random_person()
a_name = person_a[0]
a_description = person_a[1]
a_country = person_a[2]
a_followers = person_a[3]

is_game_on = True
while is_game_on:
    person_b = random_person()
    b_name = person_b[0]
    b_description = person_b[1]
    b_country = person_b[2]
    b_followers = person_b[3]

    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
    print(vs)
    print(f"Compare B: {b_name}, a {b_description}, from {b_country}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
        if a_followers > b_followers:
            score += 1
            person_a = person_b
        else:
            print(f"wrong answer {b_name} has {b_followers}M follower that of {a_followers}M followers of {a_name}")
            print(f"your final score is {score}")
            is_game_on = False
    elif answer == "b":
        if b_followers > a_followers:
            score += 1
        else:
            print(f"wrong answer {a_name} has {a_followers}M follower that of {b_followers}M followers of {b_name}")
            print(f"your final score is {score}")
            is_game_on = False
