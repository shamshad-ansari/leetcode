class StreamChecker:

    def __init__(self, words: list[str]):
        self.trie = {}
        self.stream = deque([])
        self.max = max(len(word) for word in words)

        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        while len(self.stream) > self.max:
            self.stream.pop()

        node = self.trie
        for ch in self.stream:
            if '#' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '#' in node

    

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# {
#     e : {
#         d: {
#             c :{
#                 #: word
#             }
#         }
#     }
# }
