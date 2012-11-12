def read_matrix(fname)
  File.read(fname).split("\n").collect{|l| l.split(/[^\d]/).collect(&:to_i)}
end

def minsum(matrix)
  size = matrix.length #Assuming it is a square matrix(n*n, not n*m)
  minsummatrix = Array.new(size){Array.new(size)}
  minsummatrix[-1][-1] = matrix[-1][-1]
  (0...size-1).reverse_each do |x|
    minsummatrix[x][-1] = matrix[x][-1] + minsummatrix[x+1][-1]
  end
  (0...size-1).reverse_each do |x|
    minsummatrix[-1][x] = matrix[-1][x] + minsummatrix[-1][x+1]
  end
  (0...size-1).reverse_each do |i|
    (0...size-1).reverse_each do |x|
      minsummatrix[x][i] = matrix[x][i] + [minsummatrix[x+1][i], minsummatrix[x][i+1]].min
    end
    (0...size-1).reverse_each do |x|
      minsummatrix[i][x] = matrix[i][x] + [minsummatrix[i][x+1], minsummatrix[i+1][x]].min
    end
  end
  return minsummatrix[0][0]
end

p minsum(read_matrix(ARGV[0]))

