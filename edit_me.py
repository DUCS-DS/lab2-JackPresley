def monotonic(lst):
    if len(lst) < 2:
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    
    return increasing or decreasing

if __name__ == "__main__":
    # Test cases
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(monotonic(test_list))  # True

    test_list2 = [9, 7, 5, 4, 4, 3, 1]
    print(monotonic(test_list2))  # True

    test_list3 = [1, 3, 2, 4, 5]
    print(monotonic(test_list3))  # False

    test_list4 = [7, 7, 7, 7, 7]
    print(monotonic(test_list4))  # True

    test_list5 = []
    print(monotonic(test_list5))  # True

    test_list6 = [6, 5, 4, 3, 2, 1]
    print(monotonic(test_list6))  # True

