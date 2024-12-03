def check_report(list)
    prev = list.first
    comparison_method = prev < list.last ? "<" : ">"
    list[1..].each do
        return false unless ((prev - _1).abs in (1..3)) && prev.send(comparison_method, _1)
        prev = _1
    end

    true
end

reports = File.read("input.txt").split("\n").map(&:split)

puts reports.filter { check_report(_1.map(&:to_i)) }.count
