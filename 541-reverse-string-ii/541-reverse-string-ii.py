class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result_s = ""
        index2k = []
        len_s = len(s)
        k_2 = 2 * k
        
        # Find list of index break by 2k
        for i in range(0, len_s + 1):
            if i % k_2 == 0:
                index2k.append(i)
            
        # Break s down to 2k, revert the first k and add to results
        len_2k = len(index2k)
        for key, value in enumerate(index2k):
            if key + 1 >= len_2k:
                k_2_s = s[index2k[key]:]
            else:
                k_2_s = s[index2k[key]:index2k[key+1]]

            reverse_k_s = k_2_s[0:k][::-1]
            result_s += reverse_k_s + k_2_s[k:]
            
        return result_s
