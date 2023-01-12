class Codec:
    def __init__(self):
        self.shortToLong = {}
        self.i = 0
        self.base = 'http://tinyurl.com/'
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = self.base + str(self.i)
        self.shortToLong[short] = longUrl
        self.i += 1
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))