# How many votes did you get?

my_votes = int(input("How many votes did you get in the election? "))

#  Total votes in the election

total_votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.

percentage_votes = (my_votes / total_votes) * 100

print(f"I received {my_votes / total_votes * 100}% of the total votes.")