puts File.read("input.txt").scan( /mul\((\d+),(\d+)\)/).map { |i, j| i.to_i * j.to_i }.sum
