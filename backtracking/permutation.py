
def backtrrrkperm(nums,path,results):
    if not nums:
        results.append(path)
        return
    for i in range(len(nums)):
        new_path = path + [nums[i]]
        new_nums = nums[:i] + nums[i+1]
        backtrrrkperm(new_nums,new_path,results)

nums = [1,2,3]
print(backtrrrkperm(nums,path=[],results=[]))














