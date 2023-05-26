# 💻 Coding Helper

This application is designed to assist with a variety of code-related tasks. Built with the Streamlit framework for Python, it leverages the `langchain` package to interact with OpenAI's language model to process tasks such as explaining, generating, debugging, answering, optimizing, refactoring, and documenting code.

## Setup

### Requirements
- Python 3.6 or higher
- Streamlit
- OpenAI (using `langchain` package)

### Installation

1. Clone this repository
2. Install the required packages
```bash
pip install streamlit langchain
```
3. Run the Streamlit app
```bash
streamlit run main.py
```

## Usage

The application interface is split into two sections: the main panel and a sidebar.

### Sidebar

The sidebar provides information about the application's features and how to use it.

### Main Panel

This is where you interact with the application. You can select the type of assistance you need, the programming language you're using, and the code or requirements that you need help with. The application currently supports Python, Java, and JavaScript.

- Type of Assistance: Options include 'Explain', 'Generate', 'Debug', 'Answer', 'Optimize', 'Refactor', and 'Document'.
- Language: The programming language you're working with.
- Code/Requirements: The code you want assistance with, or the requirements for generating code.

Once you've filled out these fields, click the 'Execute' button to process the request. The application will then display the response in the main panel.