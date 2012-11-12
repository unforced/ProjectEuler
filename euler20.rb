def factorial(n)
  n<=1 ? 1 : n * factorial(n-1)
end

puts factorial(ARGV[0].to_i).to_s.each_char.collect(&:to_i).inject(:+)
