class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return (self.items == [])
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

def is_balanced(items):
    stack = Stack()
    open_brackets = "({["
    close_brackets = ")}]"
    for item in items:
        if item in open_brackets:
            stack.push(item)
        elif item in close_brackets:
            if stack.is_empty():
                return False
            if open_brackets.index(stack.peek()) != close_brackets.index(item):
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    items = "(((([{}]))))"
    # items2 = "[([])((([[[]]])))]{()}"
    # items3 = "{{[(])]}}"

    if is_balanced(items):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
