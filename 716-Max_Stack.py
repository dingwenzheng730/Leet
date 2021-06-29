'''
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Precondition: pop empty?
'''
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            if x > self.stack[-1][1]:
                self.stack.append((x, x))
            else:
                self.stack.append((x, self.stack[-1][1]))
        else:
            self.stack.append((x,x))

    def pop(self) -> int:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        moved_items = []
        while self.stack[-1][0] != max_val:
            moved_items.append(self.stack.pop())
        self.stack.pop()
        while moved_items:
            self.push(moved_items.pop()[0])
        return max_val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()