"""
You are playing the following Nim Game with your friend:
    There is a heap of stones on the table,
    each time one of you take turns to remove 1 to 3 stones.
    The one who removes the last stone will be the winner.
    You will take the first turn to remove the stones.

    Both of you are very clever and have optimal strategies for the game.
    Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
"""


class Solution(object):

    def canWinNim(self, n):
        if n >= 4:
            result = n % 4
            if result == 0:
                return False
            else:
                return True
        return True

game = Solution()

print(game.canWinNim(1))
print(game.canWinNim(2))
print(game.canWinNim(3))
print(game.canWinNim(4))
print(game.canWinNim(5))
print(game.canWinNim(6))
print(game.canWinNim(7))
print(game.canWinNim(8))
print(game.canWinNim(125))
print(game.canWinNim(1404))
print(game.canWinNim(1523))

