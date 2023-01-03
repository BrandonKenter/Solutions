class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("%")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "%":
                j += 1
            length = int(s[i:j])
            cur_s = s[j + 1 : j + 1 + length]
            res.append(cur_s)
            i = j + 1 + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))