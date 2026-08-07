class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each str, get dict(char : count) (O(m * n) space, O(m * n) time)
        # for each dict, not checked: loop through all dicts after for anagrams
        char_count_checked = []
        for word in strs:
            char_count = dict()
            for letter in word:
                char_count[letter] = char_count.get(letter, 0) + 1
            char_count_checked.append([char_count, False])
        

        result = []
        for i in range(len(strs)):
            anagrams = []
            if char_count_checked[i][1]:
                continue
            for j in range(i, len(strs)):
                if char_count_checked[j][1]:
                    continue
                if char_count_checked[i][0] == char_count_checked[j][0]:
                    anagrams.append(strs[j])
                    char_count_checked[j][1] = True
            
            if anagrams:
                result.append(anagrams)


        return result
