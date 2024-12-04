require_relative "./position.rb"

def input
  @_input = File.read("input.txt").split("\n")
end

def directions
  ([-1, 0, 1].product([-1, 0, 1]) - [[0, 0]]).map { Position.new(_1, _2) }
end

def check_xmas(position, direction)
  new_position = position + direction
  %w[M A S].each do |char|
    return false if !new_position.value?(char)
    new_position+= direction
  end
  true
end

count = 0

input.each_with_index do |string, row|
  string.chars.each_with_index do |char, col|
    if char == "X"
      position = Position.new(row, col)
      directions.each do |direction|
        count +=1 if check_xmas(position, direction)
      end
    end

  end
end

p count
