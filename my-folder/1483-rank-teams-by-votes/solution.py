class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        #hashmap, every value in votes has a list value that has the placement votes for every voter. Then, we append the actual value to compare alphabetically. decrement values so the ones with higher votes appear first (sort in ascending order when negative)
        lenVotes = len(votes[0])
        hashVote = {v : [0] * lenVotes + [v] for v in votes[0]} # every character
        # {A: [0 0 0 'A'], B: []}
        for vote in votes:
            for i,v in enumerate(vote):
                hashVote[v][i] -= 1
        
        res = sorted(hashVote, key=hashVote.get)
        return "".join(res)




 
