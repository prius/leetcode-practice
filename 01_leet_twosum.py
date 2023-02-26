class Solution(object):
    def twoSum(self, nums, target):
        
        id1 = 0 # first tracker to find the first index
        id2 = 0 # second tracker to find the second index
        result = []
        found = 0 # boolean to track when the index pair is found
       
        # loop over the list as a reference until the second index is found
        while(id1<len(nums) and found==0):
            # loop over the list resulting from the absolute difference with the target until the reference is found  
             while(id2<len(nums) and found==0):
                 if ((id2 != id1) and (nums[id1] == abs(target - nums[id2]))):
                     found = 1
                     result.append(id1)
                     result.append(id2)
                 id2 = id2 + 1
            # if nothing is found go over the next reference and reset the second loop
             if (id2>=len(nums) and found==0):
                 id1 = id1 + 1
                 id2 = 0
        return result
