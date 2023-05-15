"""
    linklist.py
    实现单链表的构建
"""
class Node:
    """
        节点数据
        将自定义的类视为节点的生成类,实例对象中包含数据部分和指向下一个节点的next
    """
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return ("节点%s,next指向"%self.value + str(self.next))

class LinkList:
    """
        思路: 单链表类,生成对象可以进行增删改查操作.具体操作通过调用具体方法实现
            
    """
    def __init__(self):
        """
            初始化链表,标记一个链表的开端,以便于获取后续的节点
        """
        self.head = Node(None)

    def init_list(self, list_):
        """
            将一个列表,导入到链表中
        """
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    def show_list(self):
        """
            遍历链表
        """
        p = self.head.next
        while p is not None:
            print(p.value, end = " ")
            p = p.next
        print("\n")

    def is_empty(self):
        """
            判断链表是否为空
        """
        # if self.head.next == None:
        #     return True
        # return False
        return False if self.head.next else True
    
    def clear(self):
        """
            清空链表
        """
        self.head.next = None
    
    def append(self, value):
        """
            尾部插入数据
        """
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)
   
    def head_insert(self, value):
        n = Node(value)
        n.next = self.head.next
        self.head.next = n

    def insert(self, index, value):
        """
            按照索引插入数据,默认链表的第一个数据位置索引为0, 当参赛index大于链表总长度时,默认数据追加在尾部
        """
        p = self.head
        for i in range(0,index): 
            if p.next is None:
                break
            p = p.next 
        n = Node(value)
        n.next = p.next
        p.next = n  

    def delete(self, index):
        """
            按照索引位置删除数据
        """
        if self.is_empty():
            return 0  #链表为空,没有可以删除的数据
        
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        if p.next is not None:
            p.next = p.next.next
            return 1
        else:
            return "索引越界"

    def remove(self, value):
        """
            删除链表中值为value的数据
        """
        p = self.head
        while p.next is not None:
            if p.next.value == value: 
                p.next = p.next.next
                return
            p = p.next
        else:
            raise ValueError("链表中不存在该数值")

    def get_data(self,index):
        """
            根据索引获取链表中的值
        """
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise ValueError("索引越界") 
            p = p.next

        return p.value

list01 = [0, 1, 5, 7, 100]
list02 = [3, 150, 151, 259, 261]

l01 = LinkList()
l01.init_list(list01)
l02 = LinkList()
l02.init_list(list02)
newlink = LinkList()

l01.show_list()
l02.show_list()

p01 = l01.head
p02 = l02.head.next

while True:
    if p02 is None:
        break
    if p01.next is None:
        p01.next = p02
        break
    if p01.next.value <= p02.value:
        p01 = p01.next
    else:
        temp = p01.next
        p01.next = p02
        p02 = temp
        p01 = p01.next
    
    
l01.show_list()    


