import pandas as pd
import json

def gerar_dados():
    file_path = "BASE COTAÇÕES_saude.xlsx"
    sheet_name = "SAÚDE"
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        cols = [
            "ANALISTA", "DATA DA ANÁLISE", "NÚMERO DA COTAÇÃO", "CENÁRIO", 
            "CONGÊNERE", "PRODUTO", "CNPJ", "NOME DA EMPRESA", "VIDAS", "DA", "ML",
            "DILUIÇÃO", "AGENCIAMENTO", "COMISSÃO", "AGRAVO/DESCONTO", "REAJUSTE ANUAL", 
            "REDE", "ESTIMATIVA DE FATURA", "COPARTICIPAÇÃO", "FATURAMENTO MACRO", 
            "FATURAMENTO NECESSÁRIO", "SITUAÇÃO", "OBSERVAÇÕES", "CORRETOR", 
            "ESCRITÓRIO REGIONAL", "RELATÓRIO DE SINISTRALIDADE", "TIPO DE CONTRATAÇÃO", 
            "SINISTRALIDADE CONGÊNERE", "PRIORIDADE", "CHANCE FECHAMENTO", "ORIGEM", 
            "APRESENTOU VIDA?"
        ]
        
        existing_cols = [col for col in cols if col in df.columns]
        df = df[existing_cols]
        df = df.dropna(subset=['CNPJ'])
        
        for col in df.select_dtypes(include=['datetime64']).columns:
            df[col] = df[col].dt.strftime('%d/%m/%Y')
            
        df = df.fillna("")
        records = df.to_dict(orient='records')
        
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
            
        print(f"Sucesso! {len(records)} registros salvos em dados.json.")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == '__main__':
    gerar_dados()