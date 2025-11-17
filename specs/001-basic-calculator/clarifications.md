## Question 1: Square Root of Negative Numbers

**Context**: User Story 2 and FR-002 mention square root operations.

**What we need to know**: How should the calculator handle square roots of negative numbers?

**Suggested Answers**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A      | Raise an appropriate error | Consistent with other error handling for invalid mathematical operations. |
| B      | Return NaN (Not a Number) | Standard behavior in many floating-point systems for undefined real results. |
| C      | Support complex numbers | Expands the scope to include complex number arithmetic, potentially increasing complexity. |

**Your choice**: _[Wait for user response]_

## Question 2: Operator Precedence

**Context**: User Story 3 mentions parentheses for order of operations.

**What we need to know**: What is the default operator precedence for operations when parentheses are not used?

**Suggested Answers**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A      | Standard mathematical precedence (PEMDAS/BODMAS) | Follows common mathematical rules, intuitive for most users. |
| B      | Left-to-right evaluation | Simpler to implement, but less intuitive for standard mathematical expressions. |

**Your choice**: _[Wait for user response]_

## Question 3: Definition of "Appropriate Error"

**Context**: Multiple functional requirements and success criteria refer to "an appropriate error".

**What we need to know**: How should "an appropriate error" be defined?

**Suggested Answers**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A      | An error that clearly indicates the nature of the problem to the caller and allows for programmatic handling. | Provides clear feedback and enables robust error recovery in calling code. |
| B      | A generic error message indicating invalid input. | Simpler to implement, but less helpful for debugging or programmatic handling. |

**Your choice**: _[Wait for user response]_

## Question 4: Floating Point Rounding Rule

**Context**: FR-008 and SC-003 mention rounding floating-point results to 10 decimal places.

**What we need to know**: What specific rounding rule should be applied when rounding floating-point results?

**Suggested Answers**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A      | Round half up (e.g., 2.5 rounds to 3, -2.5 rounds to -3) | Common rounding method, often taught in schools. |
| B      | Round half even (banker's rounding) (e.g., 2.5 rounds to 2, 3.5 rounds to 4) | Reduces bias in a sequence of calculations, common in financial applications. |
| C      | Truncate (round towards zero) | Simplest to implement, but can introduce bias. |

**Your choice**: _[Wait for user response]_
