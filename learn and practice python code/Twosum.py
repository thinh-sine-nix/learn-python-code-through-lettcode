from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}
            for index, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                    return [seen[complement], index]
                seen[num] = index
                
if __name__ == "__main__":

  def get_input():
    while True:
      try:
        nums_str = input(
            "Enter the list of numbers (comma-separated, e.g., 2,7,11,15): ")
        nums = [int(x.strip()) for x in nums_str.split(',')]
        if len(nums) < 2:
          print("Error: Please enter at least two numbers.")
          continue
        target = int(input("Enter the target integer: "))
        return nums, target
      except ValueError:
        print("Error: Invalid input. Please enter integers only.")

  nums, target = get_input()
  solution = Solution()
  result = solution.twoSum(nums, target)
  print(f"Indices of numbers that sum to {target}: {result}")