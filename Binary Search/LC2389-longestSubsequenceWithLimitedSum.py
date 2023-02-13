# Template 2
# Find minimal k where isCondition(k) is True
# isCondition is "sums[mid] > query"
# F F T T T T T <- find first index that is TRUE
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sums, prev = [], 0
        for num in nums:
            sums.append(num + prev)
            prev += num
        
        answer = []
        for query in queries:
            # Left bound is len(nums), not len(nums) - 1 because our stop index
            # might be len(nums), which signifies that the entire array is
            # able to contribute to the longest subsequence without exceeding the
            # query value. 
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if sums[mid] > query:
                    right = mid
                else:
                    left = mid + 1
            # We do - 1 + 1 for clarity
            # - 1 is for accounting for our stop position in the binary search.
            # Our left ands at the leftmost position where sums[mid] > query is
            # True. So to get the position where sums[mid] <= query, we do left - 1. 
            # + 1 is for getting the subsequence lenght. If we are at index 1, 
            # the length of the subsequence is not 1, it's 2. So we add 1 to 1.
            answer.append(left - 1 + 1)
        return answer


# Template 1
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort because we can greedily get the longest subsequence by adding to
        # it starting from the smallest value to the highest value.
        # Make a sums array of the values up until each index so we can use this
        # for our binary search to determine if the sum of the elements up to each 
        # index is <= queries[i].
        nums.sort()
        sums, prev = [], 0
        for num in nums:
            sums.append(num + prev)
            prev += num
        
        # Binary search each query sum using the "less or equal" subpattern.
        # Starting idx at -1 is for the edge case where we never get a sum
        # that is less than queries[i]. This means idx will never be updated
        # and appending idx + 1 means we append 0, which is what we want when
        # we have a querie that is smaller than all of the elements in nums.
        answer = []
        for query in queries:
            idx, left, right = -1, 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                val = sums[mid]
                if val == query:
                    idx = mid
                    break
                elif val < query:
                    idx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(idx + 1)
        return answer
