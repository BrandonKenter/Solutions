class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        size = [1] * n

        def find(n):
            if par[n] == n:
                return n
            par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            if size[p1] < size[p2]:
                size[p2] += size[p1]
                par[p1] = p2
            else:
                size[p1] += size[p2]
                par[p2] = p1
        

        email_to_i = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in email_to_i:
                    union(i, email_to_i[email])
                else:
                    email_to_i[email] = i
        
        ans = [[entry[0]] for entry in accounts]

        emails = defaultdict(list)
        for email, i in email_to_i.items():
            parent = find(i)
            emails[parent].append(email)
        
        ans = []
        for i in range(n):
            account = [] 
            if not emails[i]:
                continue
            emails[i].sort()
            account = [accounts[i][0]] + emails[i]
            ans.append(account)
        return ans