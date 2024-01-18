# Efficient string building

# arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)

# In JavaScript, benchmarking shows that concatenation with += is faster than using .join().
