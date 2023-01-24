class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in range(n):
            left, right = 0, n - 1
            while left <= right:
                image[row][left], image[row][right] = image[row][right], image[row][left]
                if left == right:
                    image[row][left] = 1 - image[row][left]
                else:
                    image[row][left] = 1 - image[row][left]
                    image[row][right] = 1 - image[row][right]
                left += 1
                right -= 1
        return image