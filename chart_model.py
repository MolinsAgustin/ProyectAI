from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.tools.python.tool import PythonREPL
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

# Get the OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

class Grafico(BaseModel):
    """Informacion para la generación de un gráfico si corresponde."""
    comments: Optional[str] = Field(description="Comentarios adicionales acerca del codigo brindado")
    codigo: Optional[str] = Field(description="Codigo fuente para generar el codigo en python. Limitarse a brindar unicamente el codigo aqui sin ningun comentario adicional")

template_grafico = """Eres experto en python y en analisis de datos. 
            Con la informacion genera un codigo de python (solo si la respuesta tiene más de 5 datos) para la generación de un grafico.
            Informacion: {informacion}
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

def generar_grafico(informacion, consulta):
    output_grafico = chain_grafico.invoke({"informacion": informacion, "consulta": consulta})
    return output_grafico.codigo

def generar_grafico_base64(informacion,consulta):
    print('hola')


def ejecutar_codigo_grafico(codigo):
    if codigo:
        python_repl = PythonREPL()
        python_repl.run(codigo)