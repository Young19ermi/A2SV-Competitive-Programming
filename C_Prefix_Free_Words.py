
class TrieNode:
    def __init__(self):
        self.case = [None, None]
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, length):
        stack, trie = [], self.root 
        res = []
        for i in range(length):
            stack.append(trie) 
            
            if trie.case[0] is None or not trie.case[0].is_end:
                if trie.case[0] is None:
                    trie.case[0] = TrieNode()
                trie = trie.case[0]
                res.append('0')




            elif trie.case[1] is None or not trie.case[1].is_end:
                if trie.case[1] is None:
                    trie.case[1] = TrieNode()
                trie = trie.case[1]
                res.append('1')
                
            else:
                return 

        
        trie.is_end = True
        
        while stack and stack[-1].case[1] and stack[-1].case[1].is_end:
            prev = stack.pop()
            prev.is_end = True

        return ''.join(res)



















def main():
    n = int(input())    
    nums = sorted(zip(map(int, input().split()), range(n)))
    trie = Trie()
    words = [''] * n
    for num, indx in nums:
        word = trie.insert(num)
        if not word:
            print('NO')
            return
        words[indx] = word

    print('YES')
    for word in words:
        print(word)



if __name__ == '__main__':
    main()


