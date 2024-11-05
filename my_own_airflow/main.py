import streamlit as st
import pandas as pd
import subprocess
import os

# Função para carregar os dados do arquivo CSV
def load_data():
    df = pd.read_csv("my_airflow/execution_logs.log")
    return df

# Função para executar o script Python com o ambiente virtual ativado
def run_python_script():
    # Caminho para o executável Python do ambiente virtual
    venv_python = os.path.join(".venv", "Scripts", "python.exe")
    
    # Executa o script usando o Python do ambiente virtual
    subprocess.run([venv_python, ".\\my_airflow\\pipeline\\pipeline.py"])

# Layout do aplicativo Streamlit
def main():
    st.title("Visualização de Logs e Execução de Scripts")
    st.image("my_airflow/pics/airflow_logo.png")

    # Carregar os dados do arquivo CSV
    df = load_data()

    # Exibir os dados na interface do Streamlit
    st.write("Logs de Execução:", df)

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        df = load_data()
        st.write("Dados Atualizados com Sucesso!")

    # Botão para executar o script Python
    if st.button("Executar Script Python"):
        run_python_script()
        st.write("Script Python executado com sucesso!")

if __name__ == "__main__":
    main()