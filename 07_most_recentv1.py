"""" Get data from user and store it in a list, then
display the most recent three entries nicely
Trial #1 - uses a list with reverse ordering
"""

# Set up empty list
all_calculations = []

# Get 5 items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)


all_calculations.reverse()

# Show that everything made it to the list...
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent Three ***")
for item in range(0, 3):
    print(all_calculations[item])
