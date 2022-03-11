def solution(A):
    # write your code in Python 3.6
    myList=[A.count(x) for x in set(A)]
    return sum(filter(lambda x: x>1, myList))


print(solution([1,2,3,2]))