# array declaration
var names: [String] = ["Anne", "Gary", "Keith"]
var names = ["Anne", "Gary", "Keith"]
var numbers = [1, -3, 50, 72, -95, 115]
var numbers: [Int8] = [1, -3, 50, 72, -95, 115]


# array types
var myArray: [Int] = []
var myArray: Array<Int> = []
var myArray = [Int]()


# To create an array of count 100 with repeating default values:
var myArray = [Int](repeating: 0, count: 100)


var names = ["Amy"]
names.append("Joe")
names += ["Keith", "Jane"]
print(names) //["Amy", "Joe", "Keith", "Jane"]

names.insert("Bob", at: 0)

var names = ["Amy", "Brad", "Chelsea", "Dan"]
let chelsea = names.remove(at: 2)
let dan = names.removeLast()
names.removeAll()

var myNewArray = firstArray + secondArray


# Dictionaries
[key1: value1, key2: value2, key3: value3]
var scores = ["Richard": 500, "Luke": 400, "Cheryl": 800]

var myDictionary = [String: Int]()
var myDictionary = Dictionary<String, Int>()
var myDictionary: [String: Int] = [:]

let oldValue = scores.updateValue(100, forKey: "Richard")


# Accessing a Dictionary
var scores = ["Richard": 500, "Luke": 400, "Cheryl": 800]
let players = Array(scores.keys) // ["Richard", "Luke", "Cheryl"]
let points = Array(scores.values) // [500, 400, 800]

