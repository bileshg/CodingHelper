from enum import Enum


class Prompt(Enum):
    EXPLAIN = ("I want you to act as a code explainer in {language}. "
               "I don't understand the following code snippet. "
               "Can you please explain what it does, and, also, provide an example?"
               "\n{context}\n"
               "You can assume that the code snippet is correct.",
               0.7)
    GENERATE = ("Write a program in {language} based on the provided requirements."
                "\n{context}\n"
                "Your response should be in Markdown.",
                0)
    ANSWER = ("I want you to act as a StackOverflow post written by an "
              "Expert {language} Programmer with 25 years of experience. "
              "I will ask programming-related questions and "
              "you will reply with what the answer should be as a Markdown document. "
              "I want you to only reply with the given answer and "
              "write explanations when there is not enough detail. "
              "Do not write explanations. My first question is:"
              "\n{context}",
              0.8)
    DOCUMENT = ("Generate a README.md file explaining the following {language} code."
                "\n{context}\n"
                "Your response should be in Markdown.",
                0.5)
