
#alphabet trie 
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.words.append(word)
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_end























class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
            
        res = ''
        
        for word in words:
            if len(word) < len(res): continue
            cur = root
            for letter in word:
                cur = cur.children[letter]
                if not cur.end: break
                
            if cur.end and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res






















        #search suggestion
    class TrieNode:
        def __init__(self):
                self.is_end = False
                self.children = [ None for _ in range(26)]
                self.words = []
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            def insert(self,word):
                curr = self.root
                for letter in word:
                    index = ord(letter) - ord('a')
                    if curr.children[index] is None:
                        curr.children[index] = TrieNode()
                    curr = curr.children[index]
                    curr.words.append(word)
                
            def search(self,word):
                curr = self.root
                for letter in word:
                    index = ord(letter) - ord('a')
                    if curr.children[index] is None:
                        return False
                    curr = curr.children[index]
                return curr.words
        class Solution:
            def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
                root = Trie()
                for w in products:
                    root.insert(w)
                res = []
                for i in range(len(searchWord)):
                    temp = root.search(searchWord[:i+1])
                    print(temp)
                    if temp:
                        res.append(sorted(temp)[:3])
                    else:
                        res.append([])
                return res


































class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end_of_word = True

    def find_max_xor(self, num: int) -> int:
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            other_bit = 1 - bit
            if node.children[other_bit]:
                max_xor |= (1 << i)
                node = node.children[other_bit]
            else:
                node = node.children[bit]
        return max_xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.add(num)

        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, trie.find_max_xor(num))

    
    def solve(self, s:str)->None:
        trie = Trie()
        for i in range(len(s)):
            trie.add(ord(s[i]))
            max_xor = 0
        for j in range(i+1, len(s)):
            max_xor = max(max_xor, trie.find_max_xor(ord(s[j])))
            print(max_xor)
            