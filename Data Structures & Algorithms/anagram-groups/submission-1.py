class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute froce;
        #Sort all string in aphabet as a key 
        #Then, compare to existing group, if group have a sort key add into the group
        #Otherwise create a new group


        groups = {}
        for s in strs:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
 