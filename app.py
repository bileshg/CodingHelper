from enum import Enum
import streamlit as st
import openai

openai.api_key = st.secrets["chatgpt-API-key"]


class Prompt(Enum):
    EXPLAIN = "I want you to act as a code explainer in %s. " \
              "I don't understand the following code snippet. " \
              "Can you please explain what it does, and, also, provide an example?" \
              "You can assume that the code snippet is correct. Your response should be in Markdown."
    GENERATE = "Write a program in %s based on the following requirements. Your program should be in Markdown."
    DEBUG = "I want you to act as a %s debugger. " \
            "The following code snippet does not work as intended. " \
            "Can you please explain why it does not work, and, also, provide the fix for it?" \
            "Your response should be in Markdown."
    ANSWER = 'I want you to act as a StackOverflow post written by an ' \
             'Expert %s Programmer with 25 years of experience. ' \
             'I will ask programming-related questions and ' \
             'you will reply with what the answer should be as a Markdown document. ' \
             'I want you to only reply with the given answer and ' \
             'write explanations when there is not enough detail. ' \
             'Do not write explanations. My first question is:'
    OPTIMIZE = "I want you to act as a code optimizer in %s. " \
               "Can you make the following code snippet more efficient so that it runs faster? " \
               "You can assume that the code snippet is correct. Your response should be in Markdown."
    REFACTOR = "I want you to act as a code optimizer in %s. " \
               "Can you make the following code snippet cleaner and more readable? " \
               "You can assume that the code snippet is correct. Your response should be in Markdown."
    DOCUMENT = "Write documentation for the following %s code. Your documentation should be in Markdown."

    def get_text(self, language):
        return self.value % language


def ask_gpt(prompt, model='text-davinci-003', temperature=0.7):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def execute_query(prompt, language, context):
    return ask_gpt(f'{prompt.get_text(language)}\n{context}')


def main():
    st.title("Coding Helper")

    col1, col2 = st.columns(2)

    with col1:
        task = st.selectbox(
            "Type of Assistance", (
                "Explain",
                "Generate",
                "Debug",
                "Answer",
                "Optimize",
                "Refactor",
                "Document"
            )
        )

    with col2:
        language = st.selectbox(
            "Language", (
                "Python",
                "Java",
                "JavaScript",
                "SQL"
            )
        )

    context = st.text_area(
        "Code/Requirements",
        height=200,
        max_chars=1500,
        placeholder="Enter your code or requirements here..."
    )

    if st.button('Execute'):
        prompt = Prompt[task.upper().replace(" ", "_")]
        response = execute_query(prompt, language, context)
        st.write(response)


if __name__ == '__main__':
    main()
