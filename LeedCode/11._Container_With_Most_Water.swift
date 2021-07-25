class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var maxCount = 0
        var a = 0
        var z = height.count - 1
        
        while a < z {
            
            if height[a] < height[z] {
                let count = height[a] * (z-a)
                
                if maxCount < count {
                    maxCount = count
                }
                a += 1
            } else {
                let count = height[z] * (z-a)
                
                if maxCount < count {
                    maxCount = count
                }
                z -= 1
            }
        }
        
        return maxCount
    }
}
