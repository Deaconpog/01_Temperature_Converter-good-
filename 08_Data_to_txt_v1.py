# Source - https://www.quru99.com/reading-and-writing-files-in-python.html

# Data can be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# Assume valid data for now.
filename = input("Enter a Filename: ")

# Create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item)

# Close file
f.close()
