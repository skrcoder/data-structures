# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

class HashTable:
    def __init__(self, size):
        self.elem = [None] * size
        self.count = size

    def hash(self, key):
        # 散列函数为求余法
        return key % self.count

    def insert_hash(self, key):
        address = self.hash(key)
        while self.elem[address]:
            # 线性探测法解决冲突
            address = (address + 1) % self.count
        self.elem[address] = key

    def search_hash(self, key):
        start = address = self.hash(key)
        while self.elem[address] != key:
            # 出现冲突
            address = (address + 1) % self.count
            if not self.elem[address] or address == start:
                # 没有找到或者回到循环到了最开始的地方
                return False
        return True

if __name__ == "__main__":
    hash_table = HashTable(12)
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    print "ori list:", list_a
    for i in list_a:
        hash_table.insert_hash(i)
    for i in hash_table.elem:
        if i:
            print i, hash_table.elem.index(i)
    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))
