class TrieNode:
    def __init__(self):
        self.children = [None,None]
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_xor = 0
        self.max_xor_node = None



def solve(self, s:str)->None:
        trie = Trie()
        for i in range(len(s)):
            trie.add(ord(s[i]))
            max_xor = 0
        for j in range(i+1, len(s)):
            max_xor = max(max_xor, trie.find_max_xor(ord(s[j])))
        return max_xor
