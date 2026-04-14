nums = [3,2,4]
target = 6

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range (0, len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
    
two_sum(nums, target)
            
