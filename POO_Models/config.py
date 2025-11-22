import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    @staticmethod
    def get_dataset_path():
        path = os.getenv(r'c:\Users\Felipe\Desktop\student-mat\data\student-mat.csv')
        if path and os.path.exists(path):
            return path
        
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        default = os.path.join(repo_root, "data", "student-mat.csv")
        if os.path.exists(default):
            return default
        
        raise ValueError(f"Erro: Variável DATASET não encontrado no .env e arquivo padrão ausente: {default}")