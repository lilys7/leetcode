class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        #n gives us the number of possible languages, arr languages length will be the num of ppl there are and each index (person) has a list of all the languages they know, friendships is array of array doubles symbolizing friendships between each user. 
        #hashmap w each user and list of their friends
        #{1:[4,2], 2:[1,3], 3:[4,2], 4:[1,3]}
        #{0:[2], 1:[1,3], 2:[1,2], 3:[3]}

        #{1:[1,2], 2:[0,2], 3:[1,3]} language: index person
        #do max people - max value length
        lang_set = [set(l) for l in languages]
        #identify the problem users (people who cannot communicate to each other)
        problem = set()
        #iterate through all in friendships
        for u, v in friendships:
            u_ind, v_ind = u - 1, v - 1 #cause 1 indexed
            if not lang_set[u_ind] & lang_set[v_ind]:
                problem.add(u_ind)
                problem.add(v_ind)
        #if the problem set is empty, all users can communicate
        if not problem:
            return 0
        
        #now we need to find the most frequent language
        langCount = [0] * (n+1)
        for user in problem:
            for lang in lang_set[user]:
                langCount[lang] += 1
        maxLang = max(langCount)
        return len(problem) - maxLang
        
        
        




