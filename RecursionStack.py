def dfs(n, k):
    if n > 10:
        return
    print(" "*k*2+"<"+str(n)+">")
    dfs(n*2, k+1)
    dfs(n*2+1, k+1)
    print(" "*k*2+"</"+str(n)+">")

dfs(1, 0)
