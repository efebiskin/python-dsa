from dsa.trees import TreeNode, is_valid_bst, level_order, lowest_common_ancestor


def build_bst():
    #         5
    #        / \
    #       3   8
    #      / \   \
    #     1   4   9
    n1, n3, n4, n5, n8, n9 = TreeNode(1), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(8), TreeNode(9)
    n5.left, n5.right = n3, n8
    n3.left, n3.right = n1, n4
    n8.right = n9
    return n5, {1: n1, 3: n3, 4: n4, 5: n5, 8: n8, 9: n9}


class TestLevelOrder:
    def test_empty(self):
        assert level_order(None) == []

    def test_standard(self):
        root, _ = build_bst()
        assert level_order(root) == [[5], [3, 8], [1, 4, 9]]


class TestIsValidBST:
    def test_valid_bst(self):
        root, _ = build_bst()
        assert is_valid_bst(root) is True

    def test_rejects_local_but_not_global(self):
        # Looks valid locally: 5 > 3 and 5 < 6. But 3 in the right subtree
        # violates the global "all > 5" rule.
        root = TreeNode(5, TreeNode(3), TreeNode(6, TreeNode(3), TreeNode(7)))
        assert is_valid_bst(root) is False

    def test_single_node(self):
        assert is_valid_bst(TreeNode(42)) is True


class TestLowestCommonAncestor:
    def test_split_subtrees(self):
        root, nodes = build_bst()
        assert lowest_common_ancestor(root, nodes[1], nodes[9]) is root  # 5

    def test_one_is_ancestor(self):
        root, nodes = build_bst()
        assert lowest_common_ancestor(root, nodes[3], nodes[4]) is nodes[3]

    def test_same_node(self):
        root, nodes = build_bst()
        assert lowest_common_ancestor(root, nodes[5], nodes[5]) is nodes[5]
