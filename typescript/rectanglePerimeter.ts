


// This function should take two positive numbers (length and width) as inputs and return the perimeter of a rectangle.

// example

// Input: Two integers (number).

// Output: Integer (number).

// Examples:

// 1
// assert.strictEqual(rectanglePerimeter(2, 4), 12);
// 2
// assert.strictEqual(rectanglePerimeter(3, 5), 16);
// 3
// assert.strictEqual(rectanglePerimeter(10, 20), 60);
// 4
// assert.strictEqual(rectanglePerimeter(7, 2), 18);
// How it’s used:

// in architectural and engineering applications for calculating the perimeter of buildings or rooms;
// in computer graphics to calculate the perimeter of a rectangle on a screen.
// Preconditions:

// length, width ∈ R;
// length, width > 0.


function rectanglePerimeter(length: number, width: number): number {
    // your code here
    return 2 * (length + width);
}

console.log("Example:");
console.log(rectanglePerimeter(3, 2));

