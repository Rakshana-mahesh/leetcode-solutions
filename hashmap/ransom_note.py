from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for letter, needed in note_count.items():
            if magazine_count[letter] < needed:
                return False
        
        return True