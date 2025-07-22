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

trie = Trie()
trie.insert("hello")
print(trie.root.children)