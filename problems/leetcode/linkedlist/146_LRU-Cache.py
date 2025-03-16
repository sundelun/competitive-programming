#代码来自0x3f，灵茶山艾府
# https://leetcode.cn/problems/lru-cache/
class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    # we need a hash table and a dummy node
    # the linked list have both directions
    def __init__(self, capacity: int):
        self.record = {}
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
    
    # get the node from hash table
    def getNode(self, key: int) -> Optional[Node]:
        if key not in self.record:
            return None
        # if the node is in hash table, we will make it to the end of linked list
        # mark it as just recently used
        node = self.record[key]
        self.remove(node)
        self.push(node)
        return node

    # get the key's corresponding node
    def get(self, key: int) -> int:
        node = self.getNode(key)
        return -1 if node is None else node.value

    # add/update they key's corresponding node
    def put(self, key: int, value: int) -> None:
        node = self.getNode(key)
        # if it is inside hashtable then we only need to change the value
        if node:
            node.value = value
            return
        # Otherwise first insert it into the linked list
        newnode = Node(key, value)
        self.record[key] = newnode
        self.push(newnode)
        # remove the least recently used
        if len(self.record) > self.capacity:
            delnode = self.dummy.next
            del self.record[delnode.key]
            self.remove(delnode)

    # remove the current node
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # we will be adding the node by pushing the node to the end of linked list
    # and also adjust dummy and original last's prev and next
    def push(self, node: Node) -> None:
        last = self.dummy.prev
        last.next = node
        node.prev = last
        node.next = self.dummy
        self.dummy.prev = node