class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {"".join(sorted(s1)):1}
        l = 0
        r = l + len(s1)
        print(len(s1))
        print(s2[l:r])

        while r <= len(s2):
            print("s2", "".join(sorted(s2[l:r])))
            if "".join(sorted(s2[l:r])) in s1_map:
                return True
                
            l+=1
            r+=1

        return False

