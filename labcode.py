# --- Problem 1: Basic Statistics ---
tokens = [18, 42, 37, 10, 55, 26]

total = sum(tokens)
avg = total / len(tokens)
mn = min(tokens)
mx = max(tokens)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Minimum: {mn}")
print(f"Maximum: {mx}")

# --- Problem 2: Prompt Validation Logic ---
prompts = [
    " Explain transformers ?",
    "hi",
    " please summarize this paragraph about GANs ",
    " Generate an image of a cat"
]

def is_good_prompt(prompt):
    if len(prompt) < 20:
        return False
    if "?" in prompt:
        return True
    if "please" in prompt.lower():
        return True
    return False

for prompt in prompts:
    if is_good_prompt(prompt):
        print(prompt, "->", is_good_prompt(prompt))

# --- Problem 3: Data Zipping/List Building ---
lengths = [20, 35, 15, 50, 45]
helpful = [0, 1, 0, 1, 1]

data = []
for i in range(len(lengths)):
    data.append((lengths[i], helpful[i]))

print(data)

# --- Problem 4: Accuracy Calculation ---
y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1, 1]

correct = 0
for i in range(len(y_true)):
    if y_true[i] == y_pred[i]:
        correct += 1

accuracy = correct / len(y_true)
print("Accuracy:", accuracy)