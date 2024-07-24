### LLaMa 3 - FREE AND LOCAL - CHATGPT clone

<img src="https://github.com/lefevbre-organization/llama3/blob/main/ia.jpg" width="400">

### Experiment Workflow Description

This experiment integrates Ollama with the LLaMa3 model running locally in Docker, exposing an API at `:11434/api/generate`. Additionally, there is another container running a Python Flask API that calls the Ollama API. We have a client installed as an add-on in Google Gmail for seamless integration.

#### Workflow Steps:
1. Set up the Docker environment to run the LLaMa3 model with Ollama integration.
2. Expose the RESTful API endpoint `:11434/api/generate` for the LLaMa3 model.
3. Implement a Python Flask API in another container to interact with the Ollama API.
4. Stabilize connectivity between the Flask API and Ollama for data processing.
5. Install the custom client add-on in Google Gmail for streamlined communication with the integrated system.

**Use Case:**
- **Scenario:** A user selects an email and uses a text box to input a prompt "I want an automatic response to be written and saved as a draft."
  
**Next Steps (To-Do):**
- Implement an "Open interpreter" for the automatic execution of tasks using the LLM of LLaMa3 via [Open Interpreter](https://www.openinterpreter.com).

**Additional Use Case with Open interpreter:**
- **Scenario:** A user requests that the selected email, which has a PDF attachment, be converted to DOCX format.

This workflow represents a seamless interaction between Ollama, LLaMa3 model, Python Flask API, Google Gmail add-on, and Open Interpreter for optimized experimental outcomes.
- Other necessary files and directories for your application.

## Contributions

If you wish to contribute improvements or fixes, feel free to do so through Pull Requests. Any suggestions are welcome.

