"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.
    >>> wf = WordFinder("words.txt")
    235886 words read
    >>> wf.random() in wf.words
    True
    >>> wf.random() in wf.words
    True
    >>> wf.random() in wf.words
    True
    """
    ...
    def __init__(self, path):
        """read dictionary and reports # items read."""
        
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    >>> swf = SpecialWordFinder("words.txt")
    235886 words read
    >>> swf.random() in swf.words
    True
    >>> swf.random() in swf.words
    True
    >>> swf.random() in swf.words
    True
    """
    ...
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
    def random(self):
        """Return random word."""
        return random.choice(self.words)
