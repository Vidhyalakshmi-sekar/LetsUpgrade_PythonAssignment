import random

# getting maximum number of participants as input
max_participants = int(input("Please enter the maximum number of participants: "))

# Creating an empty list to add the participants
participants = []

for people in range(max_participants):
    participant = input("Please enter the participant: ")
    # adding participant to the participants list
    participants.append(participant)

# picking a random winner

winner = random.randint(0, max_participants - 1)
winner = participants[winner]
print("And the winner is: ", winner)
