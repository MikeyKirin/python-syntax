def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    if 7 in nums:
        print("True!")

    if not 7 in nums:
        print("False")


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
