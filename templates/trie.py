# question of #208
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
class Node:
    def __init__(self):
       self.son = dict()
       # mark how many number of elements end with the current Node
       self.cnt = 0
class Trie:
    def __init__(self):
        self.root = Node()

    # insert the word into trie
    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            # if not created we create a new son follow by character
            if s not in cur.son:
                cur.son[s] = Node()
            cur = cur.son[s]
        # mark the final character as last character
        cur.cnt += 1

    # return True if word is in trie otherwise return False
    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            # not inserted character then return False
            if s not in cur.son:
                return False
            cur = cur.son[s]
        # we only return True if the final character of word has exist
        # suppose we have inserted "apple" and now we search("app")
        # the expected should be False but if we don't check cur.cnt > 0 it would return True
        return True if cur.cnt > 0 else False

    # return True if we have a word start with prefix otherwise return False
    # same as search method except for last line
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.son:
                return False
            cur = cur.son[s]
        return True