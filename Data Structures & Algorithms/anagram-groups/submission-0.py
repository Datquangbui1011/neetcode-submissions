class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = defaultdict(list)
        for i in strs:
            string_sorted = ''.join(sorted(i))
            b[string_sorted].append(i)
            
        return list(b.values())
        