class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
            count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

        if count_s1 == count_s2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            new_char = s2[r]
            count_s2[new_char] = 1 + count_s2.get(new_char, 0)

            old_char = s2[l]
            count_s2[old_char] -=1

            if count_s2[old_char] == 0:
                del count_s2[old_char]
            
            l+=1

            if count_s1 == count_s2:
                return True

        return False
 
        