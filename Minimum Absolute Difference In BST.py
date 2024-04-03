class Solution:
    def absolute_diff(self,root):
        ans = float("inf")
        lst =[]
        def func(root):
            nonlocal ans
            if root is None:
                return
            func(root.left)
            if not lst:
                lst.append(root.data)
            else:
                ele = lst.pop()
                ans = min(ans,root.data-ele)
                lst.append(root.data)
            func(root.right)
        func(root)
        return ans