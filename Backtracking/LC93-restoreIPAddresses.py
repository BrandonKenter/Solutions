class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        # Declare result collection
        res = []
        cur_ip = []

        def backtrack(i, dots):
            # Check if state is a solution
            # Add to solution because asked for ALL solutions
            if dots == 4 and i == len(s):
                cur_ip[-1] = cur_ip[-1][:-1]
                res.append("".join(cur_ip))
                return

            # Base case
            if dots > 4:
                return
            
            # Attempt to make a choice for every possible choice for the 
            # current position i in s
            for j in range(i, min(i + 3, len(s))):
                # Base case check if the state using this choice is valid
                # If this evaluates to False, we are pruning future unfruitful 
                # paths
                if (
                    int(s[i:j + 1]) < 256 and
                    (i == j or s[i] != '0')
                ):
                    # State for this choice is valid, so update state
                    cur_ip.append(s[i:j+1] + '.')
                    backtrack(j + 1, dots + 1)
                    # Clean up choice (backtrack)
                    cur_ip.pop()
        backtrack(0, 0)
        return res