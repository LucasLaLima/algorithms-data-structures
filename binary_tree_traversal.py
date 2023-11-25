 """
Tree traversal is the process of visiting all nodes of a tree.

Three universally understood types of tree traversal.
1) in-order
2) post-order
3) pre-order

Nodes always has at most two children.

Using the binary_tree.png:
1) In-order:
- Visits left-most node
- Then root node
- Then right node

Answer: DBEAFCG

2) Post-order
Used to delete a tree leaf to root
- Left
- Right
- Root

Answer: DEBFGCA

3) Pre-order
Used to create a copy of a tree
- Root
- Left
- Right

Answer: ABDECFG
 """