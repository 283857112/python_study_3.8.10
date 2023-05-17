"""
    顺序存储栈的模型
    
"""
class StackError(Exception):
    """
        自定义栈异常
    """
    pass

#顺序栈
class SStack:
    """
        顺序栈,利用列表连续存储
    """

    def __init__(self):
        self._elems = []

    def is_empty(self):
        """
            判断栈是否为空
        """
        return self._elems == []

    def push(self,value):
        """
            入栈,默认self._elems尾部为栈顶
        """
        self._elems.append(value)

    def pop(self):
        """
            出栈
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems.pop()
    
    def top(self):
        """
            查看栈顶元素    
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]

#链表结点
class Node:
    """
        节点数据
        将自定义的类视为节点的生成类,实例对象中包含数据部分和指向下一个节点的next
    """
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
#链表栈,非连续性存储
class LStack:
    def __init__(self):
        self._top = None

    def is_empyt(self):
        """
            判断是否为空
        """
        return self._top is None
    
    def push(self,value):
        """
            入栈
        """
        n = Node(value)
        n.next = self._top
        self._top = n
        # self._top = Node(value, self._top)
    def pop(self):
        """
            出栈
        """
        if self.is_empyt():
            raise("Stack is empty")
        value = self._top.value
        self._top = self._top.next
        return value
    
    def top(self):
        if not self.is_empyt():
            return self._top.value
"""
### 栈的应用,逆波兰表达式
s = SStack()
while True:
    str_ = input("please input:")
    if str_ == "":
        break
    
    str_list =str_.split(" ")
    for item in str_list:
        if item not in ("+", "-", "*", "/","p"):
            s.push(item)
        elif item in ("+", "-", "*", "/"):
            data1 = s.pop()
            data2 = s.pop() 
            re = eval("%s%s%s"%(data2,item,data1))
            s.push(re)
        elif item == "p":
            print(s.top())
"""
