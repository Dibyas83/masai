

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Example usage:
bricks = Stack()
bricks.push("Brick 1")
bricks.push("Brick 2")
bricks.push("Brick 3")

print("Top brick:", bricks.peek()) # Output: Brick 3
print("Stack size:", bricks.size()) # Output: 3

removed_brick = bricks.pop()
print("Removed brick:", removed_brick) # Output: Brick 3
print("Stack size after pop:", bricks.size()) # Output: 2

print("Is stack empty?", bricks.is_empty()) # Output: False

while not bricks.is_empty():
    print("Removed brick:", bricks.pop())
# Output:
# Removed brick: Brick 2
# Removed brick: Brick 1

print("Is stack empty?", bricks.is_empty()) # Output: True
print(bricks.pop()) # Output: Cannot pop from an empty stack









