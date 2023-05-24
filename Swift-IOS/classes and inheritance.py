
# class 

class Person {
  let name: String

  init(name: String) {
    self.name = name
  }
}

# Defining a Base Class

class Vehicle {
    var currentSpeed = 0.0

    var description: String {
        "traveling at \(currentSpeed) miles per hour"
    }

    func makeNoise() {
        // do nothing - an arbitrary vehicle doesn't necessarily make a noise
    }
}

let someVehicle = Vehicle()
print("Vehicle: \(someVehicle.description)")

# Defining a Base Class

# syntax
class SomeSubclass: SomeSuperclass {
    // subclass definition goes here
}

class Bicycle: Vehicle {
    var hasBasket = false
}

# Override Methods and Properties

class Train: Vehicle {
    override func makeNoise() {
        print("Choo Choo!")
    }
}

let train = Train()
train.makeNoise()

# importing from superclass
class Car: Vehicle {
    var gear = 1
    override var description: String {
        super.description + " in gear \(gear)"
    }
}


# Override Initializer

class Person {
  let name: String

  init(name: String) {
    self.name = name
  }
}

class Student: Person {
  var favoriteSubject: String

  init(name: String, favoriteSubject: String) {
    self.favoriteSubject = favoriteSubject
    super.init(name: name)
  }
}


