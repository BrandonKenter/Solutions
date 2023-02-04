class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            cur_word, cur_dist = q.popleft()
            if cur_word == endWord:
                return cur_dist

            for i in range(len(cur_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = cur_word[:i] + c + cur_word[i + 1:]
                    if new_word in word_set:
                        q.append((new_word, cur_dist + 1))
                        word_set.remove(new_word)
        return 0