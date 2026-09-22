class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common(k)
        res2 = []
        for lista in res:
            res2.append(lista[0])

        #print(res)
        return res2
