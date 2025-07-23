class TrieNode:
    def __init__(self):
        self.children={}
        self.endString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            node = curr.children.get(ch)
            if not node:
                node = TrieNode()
                curr.children[ch] = node
            curr = node
        curr.endString = True
        print('Successfully inserted')

    def searchString(self , word):
        curr = self.root
        for ch in word:
            node = curr.children[ch]
            if not node:
                return False
            curr = node
        
        if curr.endString == True:
            return True
        return False

def deleteNode(root, word, index):
    if index == len(word):
        if root.endString:
            root.endString = False
            return len(root.children) == 0
        return False

    ch = word[index]
    curr = root.children.get(ch)

    if curr is None:
        return False 

    shouldDeleteChild = deleteNode(curr, word, index + 1)

    if shouldDeleteChild:
        del root.children[ch]
        return not root.endString and len(root.children) == 0

    return False
