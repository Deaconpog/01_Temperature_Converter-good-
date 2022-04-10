"""" Get data from user and store it in a list, then
display the most recent three entries nicely
Trial #2 - uses a deque method no need for reverse ordering
"""

from collections import deque
calculations = deque()

# Get 5 items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")

    # Add item to start of 'list'
    calculations.appendleft(get_item)

# Show that everything made it to the list...
print()
print("*** The Entire Deque ***")
print(calculations)

print()

print("*** Most Recent Three ***")
for item in range(0, 3):
    print(calculations[item])
