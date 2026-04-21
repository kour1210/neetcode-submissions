class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashMap={}
        for ch in s:
            hashMap[ch]=hashMap.get(ch, 0)+1
        for ch in t:
            hashMap[ch]=hashMap.get(ch, 0)-1
        for val in hashMap.values():
            if val !=0:
                return False
        return True

        