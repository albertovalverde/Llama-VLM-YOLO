### LLaMa 3 - FREE AND LOCAL - CHATGPT clone

<img src="https://github.com/lefevbre-organization/llama3/blob/main/ia.jpg" width="400">

### Experiment Workflow Description

This experiment integrates Ollama with the LLaMa3 model running locally in Docker, exposing an API at `:11434/api/generate`. Additionally, there is another container running a Python Flask API that calls the Ollama API. We will establish an interface through a Raspberry Pi 5 with an AI kit, commonly used for robotics applications.

#### Workflow Steps:
1. Set up the Docker environment to run the LLaMa3 model with Ollama integration.
2. Expose the RESTful API endpoint `:11434/api/generate` for the LLaMa3 model.
3. Implement a Python Flask API in another container to interact with the Ollama API.
4. Stabilize connectivity between the Flask API and Ollama for data processing.
5. Enable access to the integrated system through a Raspberry Pi 5 with an AI kit for streamlined communication and control.

  
**Next Steps (To-Do):**
- Implement an "Open interpreter" for the automatic execution of tasks using the LLM of LLaMa3 via [Open Interpreter](https://www.openinterpreter.com).

This workflow showcases the seamless integration of Ollama, LLaMa3 model, Python Flask API, and the Raspberry Pi 5 with AI kit, leveraging Open Interpreter for optimized experimental outcomes in a robotics-oriented context.
