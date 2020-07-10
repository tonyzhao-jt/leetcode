class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter *k] 
    
        delta = longer - shorter
        return [k * shorter + delta * i for i in range(k + 1)]


        