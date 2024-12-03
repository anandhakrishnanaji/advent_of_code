def check_report(list, is_warned = false)
    prev = list.first
    comparison_method = prev < list.last ? "<" : ">"
    list[1..].each_with_index do |elem, ind|
        if prev.send(comparison_method, elem) && ((prev - elem).abs in (1..3))
            prev = elem
        else
            return false if is_warned

            return check_report(list.reject.with_index { |_el, index| index ==  ind+1 }, true) || check_report(list.reject.with_index { |_el, index| index == ind }, true)
        end
    end

    true
end

reports = File.read("input.txt").split("\n").map(&:split)

puts reports.filter { check_report(_1.map(&:to_i)) }.count
