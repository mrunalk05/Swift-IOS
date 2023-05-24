for index in 1...5 {
  print("This is number \(index)")
}

for _ in 1...3 {
  print("Hello!")
}

let names = ["Joseph", "Cathy", "Winston"]
for name in names {
  print("Hello \(name)")
}

# The enumerated() method of an array or string to return a tuple—a special type that can hold an ordered list of values wrapped in parentheses—containing both the index and the value of each item:

for (index, letter) in "ABCD".enumerated() {
  print("\(index): \(letter)")
}

# Console Output:
0: A
1: B
2: C
3: D

# while loop
var numberOfLives = 3
var stillAlive = true

while stillAlive {
  numberOfLives -= 1
  if numberOfLives == 0 {
    stillAlive = false
  }
}

# Repeat-While Loops
A repeat-while loop is similar to the while loop, but this syntax executes the block once before checking the condition.

var steps = 0
let wall = 2 // there's a wall after two steps

repeat {
  print("Step")

  steps += 1

  if steps == wall {
    print("You've hit a wall!")
    break
  }
} while steps < 10 // maximum in this direction

