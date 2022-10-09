class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result_s = ""
        
        # indexed of 2k is the range from 0 to len s with step is 2k
        indexes_2k = list(range(0, len(s) + 1, 2 * k))
        len_indexes_2k = len(indexes_2k) 
        
        # Break s down to 2k, revert the first k and add to results
        for key, value in enumerate(indexes_2k):
            if key + 1 >= len_indexes_2k:
                chunk_2k = s[value:]
            else:
                chunk_2k = s[value:indexes_2k[key + 1]]

            reverse_chunk_k = chunk_2k[0:k][::-1]
            transfer_chunk_2k = reverse_chunk_k + chunk_2k[k:]
            
            result_s += transfer_chunk_2k
            
        return result_s
