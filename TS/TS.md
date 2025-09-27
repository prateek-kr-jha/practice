# Type Script: A stricter and type safe JS
------
Javascript that scales.
Superset of JS.
Doesn't directly execute in Browser.
TS -> compiler -> JS

### 1. Variables and Types:
In typescript every variable can have type, in case it doesn't have, TS infers it.
```ts
// Numbers
let age: number = 25;

// Strings
let name: string = "Prateek";

// Booleans
let isDone: boolean = false;

// Arrays
let scores: number[] = [10, 20, 30];
let names: string[] = ["Alice", "Bob"];

// Objects
let user: { id: number; name: string } = { id: 1, name: "Alice" };

let city = "Bangalore"; // inferred as string

```

### 2. Functions:
You can give types to parameters and return values.
Functions can also return void if they don't return anything.

```ts
function add(a: number, b: number): number {
  return a + b;
}

let result = add(5, 3); // result is number

function logMessage(msg: string): void {
  console.log(msg);
}
```

### 3. Union and Literal Types:
Union = a variable can be one of several types.

```ts
let value: number | string;
value = 42;
value = "hello";
```

### 4. Classes:
Classes are like blueprints for objects.
You define fields(properties) and methods.

```ts
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): void {
    console.log(`Hi, I am ${this.name}, ${this.age} years old`);
  }
}

const p = new Person("Alice", 30);
p.greet(); // Hi, I am Alice, 30 years old
```

### 5. Inheritance (extends) & super:
You can make a class extend another class (your TodoItem extends TreeItem)

```ts
class Animal {
  constructor(public name: string) {}
  speak() {
    console.log(`${this.name} makes a sound`);
  }
}

class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name); // call parent constructor
  }
  speak() {
    console.log(`${this.name} barks`);
  }
}

const d = new Dog("Tommy", "Beagle");
d.speak(); // Tommy barks

```


- Three basic types: number, string, boolean
- when impossibel to know the type use "Any"
- Array: 
```TS
  let list: number[] = [1, 2, 3]
  // generic array
  let list: Array<number> = [1, 2, 3]
```
- for enumerations:
```TS
enum Color { Red, Green, Blue }
let c: Color: Color.Green
```

- void is used in case function doesn't return anything
- functions are 1st class citizen, support lambda syntax and support type inference

```TS
// all are same
let f1 = function (i: number): number { return i * i; }
// type inferred
let f2 = function (i: number) { return i * i; }

let f3 = (i: number): number => { return i * i; }
// type inferred
let f4 = (i: number) => { return i * i; }

let f5 = (i: number) => i * i;

function f6(i: string | number): void {
  console.log("The value was " + i);
}
```

- interfaces are structural, anything that has the properties is compliant with the interfaces
```TS
interface Person {
  name: string;

  // optional properties
  age?: number;

  move(): void
}

// Object that implements the "Person" interface
// Can be treated as a Person since it has the name and move properties
let p: Person = { name: "Bobby", move: () => { } };
// Objects that have the optional property:
let validPerson: Person = { name: "Bobby", age: 42, move: () => { } };
// Is not a person because age is not a number
let invalidPerson: Person = { name: "Bobby", age: true };

// Interfaces can also describe a function type
interface SearchFunc {
  (source: string, subString: string): boolean;
}
// Only the parameters' types are important, names are not important.
let mySearch: SearchFunc;
mySearch = function (src: string, sub: string) {
  return src.search(sub) != -1;
}
```

- classes - members are public by default
```TS

```