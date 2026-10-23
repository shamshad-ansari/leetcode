class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        result = []
        for i, word in enumerate(words):
            if word[0] in 'aeiouAEIOU':
                word = word + 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word = word + 'a' * (i+1)
            words[i] = word
        
        
        return ' '.join(words)