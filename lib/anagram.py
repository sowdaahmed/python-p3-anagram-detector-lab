# your code goes here!
#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the original word's letters for comparison
        sorted_word = sorted(self.word.lower())
        # Collect matches
        matches = []

        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word.lower():
                matches.append(candidate)

        return matches

