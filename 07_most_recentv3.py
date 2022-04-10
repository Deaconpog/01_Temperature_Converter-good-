"""" Get data from user and store it in a list, then
display the most recent three entries nicely
Trial #3 - prints list in reverse order
(no need for extra code or importing extra libraries)
"""

# Set up empty list
all_calculations = []

# Get 5 items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# Show that everything made it to the list...
print()
print("*** The Entire Deque ***")
print(all_calculations)

print()

print("*** Most Recent Three ***")
# Prints items starting at the END of the list
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])
