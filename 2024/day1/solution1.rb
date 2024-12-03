input_list = File.read("input.txt").split("\n").map(&:split)

left_numbers = input_list.map(&:first).map(&:to_i).sort
right_numbers = input_list.map(&:last).map(&:to_i).sort

puts left_numbers.zip(right_numbers).map { (_1 - _2).abs }.sum
