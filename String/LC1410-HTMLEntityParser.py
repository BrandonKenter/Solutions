class Solution:
    def entityParser(self, text: str) -> str:
        e = {"&quot;":"\"", "&apos;":"\'", "&amp;":"&", "&gt;":">", "&lt;":"<", "&frasl;":"/"}

        res = []
        i = j = 0
        while i < len(text):
            if text[i] != '&':
                res.append(text[i])
                i += 1
                j += 1
            else:
                if i < len(text) - 1 and text[i+1] != '&': # check that we don't have two '&' in a row
                    while j < len(text) and text[j] != ';':
                        j += 1
                    if text[i:j+1] in e:
                        res.append(e[text[i:j+1]])
                    else:
                        res.append(text[i:j+1])
                else:
                    res.append('&')
                j += 1
                i = j
        return "".join(res)
        