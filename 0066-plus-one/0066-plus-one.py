class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits = [str(i) for i in digits]
        # digits = str(int(''.join(digits)) + 1)
        # return [int(i) for i in digits]
        
        length = len(digits)
        carry, i = 1, length - 1
        
        # assume always have carry
        while carry:
            # still in the list
            if i > -1:
                value = digits[i]
            
                if value == 9:
                    digits[i] = 0
                else:
                    # value is not 9 then update carry to 0
                    digits[i] += 1
                    carry = 0
                    
            else:
                # exist carry then appen 1 to top
                digits = [1] + digits
                carry = 0
                
            i -= 1
            
        return digits
            