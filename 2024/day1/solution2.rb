input_list = File.read("input.txt").split("\n").map(&:split)

left_numbers = input_list.map(&:first).map(&:to_i)
right_numbers = input_list.map(&:last).map(&:to_i)

memory_hash = Hash.new { |hash, key| hash[key] = right_numbers.count(key) }

total_sum = left_numbers.map { _1 * memory_hash[_1] }.sum

puts total_sum
