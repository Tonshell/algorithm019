# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def moveZore(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for i in range(j,len(nums)):
        nums[i] = 0
    print(nums)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    moveZore([0,1,0,3,4,5])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
