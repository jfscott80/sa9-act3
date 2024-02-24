require "stack"
RSpec.describe Stack do
    # let(:stack) { Stack.new }
    describe "#display" do
        it "should return 'None' on empty stack" do
            expect(Stack.display).to eq("None")
            end
        end
    describe "#size" do
        it "should return zero on empty stack" do
            expect(Stack.size).to eq(0)
            end
        end
    describe "#push" do
        it "should push data to top of stack" do
            Stack.push("1")
            expect(Stack.size).to eq(1)
            expect(Stack.display).to eq(["1" ])
            end
        end
    describe "#peek" do
        it "should return 1" do
            expect(Stack.peek).to eq("1")
            end
        end
    describe "#pop" do
        it "should return 1 and size should return zero" do
            expect(Stack.pop).to eq("1")
            expect(Stack.size).to eq(0)
            end
        end
end