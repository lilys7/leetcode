class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #loop thru all strs. have a hashmap of sets. If the ordered ver. of the word is equal to a prev ordered version, add to that set. otherwise add on its own.
        map = defaultdict(list) #sorted ver : actual word
        for s in strs:
            sort = sorted(s)
            sorted_str = "".join(sort)
            map[sorted_str].append(s)
        return map.values()


        
