import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Dodge the Asteroids!")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, -250)

# Create a list for asteroids
asteroids = []
num_asteroids = 10

# Function to create asteroids
def create_asteroid():
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color("gray")
    asteroid.penup()
    asteroid.speed(0)
    x = random.randint(-290, 290)
    asteroid.goto(x, 300)
    asteroids.append(asteroid)

# Create initial asteroids
for _ in range(num_asteroids):
    create_asteroid()

# Player movement
def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Game loop
while True:
    for asteroid in asteroids:
        # Move the asteroid down
        y = asteroid.ycor()
        y -= 5
        asteroid.sety(y)

        # Check for collision with the player
        if asteroid.distance(player) < 20:
            player.goto(0, -250)  # Reset player position
            for a in asteroids:
                a.hideturtle()  # Hide all asteroids
            asteroids.clear()  # Clear the list of asteroids
            print("Game Over! Resetting game...")
            # Create new asteroids
            for _ in range(num_asteroids):
                create_asteroid()

        # Respawn asteroids at the top
        if y < -300:
            x = random.randint(-290, 290)
            asteroid.goto(x, 300)

    screen.update()  # Update the screen
