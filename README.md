# Proyecto LaTeX en Formato APA 7

Este proyecto contiene un documento LaTeX en español siguiendo el formato APA 7.

## Estructura del Proyecto

- `src/`: Contiene los archivos fuente
  - `main.tex`: Documento principal
  - `capitulos/`: Contiene los capítulos del documento
  - `referencias.bib`: Archivo BibTeX con las referencias
- `dist/`: Contendrá el PDF generado
- `compile.py`: Script para compilar el documento

## Requisitos

- Python 3.x
- LaTeX (con pdflatex y bibtex)
- Paquetes LaTeX:
  - babel-spanish
  - apacite
  - csquotes
  - setspace
  - geometry
  - graphicx
  - hyperref

## Uso

1. Asegúrate de tener instalados todos los requisitos
2. Ejecuta el script de compilación:
   ```bash
   python compile.py
   ```
3. El PDF generado se encontrará en la carpeta `dist/`

## Edición del Documento

- Modifica `main.tex` para cambiar la configuración general
- Edita los archivos en `capitulos/` para modificar el contenido
- Actualiza `referencias.bib` para gestionar las referencias bibliográficas
