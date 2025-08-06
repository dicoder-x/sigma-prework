def digitize(n):
    return [int(char) for char in str(n)][::-1] # Convert int to str, loop through str & convert digit to int then reverse order