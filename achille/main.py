# # CASE WHERE ACHILLE OVERTAKE THE TURTLE
# # Define speed of Achille and the turtle by step
achille_speed = 1
turtle_speed = 0.5

# Initialise positions
turtle_position = 0
achille_position = 0

# Simulation loop
while achille_position < turtle_position :
    # Make achille and the turtle move in fonction of their speed
    achille_position += achille_speed
    turtle_position += turtle_speed

    # Show the positions step by step
    print(f"Achille position : {achille_position} meters")
    print(f"Turtle position : {turtle_position} meters")

# Verify who won the race
if achille_position > turtle_position:
    print("Achille has won the race !")
elif turtle_position > achille_position:
    print("The turtle won the race !")
else:
    print("It's a tie !")


# CASE WHERE ACHILLE NEVER GET TO THE TURTLE

def course_achille_tortue(speed_achille, speed_turtle, distance):
    position_achille = 0
    position_turtle = 5

    for i in range(distance):
        position_achille += speed_achille
        position_turtle += speed_turtle

        if position_achille >= position_turtle:
            position_achille = position_turtle - 1 # Prevent achille from overtake the turtle

        print(f"Étape {i+1}: Achille est à la position {position_achille}, Tortue est à la position {position_turtle}")

distance_course = 100 # Define the race's distance
vitesse_achille = 5
vitesse_tortue = 1

course_achille_tortue(vitesse_achille, vitesse_tortue, distance_course)