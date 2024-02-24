# create Stack class
class Stack
    attr_reader :elements
    attr_writer :elements
    attr_reader :size
    attr_writer :size
    @elements = []
    @size = 0

    # str method
    def self.display
        if size > 0
            @elements.each do |e|
                print "#{e} "
            end
        else
            return "None"
        end
    end

    def self.size
        return @elements.size
    end

    def self.push(data)
        @elements.push(data)
    end

    def self.pop
        temp = @elements[-1]
        @elements.pop()
        return temp
    end

    def self.peek
        return @elements[-1]
     end
end
