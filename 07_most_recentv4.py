"""" Get data from user and store it in a list, then
display the most recent three entries nicely
Final version based on trial #3
Adds break loop and checks for empty list
"""

# Set up empty list
all_calculations = []

# Get items of data and add to list
get_item = ""
while get_item != "zz":
    get_item = input("Enter an item: ")

    if get_item == "zz":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("No item in list")

else:

    # Show that everything made it to the list...
    print()
    print("*** The Full List ***")
    print(all_calculations)

    # Print items starting at the END of the list
    if len(all_calculations) >= 3:
        print("*** Most Recent Three ***")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("*** Items from Newest to Oldest ***")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) -
                                   all_calculations.index(item) - 1])
