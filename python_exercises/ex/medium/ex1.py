def three_sum(nums):
    result = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to avoid duplicates in different order
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return [list(triplet) for triplet in result]


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

#done