"""
    队列
"""
class QueueError(Exception):
    pass

#顺序队列
class SQueue:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []
    
    def in_queue(self, value):
        """
            默认表尾为入队,表头为出队
        """
        self._elems.append(value)

    def out_queue(self):
        """
            出队
        """
        if self.is_empty():
            raise QueueError("queue is empty")
        return self._elems.pop(0)
        
    def top_queue(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        return self._elems.pop[0]
        

#链式队列结点
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

#链式队列
class LQueue:
    def __init__(self):
        self.head = self.tail = Node(None)
        

    def is_empty(self):
        return self.head.next is None
    
    def in_queue(self,value):
        n = Node(value)
        self.tail.next = n
        self.tail = self.tail.next

    def out_queue(self):
        val = self.head.next.value
        self.head = self.head.next
        return val
    

if __name__ == "__main__":
    # q = SQueue()
    # for i in range(10):
    #     q.in_queue(i)

    # for i in range(11):
    #     try:
    #         print(q.out_queue())
    #     except QueueError:
    #         print("has empty")
    #         break

    lq = LQueue()
    print(lq.is_empty())
    for i in range(5):
        lq.in_queue(i)
    print(lq.is_empty())
    for i in range(5):
        print(lq.out_queue())
    print(lq.is_empty())