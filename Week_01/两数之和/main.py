# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



#两数之和 暴力法 （时间复杂度高，O(n^2)）
def twoSum(nums,target):
    sumsArray = []
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
           if target - nums[j] == nums[i] :
               array = [i,j]
               sumsArray.append(array);
               continue;
    print(sumsArray)

# 哈希解法
def twoSum_Hash(nums,target):
    hashTable = {}
    for i,num in enumerate(nums):
        if target - num in hashTable :
            return [hashTable[target - num],i]
        hashTable[nums[i]] = i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   #twoSum([2, 7, 11, 15],9)
   print(twoSum_Hash([2, 7, 11, 15],9))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
