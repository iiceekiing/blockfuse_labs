# Using pop() to remove elements

colors = ["red", "green", "blue", "yellow"]
print("Original list:", colors)

# Remove last item
last_color = colors.pop()
print("After pop:", colors)
print("Popped item:", last_color)

# Remove at index
second_color = colors.pop(1)
print("After popping index 1:", colors)
print("Removed item:", second_color)

