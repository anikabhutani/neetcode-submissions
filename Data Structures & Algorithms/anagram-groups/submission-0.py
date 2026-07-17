class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        setResult = {}
        for str in strs:
            sortedS = ''.join(sorted(str))
            if sortedS in setResult:
                setResult[sortedS].append(str)
            else:
                setResult[sortedS] = [str]
        
        return list(setResult.values())
        