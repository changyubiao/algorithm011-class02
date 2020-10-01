# 学习笔记
本周主要学习了一些 递归的套路,对递归有了一点点的理解,递归其实还是没有那么可怕, 

树的递归, 和泛型递归. 





## 总结
本周主要对 递归进行了一些练习 , 其实分支, 回溯 本质上来说 都是递归而已, 感觉差不多.








## 递归 模板

```python

def recursion(level, param1, param2, ...): 

    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
	   
    
    # 当前层 处理	   
    # process logic in current level 
    process(level, data...) 
    
    # drill down  到下一层 
    self.recursion(level + 1, p1, ...) 
    
    
    # 清理 一些变量 
    # reverse the current level status if needed
    pass
    
```


## 分治模板
```python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
    print_result
    return
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, …)
    # revert the current level states
```








## 实战题目

1. [leetcode_47 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number)
2. [leetcode_22 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
3. [leetcode_50 Pow(x, n)](https://leetcode-cn.com/problems/powx-n)
4. [leetcode_51  N皇后](https://leetcode-cn.com/problems/n-queens/)
5. [leetcode_70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
6. [78. 子集](https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/)
7. [98. 验证二叉搜索树 ](https://leetcode-cn.com/problems/validate-binary-search-tree/)
8. [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
9. [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
10. [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/description/)
11. [297. 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)
12. [77. 组合](https://leetcode-cn.com/problems/combinations/)
13. [46. 全排列](https://leetcode-cn.com/problems/permutations)
13. [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)
13. []()
13. []()
13. []()
13. []()
13. []()



## todo

1. ⼆叉树的最近公共祖先 

2. 从前序与中序遍历序列构造⼆叉树

3. 169.多数元素   https://leetcode-cn.com/problems/majority-element/description/
