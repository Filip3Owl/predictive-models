import os
import pandas as pd

def find_and_load_student_data():
    # Possíveis locais do arquivo
    possible_paths = [
        'data/student-mat.csv',
        './data/student-mat.csv',
        '../data/student-mat.csv',
        'venv/data/student-mat.csv',
        './venv/data/student-mat.csv'
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f'Arquivo encontrado em: {path}')

    print("Arquivo não encontrado. Procurando arquivos CSV...")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.csv'):
                print(f"CSV encontrado: {os.path.join(root, file)}")

    raise FileNotFoundError("student-mat.csv não encontrado nos locais comuns")


df = find_and_load_student_data()