class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [t for t,f in Counter(s[i:i+10] for i in range(len(s)-9)).items() if f>1]