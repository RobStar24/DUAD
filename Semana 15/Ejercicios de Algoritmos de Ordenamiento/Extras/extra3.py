def validated_bubble_sort(lst):
    if not lst:
        raise ValueError("Error: The list is empty")
    
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("Error: The list contains non-numeric elements")
    
    def bubble_sort(lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst
    
    return bubble_sort(lst)


try:
    entry = [5, "hello", 2]
    res = validated_bubble_sort(entry)
    print(res)  
except ValueError as e:
    print(e)