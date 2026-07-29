class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Hashmap to track the character frequencies in s & t
        #Start with sliding window the size of length t
        #Keep expanding the sliding window until the character frequencies in t are met
        #Once character frequencies are met, store the current length
        #Remove first char of curr str and try scooping it up later

        if t == "":
            return ""

        thash = {}
        for c in t:
            thash[c] = 1 + thash.get(c, 0)
        
        resultX = -1
        resultY = -1
        minL = float("infinity")

        for i in range(len(s)):
            counts = {}
            for j in range(i, len(s)):
                counts[s[j]] = 1 + counts.get(s[j], 0)

                b = True
                for c in thash:
                    if thash[c] > counts.get(c,0):
                        b = False
                        break

                if b == True:
                    if minL > (j - i + 1):
                        minL = j - i + 1
                        resultX = i
                        resultY = j

        if minL != float("infinity"):
            return s[resultX: resultY + 1]
        
        return ""
