from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute froce;
        #Sort all string in aphabet as a key 
        #Then, compare to existing group, if group have a sort key add into the group
        #Otherwise create a new group


        # groups = {}
        # for s in strs:
        #     key = ''.join(sorted(s))

        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(s)
        # return list(groups.values())


        #Hash map:
        # Counting how many char exist in a strs, if it have a same number of count character, put it in the same group


        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] +=1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())





 