# https://leetcode.com/problems/flood-fill/
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with newColor.
# Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

        color_to_replace = image[sr][sc]

        if color_to_replace == newColor:  # nothing to fill
            return image

        self.fillnum(image, sc, sr, newColor, color_to_replace)

        return image

    def fillnum(self, image, sc, sr, newColor, color_to_replace):

        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != color_to_replace:
            return

        image[sr][sc] = newColor

        self.fillnum(image, sc - 1, sr, newColor, color_to_replace)
        self.fillnum(image, sc + 1, sr, newColor, color_to_replace)
        self.fillnum(image, sc, sr - 1, newColor, color_to_replace)
        self.fillnum(image, sc, sr + 1, newColor, color_to_replace)


def main():


    Image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    sol = Solution()
    print(sol.floodFill(Image,sr,sc,newColor))

if __name__ == "__main__":
    main()