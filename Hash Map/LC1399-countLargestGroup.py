class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(list)
        max_size = 0
        for i in range(1, n+1):
            cur_sum = 0
            cur_num = i
            while cur_num:
                digit = cur_num % 10
                cur_sum += digit
                cur_num //= 10
            groups[cur_sum].append(cur_num)
            max_size = max(max_size, len(groups[cur_sum]))
        
        count = 0
        for group_sum, group in groups.items():
            if len(group) == max_size:
                count += 1
        return count