# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Filter words in word_list that are anagrams of self.word
        return [w for w in word_list if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower()]
