import os
import subprocess
import shutil

def compile_latex():
    # Cambiar al directorio src
    os.chdir('src')
    
    # Compilar el documento LaTeX
    subprocess.run(['pdflatex', 'main.tex'])
    subprocess.run(['bibtex', 'main'])
    subprocess.run(['pdflatex', 'main.tex'])
    subprocess.run(['pdflatex', 'main.tex'])
    
    # Mover el PDF a la carpeta dist
    if os.path.exists('main.pdf'):
        shutil.move('main.pdf', '../dist/main.pdf')
        print("PDF generado exitosamente en la carpeta dist/")
    else:
        print("Error: No se pudo generar el PDF")

if __name__ == "__main__":
    compile_latex() 