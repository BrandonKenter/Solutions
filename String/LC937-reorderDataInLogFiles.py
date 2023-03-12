class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key=lambda log: log.split()[0])     # when suffix is tie, sort by identifier
        letters.sort(key=lambda log: log.split()[1:])    # sorted by suffix
        result = letters + digits                            
        return result
        