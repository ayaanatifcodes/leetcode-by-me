# Time and Space Complexity – Quick Reference

## 🕒 Time Complexity

Time complexity measures how the runtime of an algorithm grows as the input size grows.

We use **Big-O notation** to describe growth rate.

It does NOT measure actual seconds.
It measures scalability.

## 📈 Common Time Complexities

### O(1) — Constant Time
Runtime does not change with input size.

Example:
Accessing an array index.

Best possible complexity.

### O(n) — Linear Time
Runtime grows directly with input size.

Example:
Looping through an array once.

If input doubles → runtime doubles.

### O(n²) — Quadratic Time
Usually caused by nested loops.

If input doubles → runtime becomes 4× larger.

Gets slow very fast.

### O(log n) — Logarithmic Time
Each step reduces the problem size by half.

Example:
Binary Search.

Very efficient for large inputs.

### O(n log n)
Common in efficient sorting algorithms.

Good balance between speed and practicality.

## ⚡ Rules When Calculating Time Complexity

1. Drop constants  
   5n → O(n)

2. Drop lower-order terms  
   n² + n → O(n²)

3. Keep only the dominant term.

## 📦 Space Complexity

Space complexity measures how much extra memory an algorithm uses as input grows.

We do NOT count the input itself.
We count extra variables and data structures created.

### O(1) Space — Constant Memory
Uses fixed number of variables.

Memory does not grow with input.

### O(n) Space — Linear Memory
Creates new data structures that grow with input size.

If input doubles → memory doubles.

### O(n²) Space
Creates structures like n × n matrices.

Memory grows very quickly.

## 🧠 How to Analyze an Algorithm

Ask:

1. How many loops are there?
2. Are loops nested?
3. Does recursion split the problem?
4. Am I creating new lists, arrays, or maps?
5. Does memory grow with input size?

## 🎯 Example: Sliding Window

If we loop through a string once:

Time Complexity: O(n)

If we use only a few variables:

Space Complexity: O(1)

## 🏆 Final Mental Model

Time Complexity → How fast runtime grows  
Space Complexity → How fast memory usage grows  

Always aim for:
- Lowest possible time complexity
- Minimal extra space usage

Think scalability.
