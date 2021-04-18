[336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

Explanation:

- Get a reversed list of words
- Find all permutation pairs by check each word with the reversed list
  - Same length: If word had reversed in the reversed list and they are not the same then they are a palindrome pair
  - Diff length: If not belong above case, there are 2 options could make palindrome:
    - Case 1: by appending the other word to the back of the given word
      - Lấy từ sau ra trước số từ theo thứ tự tăng dần từ 1 đến length của từ
        - sau đó kiểm tra phân đoạn này có phải là palindrome hay không. Nếu phải, tiếp tục kiểm tra phần còn lại của chữ có nằm trong reversed hay không
          -> nếu có thì có một palindrome pair là [word, reverse của phần còn lại]

        Ví dụ: có ['rui', 'ur'], khi ghép lại là 'ruiur' là một palidrome. reversed_list sẽ là ['iur', 'ru']
        - Step 1: phần lấy ra = 'i', phần còn lại: 'ru'
        - Step 2: 'i' là một palindrome, 'ru' nằm trong reversed list
        -> ['rui', 'ur'] là sẽ ghép được một palindrom
    - Case 2: by appending the other word to the front of the given word
      - Ngược lại case 1, thực hiện tách từ trước ra sau

Analysis:
- Time complexity:
- Space complexity:


Submission Detail
```
Status: Accepted
134 / 134 test cases passed.
Runtime: 4828 ms
Memory Usage: 15.3 MB
```


```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        all_palindrome_pairs = []

        # Step 1: reverse all words
        reversed_words = [self.reversed_word(word) for word in words]

        # Step 2: get all palindromes alternative the word and list reversed words
        for word in words:
            palindrome_pairs = self.find_palindromes_helper(word, words, reversed_words)
            all_palindrome_pairs += palindrome_pairs

        return all_palindrome_pairs

    def is_palidrome(self, word):
        return word == word[::-1] if word else False

    def reversed_word(self, word):
        return word[::-1]

    def find_palindromes_helper(self, word, words, reversed_words):
        """Find all palindromes alternative the word and list reversed words"""
        palindromes_indices = []

        # Case: word exist in reversed words list, same length
        if word in reversed_words:
            reversed_word = self.reversed_word(word)
            # Avoid case revered word and word is the same
            if reversed_word != word:
                palindromes_indices.append([
                    words.index(word),
                    words.index(reversed_word)
                ])


        # Case: two words not same length
        # by appending the other word to the back of the given word
        for i, letter in enumerate(word):
            taken_out_str = word[-(i+ 1):len(word)]
            remain_str = word[0:len(word)-(i+1)]
            if self.is_palidrome(taken_out_str) and remain_str in reversed_words:
                palindromes_indices.append([
                    words.index(remain_str + taken_out_str),
                    words.index(self.reversed_word(remain_str))
                ])

        # Case: two words not same length
        # by appending the other word to the front of the given word
        for i, letter in enumerate(word):
            taken_out_str = word[-len(word):(i+1)]
            remain_str = word[(i+1):len(word)]
            if self.is_palidrome(taken_out_str) and remain_str in reversed_words:
                palindromes_indices.append([
                    words.index(self.reversed_word(remain_str)),
                    words.index(taken_out_str + remain_str)
                ])

        return palindromes_indices

```

--- Below is TLE solution of hard one
*Issue: TLE*

Explanation:

- Step 1: get index list
- Step 2: find all permutations of index list with pair [a, b]
  - use solution in the medium one
- Step 3: check if concat string in permutations is palindrome pairs, if yes put to result
  - use solution in the easy one

Analysis:
- Time complexity:
- Space complexity:


Submission Detail
```
Status: Time Limit Exceeded
47 / 134 test cases passed.
```

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Step 1: get index list
        index_list = list(range(0, len(words)))

        # Step 2: find all permutations of index list with pair [a, b]
        # expect results: [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
        permutations = self.all_permutations_with_length(index_list, 2)

        # Step 3: check if concat string in permutations is palindrome pairs
        results = []
        for p in permutations:
            word = words[p[0]] + words[p[1]]
            # check is word is palindrome
            if self.is_palindrome(word):
                results.append(p)

        return results

    def all_permutations_with_length(self, index_list, length):
        # permutation = []
        results = []
        self.find_permutation([], index_list, results, length)
        return results

    def find_permutation(self, permutation, choices, results, length):
        for i, num in enumerate(choices):
            choices_copy = choices[::]
            permutation_copy = permutation[::]
            choices_copy.pop(i)
            permutation_copy.append(num)

            if len(permutation_copy) == length:
                results.append(permutation_copy)
            elif len(choices_copy) > 0:
                self.find_permutation(permutation_copy, choices_copy, results, length)

    def is_palindrome(self, word):
        return word == word[::-1]

```

> Make it shorter, and still TLE

Submission Detail
```
Status: Time Limit Exceeded
62 / 134 test cases passed.
```

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        index_list = list(range(0, len(words)))


        result_permutations_palindrome = []
        self.find_permutation(
            [], index_list,
            result_permutations_palindrome,
            2, words
        )

        return result_permutations_palindrome

    def find_permutation(
        self, permutation, choices,
        result_permutations_palindrome,
        length, words
    ):
        for i, num in enumerate(choices):
            choices_copy = choices[::]
            permutation_copy = permutation[::]
            choices_copy.pop(i)
            permutation_copy.append(num)

            if len(permutation_copy) == length:
                word = words[
                    permutation_copy[0]] + words[permutation_copy[1]
                ]
                if word == word[::-1]:
                    result_permutations_palindrome.append(permutation_copy)

            elif len(choices_copy) > 0:
                self.find_permutation(
                    permutation_copy,
                    choices_copy,
                    result_permutations_palindrome,
                    length,
                    words
                )
```
