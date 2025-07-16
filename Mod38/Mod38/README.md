# 💳 Credit Scoring - Projeto Final

Este projeto foi desenvolvido como parte do Módulo 38, com o objetivo de aplicar técnicas de Machine Learning para previsão de inadimplência de clientes.

## 🔧 Tecnologias Utilizadas
- Python 3.10
- PyCaret
- Streamlit
- LightGBM
- Pandas

## ⚙️ Funcionalidades
- Upload de base CSV com dados dos clientes
- Pipeline automático de pré-processamento
- Escoragem com modelo LightGBM treinado
- Exibição da probabilidade de inadimplência
- Download da base escorada

---

## ▶️ Demonstração em Vídeo

<video width="100%" controls>
  <source src="video_demonstracao.mp4" type="video/mp4">
  Seu navegador não suporta a visualização do vídeo.
</video>

---

## 🧪 Como executar

```bash
# Clone o repositório
git clone https://github.com/JessicaMitsuoka/Ebac-DataScience.git

# Acesse a pasta
cd Ebac-DataScience/Mod38

# Ative o ambiente correto (ex: pycaret310)
conda activate pycaret310

# Rode o app Streamlit
streamlit run app_credit_scoring.py
