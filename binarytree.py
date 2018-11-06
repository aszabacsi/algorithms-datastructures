def flat(xs):
  
  flatarr = []
  
  for x in xs:
    if isinstance(x, list):
      flatarr.extend(flat(x))
    else: 
      flatarr.append(x)
  
  return flatarr
    
  
def toTheLeft(node):
  if node.left != None:
    return [node, toTheLeft(node.left)]
  else: return node

def toTheRight(node):
  if node.right:
    return [node, toTheRight(node.right)]
  else: return node

def topView(root):
  arr = []
  if root.left != None:
    arr.extend(reversed(toTheLeft(root.left)))
  arr.append(root)
  if root.left != None:
    arr.extend(toTheRight(root.right))
  return map(lambda x: x.info, flat(arr))


class Node:

  def __init__(self, info):

    self.left = None
    self.right = None
    self.info = info

def binaryTree(arr):
  sortedArr = sorted(arr)
  root = Node(sortedArr[0: len(arr)])
  if root.left:
    root.left = binaryTree(root.left)
  if root.right:
    root.right = binaryTree(root.right)
  return root

def binaryTreeToList(root):
  
  arr = []
  
  if root.left:
    arr.extend(binaryTreeToList(root.left))
  if root:
    arr.append(root.info)
  if root.right:
    arr.extend(binaryTreeToList(root.right))

  return flat(arr)

root = binaryTree([1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9])

print(str(topView(root)))

print(str(binaryTreeToList(root)))