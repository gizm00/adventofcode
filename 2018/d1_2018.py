
def get_nums_from_file(file_name):
    with open('input_2018_d1.txt') as f: 
        return [int(num.strip()) for num in f.readlines() if num.strip() != '']
        
def calibrate_frequency(nums):
    return sum(nums)
    
def find_repeat_frequency(nums):
    found_nums = {0:1}
    found_duplicate = None
    current_cnt = 0
    current_freq = 0
    while found_duplicate is None:
        index = current_cnt % len(nums)
        current_freq += nums[index]
        if current_freq in found_nums.keys():
            found_nums[current_freq] += 1
            if found_nums[current_freq] == 2:
                found_duplicate = current_freq
        else:
            found_nums[current_freq] = 1
        current_cnt += 1
    
    return found_duplicate
        
if __name__ == '__main__':
    nums = get_nums_from_file('input_2018_d1.txt')
    print(find_repeat_frequency(nums))
    
