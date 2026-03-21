class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n+1):

            div_3 = i % 3 == 0
            div_5 = i % 5 == 0
            if div_3 and div_5:
                s = "FizzBuzz"
            elif div_3:
                s = "Fizz"
            elif div_5:
                s = "Buzz"
            else:
                s = str(i)
            answer.append(s)
        return answer


        
