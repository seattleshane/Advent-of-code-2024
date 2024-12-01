from utils import Utils
from enum import Enum

def part_1(data: list[str]):
    left = []
    right = []
    total = 0
    for line in data:
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    left.sort()
    right.sort()
    for index, value in enumerate(left):
        diff = abs(value - right[index])
        # if value > right[index]:
        #     diff = value - right[index]
        # elif value < right[index]:
        #     diff = right[index] - value
        # else:
        #     diff = 0
        total = total + diff
        
    return total

def part_2(data: list[str]):
    left = []
    right = []
    for line in data:
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    left.sort()
    right.sort()
    set_of_right_values = set()
    right_dict: dict = {}
    total = 0
    for item in right:
        set_of_right_values.add(item)
    for set_item in set_of_right_values:
        right_dict[set_item] = right.count(set_item)
    
    for thing in left:
        if thing in right_dict.keys():
            total = total + (thing * right_dict[thing])
    
    return total


if __name__ == "__main__":
    data = Utils.get_values_from_file("test.txt")
    total = part_1(data)
    print(total)
    part_2(data)