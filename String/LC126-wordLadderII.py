class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        res = []
        q = deque([[beginWord]])
        while q:
            to_remove = set()
            for i in range(len(q)):
                cur_words_path = q.popleft()
                cur_word = cur_words_path[-1]
                if cur_word == endWord:
                    res.append(cur_words_path)

                for i in range(len(cur_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = cur_word[:i] + c + cur_word[i + 1:]
                        if new_word in word_set:
                            q.append(cur_words_path + [new_word])
                            to_remove.add(new_word)

            for word in to_remove:
                word_set.remove(word)
        return res