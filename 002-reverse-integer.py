class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list = [int(y) for y in str(x) if str(y).isdigit()]
        list.reverse()
        if x < 0:
            number = -(int(''.join(str(i) for i in list)))
        else:
            number = (int(''.join(str(i) for i in list)))
        if number > 2**31-1 or number < -2**31:
            return 0
        else:
            return number
        
solution=Solution()
print(solution.reverse(1534236461))