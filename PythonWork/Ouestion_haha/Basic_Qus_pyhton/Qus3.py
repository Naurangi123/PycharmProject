def union(arr1,arr2):
    un = []
    un = arr2
    for i in arr1:
        if i not in arr2:
            un.append(i) 
    return un
def interSection(arr1,arr2):
    inter = []
    for i in arr1:
        if i in arr2:
            inter.append(i)
    return inter

if __name__ == '__main__':
    arr1 = [1,2,3,4,5,6]
    arr2 = [2,3,4,8,9,10,15]
    print(f"Union of {arr1} and {arr2} = {union(arr1,arr2)}")
    print(f"InterSection of {arr1} and {arr2} = {interSection(arr1,arr2)}")
