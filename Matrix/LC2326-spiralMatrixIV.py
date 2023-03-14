# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for c in range(n)] for r in range(m)]
        l, r, t, b = 0, n-1, 0, m-1

        cur = head
        while l <= r and t <= b:
            for i in range(l, r+1):
                mat[t][i] = cur.val
                if not cur.next: return mat
                cur = cur.next
            t += 1
            for i in range(t, b + 1):
                mat[i][r] = cur.val 
                if not cur.next: return mat
                cur = cur.next
            r -= 1

            if t > b or l > r:
                break

            for i in range(r, l - 1, -1):
                mat[b][i] = cur.val 
                if not cur.next: return mat
                cur = cur.next
            b -= 1
            for i in range(b, t - 1, -1):
                mat[i][l] = cur.val 
                if not cur.next: return mat
                cur = cur.next
            l += 1
        return mat
            