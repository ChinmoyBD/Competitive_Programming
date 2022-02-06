// 34. Find First and Last Position of Element in Sorted Array

class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        var l = 0
        var r = nums.count-1
        var isL = false
        var isR = false

        while l <= r {
            
            if nums[l] == target {
                isL = true
            } else {
                if !isL {
                    l += 1 
                }
            }
            
            if nums[r] == target {
                isR = true
            } else {
                if !isR {
                    r -= 1
                }
            }
            
            if isL && isR {
                return [l, r]
            }
        }
        
        return [-1, -1]
    }
}
