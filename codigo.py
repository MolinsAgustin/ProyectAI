import matplotlib.pyplot as plt
from langchain_experimental.tools.python.tool import PythonREPL

codigo = "import matplotlib.pyplot as plt\nimport io\n\ndef generar_grafico():\n    paises = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'Czech Republic', 'Denmark', 'Finland']\n    ventas = [37.62, 37.62, 42.62, 37.62, 190.10, 303.96, 46.62, 90.24, 37.62, 41.62]\n    \n    plt.figure(figsize=(6, 4))\n    plt.barh(paises, ventas, color='skyblue')\n    plt.xlabel('Ventas Totales ($USD)')\n    plt.ylabel('Países')\n    plt.title('Ventas Totales por País')\n    plt.tight_layout()\n    \n    buffer = io.BytesIO()\n    plt.savefig(buffer, format='png')\n    buffer.seek(0)\n    \n    return buffer"
nombre_func = 'generar_grafico()'
exec(codigo)
buffer = eval(nombre_func)

import matplotlib.pyplot as plt
from PIL import Image
 
# Convertir el buffer a una imagen PIL y mostrarla
image = Image.open(buffer)
image.show()
