from enum import Enum


class Prompt(Enum):
    EXPLAIN = "I want you to act as a code explainer in {language}. " \
              "I don't understand the following code snippet. " \
              "Can you please explain what it does, and, also, provide an example?" \
              "\n{context}\n" \
              "You can assume that the code snippet is correct. Your response should be in Markdown."
    GENERATE = "Write a program in {language} based on the provided requirements." \
               "\n{context}\n" \
               "Your response should be in Markdown."
    DEBUG = "I want you to act as a {language} debugger. " \
            "The following code snippet does not work as intended. " \
            "\n{context}\n" \
            "Can you please explain why it does not work, and, also, provide the fix for it?" \
            "Provide the fixed code as Markdown."
    ANSWER = 'I want you to act as a StackOverflow post written by an ' \
             'Expert {language} Programmer with 25 years of experience. ' \
             'I will ask programming-related questions and ' \
             'you will reply with what the answer should be as a Markdown document. ' \
             'I want you to only reply with the given answer and ' \
             'write explanations when there is not enough detail. ' \
             'Do not write explanations. My first question is:' \
             "\n{context}"
    OPTIMIZE = "I want you to act as a code optimizer in {language}. " \
               "Can you make the following code snippet more efficient so that it runs faster? " \
               "\n{context}\n" \
               "You can assume that the code snippet is correct. Provide the optimized code as Markdown."
    REFACTOR = "I want you to act as a code optimizer in {language}. " \
               "Can you make the following code snippet cleaner and more readable? " \
               "\n{context}\n" \
               "You can assume that the code snippet is correct. Provide the refactored code as Markdown."
    DOCUMENT = "Write documentation for the following {language} code." \
               "\n{context}\n" \
               "Your documentation should be in Markdown."
