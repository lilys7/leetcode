class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapping = defaultdict(list)
        for s in strs:
            sortStr = ''.join(sorted(s))
            print(sortStr)
            mapping[sortStr].append(s)
        return list(mapping.values())


