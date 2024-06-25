from db_agent import invocar_agente
from chart_model import generar_imagen_codificada, ejecutar_codigo_grafico
from config import load_config

def main():
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Chau!")
            break
        output = invocar_agente(user_input)
        informacion = output["output"]
        # Generar un posible código de gráfico
        img_64 = generar_imagen_codificada(informacion, user_input)
        print(img_64)

if __name__ == '__main__':
    load_config()
    main()
    