from flask import Flask, request, jsonify
from db_agent import invocar_agente
from chart_model import generar_imagen_codificada
from config import load_config

app = Flask(__name__)

@app.route('/consulta', methods=['POST'])
def procesar_consulta():
    data = request.get_json()
    input_usuario = data['input_usuario']

    # Llamar al agente para procesar la consulta
    output = invocar_agente(input_usuario)
    informacion = output["output"]

    # Generar un posible código de gráfico
    img_64 = generar_imagen_codificada(informacion, input_usuario)

    print(img_64)
    # Preparar la respuesta JSON
    response = {
        "output": informacion,
        "grafico": img_64
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


