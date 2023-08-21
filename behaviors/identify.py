# assistant_lib/behaviors/identify.py

def identify_behavior():
    return """
I need you to act as a determiner. I want you to determine if my input needs a function. I will give you two functions: "cot" (chain of thought) and "none" (useful for conversations).

For example, if I ask you "What is the capital of France?", you would return "cot".

However, if I ask you "How are you?", you would return "none".

I will now give you a few examples of inputs and their corresponding functions.

Input: "What is the capital of France?", Function: "cot"
Input: "How are you?", Function: "none"
Input: "What is the meaning of life?", Function: "cot"
Input: "What is your favorite color?", Function: "none"
Now, I will give you an input. Please return the function that is associated with it.
"""
