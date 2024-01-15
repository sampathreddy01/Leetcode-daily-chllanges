class Solution(object):
    def leafSimilar(self, root1, root2):
        def getLeafSequence(root, sequence):
            if root:
                if not root.left and not root.right:
                    sequence.append(root.val)
                getLeafSequence(root.left, sequence)
                getLeafSequence(root.right, sequence)

        sequence1, sequence2 = [], []
        getLeafSequence(root1, sequence1)
        getLeafSequence(root2, sequence2)
        return sequence1==sequence2
