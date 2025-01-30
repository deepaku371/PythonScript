# Creating and working with lists in Python

# Create a simple list of fruits
fruits = ["apple", "banana", "orange", "mango", "grape"]

print("Basic List Operations:")
print("Original list:", fruits)
print("First fruit:", fruits[0])  # Access first element
print("Last fruit:", fruits[-1])  # Access last element
print("List length:", len(fruits))  # Get list length

# Modifying lists
print("\nModifying Lists:")
fruits.append("kiwi")  # Add an item
print("After adding kiwi:", fruits)

fruits.remove("banana")  # Remove an item
print("After removing banana:", fruits)

fruits.insert(1, "pear")  # Insert at specific position
print("After inserting pear at position 1:", fruits)

# Slicing lists
print("\nList Slicing:")
print("First three fruits:", fruits[:3])  # First three elements
print("Last three fruits:", fruits[-3:])  # Last three elements

# List operations
print("\nList Operations:")
veggies = ["carrot", "potato"]
food = fruits + veggies  # Combining lists
print("Combined food list:", food)

# List methods
print("\nList Methods:")
food.sort()  # Sort the list
print("Sorted list:", food)

food.reverse()  # Reverse the list
print("Reversed list:", food)

# List comprehension example
print("\nList Comprehension:")
lengths = [len(item) for item in food]
print("Length of each food item:", lengths)

# Checking if item exists in list
print("\nChecking Items:")
print("Is 'apple' in the list?", "apple" in food)
print("Is 'pizza' in the list?", "pizza" in food)