enum Direction {
    case right, buttom, left, top
}

class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        
        var x = 0
        var xx = matrix[0].count
        var y = 0
        var yy = matrix.count
        
        if xx == 0 || yy == 0 {
            return matrix[0]
        }
        
        var spiralMatrix = [Int]()
        var row = 0
        var col = 0
        var direction = Direction.right
        
        for _ in 0..<xx*yy {
            
            switch direction {
            case .right:
                spiralMatrix.append(matrix[row][col])
                
                if col < xx-1 {
                    col += 1
                } else {
                    row += 1
                    x += 1
                    direction = .buttom
                }
                print("right", spiralMatrix)
                
            case .buttom:
                spiralMatrix.append(matrix[row][col])
                if row < yy-1 {
                    row += 1
                } else {
                    col -= 1
                    xx -= 1
                    direction = .left
                }
                print("buttom", spiralMatrix)
                
            case .left:
                spiralMatrix.append(matrix[row][col])
                if col > y {
                    col -= 1
                } else {
                    row -= 1
                    yy -= 1
                    direction = .top
                }
                print("right", spiralMatrix)
                
            case .top:
                spiralMatrix.append(matrix[row][col])
                if row > x {
                    row -= 1
                } else {
                    col += 1
                    y += 1
                    direction = .right
                }
                print("top", spiralMatrix)
            }
        }
        return spiralMatrix
    }
}
