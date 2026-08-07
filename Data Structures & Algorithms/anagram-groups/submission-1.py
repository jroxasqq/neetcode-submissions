class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each str, get dict(char : count) (O(m * n) space, O(m * n) time)
        char_count_checked = []
        for word in strs:
            char_count = dict()
            for letter in word:
                char_count[letter] = char_count.get(letter, 0) + 1
            char_count_checked.append([char_count, False])
        

        # for each dict, if not checked: loop through all following dicts
        # for anagrams to add to the sublist.

        # consider that a str in strs can only be in one output sublist, we only
        # need to check them once, hence O(m) time for the below nested for loop.
        sublists = []
        for i in range(len(strs)):
            sublist = []
            if char_count_checked[i][1]:
                continue
            for j in range(i, len(strs)):
                if char_count_checked[j][1]:
                    continue
                if char_count_checked[i][0] == char_count_checked[j][0]:
                    sublist.append(strs[j])
                    char_count_checked[j][1] = True
            
            if sublist:
                sublists.append(sublist)


        return sublists
