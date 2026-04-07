class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap = {}

        #for string in strs:
            #sorted_string = "".join(sorted(string))
            #if sorted_string in hashmap:
                #hashmap[sorted_string].append(string)
            #else:
                #hashmap[sorted_string] = [string]

        #return list(hashmap.values())

        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
        return list(res.values())
