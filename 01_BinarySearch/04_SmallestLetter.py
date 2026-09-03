class Solution:
    # https://leetcode.com/problems/find-smallest-letter-greater-than-target/
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start = 0
        end = len(letters) - 1

        while start<=end:
            mid = ((end-start)//2)+start

            if (target < letters[mid]):
                end = mid-1
            else:
                start = mid+1

        return letters[start % len(letters)]
    
if __name__ == "__main__":
    letters = ["c","f","f","f","j"]
    sl = Solution()
    print(sl.nextGreatestLetter(letters, "f"))