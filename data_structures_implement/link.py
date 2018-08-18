# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

class Node:
    """
    链表中的节点
    """
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, next_node):
        self.next = next_node

class Link:
    """
    链表类
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def add(self, item):
        add_node = Node(item)
        add_node.set_next(self.head)
        self.head = add_node

    def remove(self, item):
        current = self.head
        previous = None
        is_found = False
        while not is_found and current:
            if current.get_data() == item:
                is_found = True
            else:
                previous = current
                current = current.get_next()
        if not is_found:
            #  链表中没有找到要删除的项
            return False
        if not previous:
            # 链表只有一个一个，且要被删除
            self.head = current.get_next()
        else:
            self.previous.set_next(current.get_next())
        return True

    def search(self, item):
        """
        查找某个值
        """
        current = self.head
        is_found = False
        while not is_found and current:
            if current.get_data() == item:
                is_found = True
            else:
                current = current.get_next()
        return is_found


    def show(self):
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()

if __name__ == "__main__":
    my_node = Node(1)
    print my_node.get_data(), my_node.get_next()

    my_link = Link()
    print my_link.is_empty()
    my_link.add(2)
    my_link.add(3)
    my_link.add(4)
    my_link.show()

    print my_link.remove(5)
    print my_link.remove(4)
    print my_link.remove(3)
    print my_link.remove(2)
    print my_link.remove(2)



