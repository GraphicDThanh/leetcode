class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        # carry wil have when the last item is 9
        carry, i = 1, length - 1
        
        # assume always have carry
        while carry:
            # still in the list
            if i > -1:
                value = digits[i]
            
                if value == 9:
                    # only kep the loop if have carry
                    digits[i] = 0
                else:
                    # value is not 9 then 
                    # - increase value to 1
                    # - update carry to 0
                    # quit the loop since no carry
                    digits[i] += 1
                    carry = 0
                    
            else:
                # out of element
                # add 1 to top of list
                # reset carry to 0 to quit the loop
                digits = [1] + digits
                carry = 0
                
            i -= 1
            
        return digits
            