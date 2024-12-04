require_relative "./position.rb"

def input
  @_input = File.read("input.txt").split("\n")
end

def directions
  [-1, 1].product([-1, 1]).map { Position.new(_1, _2) }
end

def check_xmas(position)
  br = position + Position.new(1, 1)
  bl = position + Position.new(1, -1)
  tr = position + Position.new(-1, 1)
  tl = position + Position.new(-1, -1)

  ((br.value?("M") && tl.value?("S")) || (br.value?("S") && tl.value?("M"))) && ((bl.value?("M") && tr.value?("S")) || (bl.value?("S") && tr.value?("M")))
end

count = 0

input.each_with_index do |string, row|
  string.chars.each_with_index do |char, col|
    count +=1 if char == "A" and check_xmas(Position.new(row, col))
  end
end

puts count
