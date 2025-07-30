## What are linear Data structures??
---
- stacks
- queues
- deques
- lists

- linear structures are collections whose items are ordered depending on how they are added or removed.
---
### stack:
---
- ordered collection of items where the addition of new items and removal of existing items always takes place at the same end.
- LIFO
 
- ADT(Abstract Data Type):
```
    class Stack:
        Stack() // Constructor
        push(item) // adds a new item at the top
        pop() // remove from the top
        peek() // returns the top item without removing
        is_empty() // check is stack is empty
        size() returns the number of items in the stack
```