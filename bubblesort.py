# -*- coding: utf-8 -*-
"""bubblesort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18wSLnMTpqk82OuTjuoPL39vrYUP4fXYI
"""

for i in range(23, 10, -1):
  print(i)

def bubblesort(nums) :
  for i in range(len(nums)-1, 0 , -1):
    for j in range(i):
      if nums[j]>nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
  return nums

nums = [5, 3, 8 , 6, 7, 2]

bubblesort(nums)

nums

