class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.items.length === 0) {
      return null;
    }
    return this.items.pop();
  }

  peek() {
    if (this.items.length === 0) {
      return null;
    }
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

function verifyEquation(equation) {
  const stack = new Stack();
  const operators = ['+', '-', '*', '/'];
  const operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

  // Remove all whitespace from the equation
  equation = equation.replace(/\s+/g, '');

  // Check for matching parentheses
  for (let i = 0; i < equation.length; i++) {
    if (equation[i] === '(') {
      stack.push(equation[i]);
    } else if (equation[i] === ')') {
      if (stack.peek() === '(') {
        stack.pop();
      } else {
        return "Unbalanced parentheses: closing parenthesis without a matching opening parenthesis";
      }
    }
  }

  if (!stack.isEmpty()) {
    return "Unbalanced parentheses: opening parenthesis without a matching closing parenthesis";
  }

  // Check if each operator is followed by an operand
  for (let i = 0; i < equation.length; i++) {
    if (operators.includes(equation[i])) {
      if (!operands.includes(equation[i + 1]) && equation[i + 1] !== '(') {
        return `Operator '${equation[i]}' is not followed by an operand`;
      }
    }
  }

  return "Equation is valid";
}

//Tests
const equation1 = "(2 + 3) * 4";
console.log(verifyEquation(equation1));  // Outputs: Equation is valid

const equation2 = "(2 + 3";
console.log(verifyEquation(equation2));  // Outputs: Unbalanced parentheses: opening parenthesis without a matching closing parenthesis

const equation3 = "2 + ";
console.log(verifyEquation(equation3));  // Outputs: Operator '+' is not followed by an operand
