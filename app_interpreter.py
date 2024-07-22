from flask import Flask, request, jsonify
from interpreter import interpreter  # Ajusta esto según la API del paquete

app = Flask(__name__)

@app.route('/interpret', methods=['POST'])
def interpret():
    try:
        # Obtiene los datos JSON del cuerpo de la solicitud
        data = request.json
        input_text = data.get('input')
        
        if not input_text:
            return jsonify({'error': 'No input provided'}), 400

        #Configura el intérprete para usar LLaMA 3
         
        interpreter.offline = True
        interpreter.llm.model = "ollama/llama3"
        interpreter.auto_run = False



        # Llama a la función del intérprete
        response = interpreter.chat(input_text)  # Ajusta esto según la función del paquete
        
        # Retorna la respuesta en formato JSON
        return jsonify({'response': response})
    
    except Exception as e:
        # Manejo de errores
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

