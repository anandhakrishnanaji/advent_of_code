Position = Struct.new(:x, :y) do
  def +(other)
    Position.new(x + other.x, y + other.y)
  end

  def valid?
    (0...input.count).include? x and (0...input.count).include? y
  end

  def value?(char)
    valid? && input[x][y] == char
  end
end
