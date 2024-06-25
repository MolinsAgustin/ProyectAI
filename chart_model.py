from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.tools.python.tool import PythonREPL
from typing import Optional
from dotenv import load_dotenv
import os
import base64
import matplotlib.pyplot as plt
import io

load_dotenv()

# Get the OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

class Grafico(BaseModel):
    """Informacion para la generación de un gráfico si corresponde."""
    comments: Optional[str] = Field(description="Comentarios adicionales acerca del codigo brindado")
    codigo: Optional[str] = Field(description="Codigo fuente para generar el codigo en python. Limitarse a brindar unicamente el codigo aqui sin ningun comentario adicional")
    funcion: Optional[str] = Field(description="Nombre de la funcion generada en codigo")

template_grafico = """Eres experto en python y en analisis de datos. 
            Con la informacion genera un codigo de python (solo si la respuesta tiene más de 5 datos) para la generación de un grafico.
            El codigo debe generar una funcion que genere el grafico y retornarlo como un buffer de bytes. La ejecucion de este codigo a posterior sera almacenado en una variable,
            por lo que debe ser importante que la funcion retorne el buffer de bytes.
            Informacion: {informacion}

            El codigo generado debe tener una estructura similar a la siguiente:

            import matplotlib.pyplot as plt
            import io

            def generar_grafico():
                # Datos de ejemplo
                nombre_datos = [ ] #Crear lista con los elementos necesarios
                datos = [ ] #Crear lista con los elementos necesarios
                
                # Crear la figura y el gráfico de barras horizontales
                plt.figure(figsize=(6, 4))

                # agregar estilos segun corresponda
                
                plt.xticks(rotation=90)
                plt.xlabel('Agregar texto eje x')
                plt.ylabel('Agregar texto eje y')
                plt.title('Agregar titulo')
                plt.tight_layout()
                
                
                # Guardar el gráfico en un buffer
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                
                return buffer
                
            Adicionalmente te envío la consulta original del usuario, para ayudarte a determinar si es necesario o no un grafico: {consulta}. 
            Eres a su vez diseñador grafico, por lo tanto el grafico debe quedar bonito, debe quedar con estilo empresarial y pero elegante.
            IMPORTANTE el grafico debe ser muy pequeño.
            """

prompt_template = PromptTemplate(
    template=template_grafico, input_variables=["informacion"]
)

llm2 = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", api_key=openai_api_key)

structured_llm = llm2.with_structured_output(schema=Grafico)

chain_grafico = prompt_template | structured_llm

def generar_codigo_grafico(informacion, consulta):
    output_grafico = chain_grafico.invoke({"informacion": informacion, "consulta": consulta})
    print(output_grafico)
    codigo = output_grafico.codigo
    nombre_func = output_grafico.funcion
    return codigo, nombre_func

def generar_grafico_base64(informacion,consulta):
    print('hola')

def generar_buffer_bytes_img(informacion,consulta):
    codigo, nombre_func = generar_codigo_grafico(informacion, consulta)
    ejecutar_codigo_grafico(codigo)
    nombre_func = nombre_func + '()'
    buf = ejecutar_codigo_grafico(nombre_func)
    return buf

def codificar_imagen(buf):
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_base64

def generar_imagen_codificada(informacion,consulta):
    codigo, nombre_func = generar_codigo_grafico(informacion, consulta)
    if codigo:
        exec(codigo)
        nombre_func = nombre_func + '()'
        buffer = eval(nombre_func)
        img_64 = codificar_imagen(buffer)
        print(img_64)
        return img_64
    return None


def ejecutar_codigo_grafico(codigo):
    if codigo:
        python_repl = PythonREPL()
        python_repl.run(codigo)