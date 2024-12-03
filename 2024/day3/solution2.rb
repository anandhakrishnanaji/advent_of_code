input = File.read("input.txt")

REGEX_PATTERN = /mul\((\d+),(\d+)\)|(don)\'t\(\)|(do)\(\)/

current_flag = true
sum = 0

input.scan(REGEX_PATTERN).each do |i, j, k, l|
  unless i.nil? || j.nil?
    sum += i.to_i * j.to_i if current_flag
  else
    current_flag = k.nil? || !l.nil?
  end
end

puts sum
