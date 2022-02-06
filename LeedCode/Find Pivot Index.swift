// Find Pivot Index

class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        
        var lSum = 0
        var rSum = nums.reduce(0, +)
        
        for i in 0..<nums.count {
            rSum -= nums[i]
            
            if lSum == rSum {
                return i
            }
            lSum += nums[i]
        }
        
        return -1
    }
}
