## This is my Undergraduate Final Year Project (FYP) on "Web-based Extension that uses LLMs to provide content summarization and quiz generation".

## The project is divided into two main parts:
### 1. Content Summarization
### 2. Quiz Generation
#### but also:
### 3. Personalization - focus on users with learning disabilities 


## How to use the Model
    ## Running Ollama and Langflow with Python Virtualenv

    This guide will help you get Ollama and LangFlow up and running using a Python virtual environment.

    ## Prerequisites

    - Python3
    - Virtualenv



    ## Create a virtual environment

    1. Download Ollama and Llam3 Model

        1. Visit [ollama.com](https://ollama.com/)
        2. Download and install Ollama
        3. Open a terminal window and download the llama3 model

            ```sh
            ollama run llama3
            ```

        Ensure that Llama3 is working before you proceed.

    2. Clone the Hackathon repository:

    ```sh
    git clone https://github.com/karanidenis/Capstone
    ```

    3. Navigate to the `Backend` directory:

    ```sh
    cd Backend
    ```

    3. Create a new virtualenv:

    ```sh
    python3 -m venv venv
    ```

    3. Activate the virtualenv:

    ```sh
    source env/bin/activate
    ```

    4. Install requirements

        ```sh
        pip install -r requirements.txt
        ```

    5. Run langflow

        ```sh
        python -m langflow run
        ```

    LangFlow will now be accessible at [http://localhost:7860/](http://localhost:7860/).
    Llama 3 via Ollama will now be available at [http://localhost:11434/](http://localhost:11434/).

    ## Run the apps

    ### Ollama - Langflow

    The examples enable you to:
    1. Ask Llama3 for summary of text content you provide
    2. Ask Llama3 for a summary of the content of webpage of the url you provide

    You must be in the `Backend` directory for the following:

    1. Ask Llama3 for summary of text content you provide

    ```sh
    python3 learnmate-model.py
    ```

    2. Ask Llama3 for a summary of the content of webpage of the url you provide

    ```sh
    python learnmate-url-model.py
    ```
