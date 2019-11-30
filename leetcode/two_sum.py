from typing import List
def twoSum( nums: List[int], target: int) -> List[int]:
    map = {}
    for idx,num in enumerate(nums):
        if num not in map:
            map[num] = [idx]
        else:
            map[num].append(idx)
    # print(map)
    for num,idx in map.items():
        diff = target-num
        # print(num,idx)
        if diff in map:
            if map[diff] != idx:
                return idx+map[diff]
            elif map[diff] == idx and len(map[diff])!=1:
                return map[diff][:2]
            else:
                continue



if __name__ == '__main__':
    print(twoSum([3,3],6))
    print(twoSum([3,2,4],6))
    print(twoSum([2,7,11,15],9))