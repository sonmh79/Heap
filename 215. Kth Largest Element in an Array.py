class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    #My Solution
    #팀 소트 정렬
    #RT: 60MS / MU: 15.1 MB
        return sorted(nums)[-k]
    
    #heapq 모듈 이용
        heap = []
        #최소 힙이기 때문에 음수로 저장
        for n in nums:
            heapq.heappush(heap,-n)
        for _ in range(k):
            heapq.heappop(heap)
        
        # -붙여서 출력
        return - heapq.heappop(heap)
    
    #heapify이용
        heapq.heapify(num)
        
        for_ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    #nlargest
        #k번째 만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴
        return heapq.nlargest(k,nums)[-1]
