class Solution(object):
    def rangeSumBST(self, root, low, high):
        l=[]
        l.append(root)
        result=low+high
        while l:
            q=l.pop(0)
            if q.val>low and q.val<high:
                result+=q.val
            if q.left:
                l.append(q.left)
            if q.right:
                l.append(q.right)
        return result
