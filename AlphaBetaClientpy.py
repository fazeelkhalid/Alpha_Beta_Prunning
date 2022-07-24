import random


MAX = 100
MIN = 0
MaxShuffles = 8
PointToWin = 56


def alphaBetaPruning(randPointList, depth, alpha, beta, child, status: bool):
    if (depth == 3):
        return randPointList[child]

    if (not status):  # Min player
        winner = MAX
        for i in range(0, 2):
            val = alphaBetaPruning(
                randPointList, depth + 1, alpha, beta, child * 2 + i, True)
            winner = min(winner, val)
            beta = min(beta, winner)

            if (beta <= alpha):
                break

        return winner

    else:  # Max Player
        winner = MIN
        for i in range(0, 2):
            val = alphaBetaPruning(
                randPointList, depth + 1, alpha, beta, child * 2 + i, False)
            winner = max(winner, val)
            alpha = max(alpha, winner)

            if (beta <= alpha):
                break
        return winner


# take student id
print("Enter your student ID : ")
StudentId = input()
# generate MaxShuffles time random number between MIN and MAX
points = random.sample(range(MIN, MAX), MaxShuffles)
print("Generated 8 random points between the minimum and maximum point limits:", end=" ")
print(points)

print("Total points to win: ", end=" ")
print(PointToWin)


Winner = alphaBetaPruning(points, 0, MIN, MAX, 0, True)

print("Achieved point by applying alpha-beta pruning =", end=" ")
print(Winner)

if (Winner > PointToWin):
    print("Winner is Optimus Prime")
else:
    print("Winner is Megatron")

# Minimum points the Optimus Prime can  achieve from the game
# if length of student id is less than the 5 than we can't do this operation so

if(len(StudentId) >= 5):
    MIN = int(StudentId[4])
    PointToWin = StudentId[len(StudentId)-2:]
    MAX = PointToWin[1] + PointToWin[0]
    PointToWin = int(MAX)
    MAX = int(int(MAX) * 1.5)

    MaxShuffles = int(StudentId[3])
    print("\nAfter the shuffle: ")
    # generate MaxShuffles time random number between MIN and MAX
    points = random.sample(range(MIN, MAX), MaxShuffles)
    print("List of all points values from each shuffle: ", end=" ")
    print(points)
    print("The maximum value of all shuffles:", end=" ")
    print(max(points))

    print("Won ", end=" ")
    print(len(list(filter(lambda x: (x >= PointToWin), points))), end=" ")
    print(" times out of ", end=" ")
    print(len(points), end=" ")
    print(" number of shuffles ")
