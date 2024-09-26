import os
from colorama import Fore, Style

def displayMaze(maze):
    os.system('cls')
    print("\n")
    for i in range(len(maze)):
        for j in range(len(maze[0])-1):
            if maze[i][j] == "A":
                print(Fore.RED + "A" + Fore.RESET, end="")
            elif maze[i][j] == "B":
                print(Fore.GREEN + "B" + Fore.RESET, end="")
            else:
                print(Style.DIM + maze[i][j] + Style.RESET_ALL, end="")
        print()

# Open maze file
with open("maze.txt", "r") as maze_file:
    maze = maze_file.readlines()

# Find start position (A) and end position (B)
starting_position = None
end_position = None
for i in range(len(maze)):
    for j in range(len(maze[0]) - 1):
        if maze[i][j] == "A":
            starting_position = (i, j)
            print(f"Starting position found: {starting_position[0]}, {starting_position[1]}")
        if maze[i][j] == "B":
            end_position = (i, j)
            print(f"End position found: {end_position[0]}, {end_position[1]}")
            

if starting_position == None:
    print(Fore.RED + "No starting position found." + Fore.RESET)
    quit()
if end_position == None:
    print(Fore.RED + "No end position found." + Fore.RESET)
    quit()


# Convert maze string to 2D list
for i in range(len(maze)):
    maze[i] = list(maze[i])


# Game loop
current_position = starting_position
while current_position != end_position:
    displayMaze(maze)

    # Controls
    controller_input = input("Select a move (W, A, S, D): ").lower()
    while controller_input not in "wasd":
        controller_input = input("Select a move (W, A, S, D): ").lower()

    new_x, new_y = current_position

    if controller_input == "w":
        new_x -= 1

    elif controller_input == "a":
        new_y -= 1

    elif controller_input == "s":
        new_x += 1

    elif controller_input == "d":
        new_y += 1


    if maze[new_x][new_y] == "." or maze[new_x][new_y] == "B":

        # Set new position to "A" and set old position to "." (empty)
        maze[current_position[0]][current_position[1]] = "."
        maze[new_x][new_y] = "A"
        current_position = (new_x, new_y)

displayMaze(maze)
print(Fore.GREEN + "You Won!!!" + Style.RESET_ALL)
