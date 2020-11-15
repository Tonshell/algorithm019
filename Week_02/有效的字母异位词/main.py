# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# 有效的字幕异位词
def isAnagram(s:str,t:str) -> bool:
    if len(s) != len(t):
        return False
    array = []
    for i in range(26):
        array.append(0)

    for i in range(len(s)):
        array[ord(s[i]) - ord('a')] += 1
        array[ord(t[i]) - ord('a')] -= 1
    for i in array:
        if i != 0:
            return False
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    isSuccess = isAnagram(s="abc", t="bac")
    print(isSuccess)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
