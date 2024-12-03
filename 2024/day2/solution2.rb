def check_report(list, is_warned = false)
    prev = list.first
    comparison_method = comp_method(list)
    list[1..].each_with_index do |elem, ind|
        is_correct =
        if prev.send(comparison_method, elem) && ((prev - elem).abs in (1..3))
            prev = elem
        else
            return false if is_warned

            return check_report(list.reject.with_index { |_el, index| index ==  ind+1 }, true) || check_report(list.reject.with_index { |_el, index| index == ind }, true)
        end
    end

    true
end

def comp_method(list)
    h = Hash.new(0)

    list[1..].each_with_index do |v, i|
        if v < list[i]
            h[">"] += 1
        elsif v > list[i]
            h["<"] += 1
        end
    end

    h[">"] > h["<"] ? ">" : "<"
end


reports = File.read("input.txt").split("\n").map(&:split)

puts reports.filter { check_report(_1.map(&:to_i)) }.count
