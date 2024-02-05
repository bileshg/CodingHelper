import os
import streamlit as st
from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate

from prompts import Prompt

os.environ["OPENAI_API_KEY"] = st.secrets["chatgpt-API-key"]


def process(task, language, context):
    template, temperature = Prompt[task.upper().replace(" ", "_")].value
    prompt = PromptTemplate(
        input_variables=["language", "context"],
        template=template
    )
    llm = OpenAI(model_name='gpt-4o', temperature=temperature, max_tokens=2048)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(language=language, context=context)


def main():
    st.title("🖥️ Coding Helper")
    st.write("This app is a coding assistant that can help you with your code-related tasks.")

    with st.sidebar:
        st.subheader("Features")
        st.write("It can help you with the following tasks:")
        st.markdown(
            "- **Explain** code snippets\n"
            "- **Generate** code based on requirements\n"
            "- **Answer** programming-related questions\n"
            "- **Document** code snippets"
        )
        st.subheader("Usage")
        st.markdown(
            "1. Select the **type of assistance** you need\n"
            "2. Select the programming **language** you need help with\n"
            "3. Enter the **code or requirements** you need help with\n"
            "4. Click the **Execute** button to get your result"
        )

    col1, col2 = st.columns(2)

    with col1:
        task = st.selectbox(
            "Type of Assistance", (
                "Explain",
                "Generate",
                "Answer",
                "Document"
            )
        )

    with col2:
        language = st.selectbox(
            "Language", (
                "Python",
                "Java",
                "JavaScript",
                "TypeScript",
                "C",
                "C++",
                "C#",
                "Go",
                "Ruby",
                "Rust",
                "Haskell",
                "Scala",
                "Kotlin",
                "Swift",
                "Julia"
            )
        )

    context = st.text_area(
        "Code/Requirements",
        height=200,
        max_chars=1500,
        placeholder="Enter your code or requirements here..."
    )

    if st.button('Execute'):
        response_area = st.empty()
        with st.spinner('Fetching results...'):
            response = process(task, language, context)
        response_area.write(response)


if __name__ == '__main__':
    main()
