class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        
        var lastIndex = nums.count
        if lastIndex == 0 {
            return 0
        }
        var tampIndex = 1
        var tampValue = nums[0]
        
        for i in 1..<lastIndex {
            if tampValue != nums[i] {
                nums[tampIndex] = nums[i]
                tampValue = nums[i]
                tampIndex += 1
            }
        }
        return tampIndex
    }
}
