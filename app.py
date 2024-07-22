from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/interpret', methods=['POST'])
def interpret():
    try:
        # Obtiene los datos JSON del cuerpo de la solicitud
        data = request.json
        input_text = data.get('input')
        
        if not input_text:
            return jsonify({'error': 'No input provided'}), 400

        # Configura y llama al modelo Ollama
        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': input_text,
                },
            ]
        )
        
        # Obtiene la respuesta del modelo
        model_response = response.get('message', {}).get('content', '')

        # Retorna la respuesta en formato JSON
        return jsonify({'response': model_response})
    
    except Exception as e:
        # Manejo de errores
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
