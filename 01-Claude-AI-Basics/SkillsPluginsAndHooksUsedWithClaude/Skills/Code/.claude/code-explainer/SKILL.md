---
name: code-explainer
description: Use this skill whenever the user asks to "explain", "walk me through", "break down", or "help me understand" a snippet of code. Also triggers on phrases like "what does this code do" or "how does this function work". Produces a beginner-friendly explanation in a fixed 4-section structure.
---

# Code Explainer

## When to use
Use this skill any time the user shares code and wants to understand it, including:
- "Explain this function"
- "Walk me through this code"
- "What does this do?"
- "How does this work?"
- "Break down this snippet"

## Output format (always use this exact structure)

Always respond with these **four sections, in this exact order**, using these exact headings. Never skip a section and never reorder them.

### 1. What it does (one line)
A single plain-English sentence summarising what the code accomplishes. No jargon. Imagine you are explaining it to a friend who has never coded.

### 2. Line by line
A bulleted list walking through the code. Format each bullet as:
- **Line N:** what this line does.

Group related lines if they clearly form a single step (e.g. an if/else block).

### 3. Real-world analogy
One or two sentences that compare the code to something from everyday life (cooking, shopping, sorting laundry, etc.). This helps beginners build mental models.

### 4. Watch out for
Two or three bullet points on common mistakes, edge cases, or things that could break. Focus on what a beginner might get wrong.

## Rules
- Use **plain English**. Avoid jargon words like "instantiate", "polymorphism", "mutate", "closure" — or if you must use them, explain them in parentheses.
- **Never invent behavior.** If you are unsure what a line does, say so.
- Assume the reader is a **beginner** programmer.
- Keep the whole response under about 250 words so it stays digestible.

## Example

For the code:
```python
def greet(name):
    if name:
        return f"Hello, {name}!"
    return "Hello, stranger!"
```

The response should look like this:

### 1. What it does (one line)
Returns a friendly greeting, using the person's name if we know it.

### 2. Line by line
- **Line 1:** Defines a function called `greet` that takes one input, `name`.
- **Line 2:** Checks if `name` has a value (not empty).
- **Line 3:** If yes, returns a personalised greeting using an f-string.
- **Line 4:** If no, returns a generic greeting instead.

### 3. Real-world analogy
Like a receptionist who says "Hello, Priya!" if they recognise you, and "Hello, stranger!" if they do not.

### 4. Watch out for
- An empty string `""` counts as "no name" because empty strings are falsy in Python.
- Passing `None` also falls into the second branch.
- The function only returns a string — it does not print anything.
