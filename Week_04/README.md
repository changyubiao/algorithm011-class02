# 学习笔记

本周学习了二分查找算法 









## 二分查找 模板 


### 1. ⼆分搜索的经典写法


查找某个值是否在已经排好序的数组中，如果存在 返回 index,不存在返回 -1 


```python

from typing import List


class Solution:

    def binary_search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return  -1 

```


### 2. ⼆分搜索

查找某个值target 在排好序的数组中，寻找target第一次出现的位置，如果存在返回index，如果不存在返回-1 

```python
from typing import List

class Solution:
    # ⼆分查找第⼀个与 target 相等的元素，时间复杂度 O(logn)
    def search_first_equal_element(self, nums: List, target: int):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                #  nums[mid]  ==  target
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                high = mid - 1
        return -1
```



### 3. ⼆分搜索

查找某个值target 在排好序的数组中，寻找target最后一次出现的位置，如果存在返回index，如果不存在返回-1 


```python
from typing import List

class Solution03:
    # ⼆分查找第最后一个与 target 相等的元素，时间复杂度 O(logn)
    def search_last_equal_element(self, nums: List, target: int):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                #  nums[mid]  ==  target
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                low = mid + 1
        return -1
```



### 4. ⼆分搜索

⼆分查找第⼀个⼤于等于 target 的元素，如果存在返回index，如果不存在返回-1 
时间复杂度 O(logn)

```python

from typing import List

class Solution:
    # ⼆分查找第⼀个⼤于等于 target 的元素，时间复杂度 O(logn)
    def search_first_greater_element(self, nums: List, target: int):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] >= target:
                if mid == 0 or nums[mid - 1] < target:
                    # 找到第⼀个⼤于等于 target 的元素
                    return mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return -1
```



### 5. ⼆分搜索
⼆分查找最后⼀个⼩于等于 target 的元素，如果存在返回index，如果不存在返回-1 

时间复杂度 O(logn)

```python

from typing import List

class Solution:
    # ⼆分查找最后⼀个⼩于等于 target 的元素，时间复杂度 O(logn)
    def search_last_less_element(self, nums: List, target: int):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)
            # print(f"mid:{mid}, {nums[mid]}")
            if nums[mid] <= target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return -1
```


