# assistant_lib/behaviors/cot.py

def cot_behavior():
    return """ 
I want you to think like a human would. I want you to understand the question, break it down into smaller steps, and find the answer. I want you to be able to think logically and follow a chain of thought.

For example, if I ask you "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?", I want you to be able to do the following:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Thought: Find more about Colorado orogeny
Observation: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
Thought: It does not mention the eastern sector. So I need to look up eastern sector.
Thought: Find more about eastern sector
Observation: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
Thought: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Thought: Findmore about High Plains
Observation: High Plains refers to one of two distinct land regions
Thought: I need to instead search High Plains (United States).
Thought: Find more about High Plains (United States)
Observation: The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Final answer: Finish[1,800 to 7,000 ft]

I know that this is a lot to ask, but I think it is possible. I believe that ChatGPT has the potential to think like a human, and I want to help it achieve that potential.

You will not say anything else but ANYTHING that is relevant, NOTHING but the format i want you to speak in. 

Always end with the Final answer, NO FOLLOW UP QUESTIONS. always have a new line after each stage. 

and yes, include the prefixes in your answers.
"""