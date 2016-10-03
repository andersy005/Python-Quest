
def rotate(matrix):
    print matrix
    n = len(matrix[0])
    print n
    
    for layer in range(n/2):
      
        first = layer
        last = n - 1 - layer

        i = first
        print "first:", first
        print "layer:", layer
        print "last:", last


        while i < last:
            print "*"*50
            offset = i - first
            print "offset:", offset

            # Save top
            top = matrix[first][i]
            print "top:", top

            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            print "matrix[first][i]: ", matrix[first][i]

            # bottom -> left
            matrix[last-offset][first] = matrix [last][last-offset]
            print "matrix[last-offset][first]: ", matrix[last-offset][first]

            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            print "matrix[last][last-offset]: ", matrix[last][last-offset]

            # top -> right 
            matrix[i][last] = top
            print "matrix[i][last]: ", matrix[i][last]

            i += 1

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(matrix))