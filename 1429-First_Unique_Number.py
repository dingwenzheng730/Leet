'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

Precondition: can be empty
C1: [] showfirstunique() -> -1
C2: one element -> return this element

Input: [1, 2, 1, 3, 4]
Output: 2

Input: [1, 1, 2, 2, 3, 3]
Outpu: -1

dict: num to whether unique
queue: all unique elements in order
'''
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque([])
        self.is_unique = {}
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while self.queue and not self.is_unique[self.queue[0]]:
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.queue.append(value)
        else:
            self.is_unique[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

