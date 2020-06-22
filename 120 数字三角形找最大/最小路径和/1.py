test_case = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

# from top to bottom
def simpleDP(a, layer, col):
    if layer == len(a) - 1: # last layer
        return a[layer][col]
    cur_val = a[layer][col]
    left = simpleDP(a, layer + 1, col)
    right = simpleDP(a, layer + 1, col + 1)
    return cur_val + min(left, right)
# from bottom to top
def btToDP(a): # record the value and from bt to top
    for layer in range(len(a) - 1, 0, -1):
        for col in range(layer):
            a[layer - 1][col] += min(a[layer][col], a[layer][col + 1]) 
    return a[0][0] 
r = simpleDP(test_case, 0, 0)
print(r)
r = btToDP(test_case)
print(r)