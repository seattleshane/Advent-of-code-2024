from utils import Utils

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
        total = total + diff
        
    return total

def part_2(data: list[str]):
    left = []
    right = []
    for line in data:
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    left.sort()
    set_of_right_values = set()
    right_dict: dict = {}
    total = 0
    for item in right:
        set_of_right_values.add(item)
    for set_item in set_of_right_values:
        right_dict[set_item] = right.count(set_item)
    
    for left_value in left:
        if left_value in right_dict.keys():
            total = total + (left_value * right_dict[left_value])
    
    return total

if __name__ == "__main__":
    data = Utils.parse_values_from_text_file("Day 1\\test.txt")
    part_1_answer = part_1(data)
    print(part_1_answer)
    part_two_answer = part_2(data)
    print(part_two_answer)
    