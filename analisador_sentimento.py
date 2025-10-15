import pandas as pd
import re
import matplotlib.pyplot as plt

def classificar_sentimento(comentario: str):
    comentario = comentario.lower()
    positivo = len(re.findall(r'\b(amo|adoro|excelente|ótimo|satisfeito|perfeito|superou|rápido|eficiente|resolveram)\b', comentario))
    negativo = len(re.findall(r'\b(pior|ruim|decepcionado|danificado|nada especial|mediana|não gostei)\b', comentario))
    if positivo > negativo:
        return 'Positivo'
    elif negativo > positivo:
        return 'Negativo'
    else:
        return 'Neutro'


df_comentarios = pd.DataFrame({'comentario': [
    "Eu amo este produto! Funciona perfeitamente.",
    "Este é o pior serviço que já usei.",
    "O atendimento foi razoável, nada especial.",
    "Produto excelente, superou minhas expectativas!",
    "Não gostei do sabor, muito ruim.",
    "Entrega rápida e eficiente, muito satisfeito.",
    "O produto chegou danificado, muito decepcionado.",
    "Atendimento ao cliente foi ótimo, resolveram meu problema rapidamente.",
    "A qualidade do produto é mediana, poderia ser melhor.",]})

df_comentarios['sentimento'] = df_comentarios['comentario'].apply(classificar_sentimento)
print(df_comentarios)
contagem = df_comentarios['sentimento'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(contagem.index, contagem.values, color=['red', 'green', 'gray'])
plt.title('Distribuição de Sentimentos dos Comentários')
plt.xlabel('Sentimento')
plt.ylabel('Número de Comentários')

plt.figure(figsize=(8, 5))
plt.pie(contagem.values, labels=contagem.index, autopct='%1.1f%%', colors=['red', 'green', 'gray'])
plt.title('Distribuição de Sentimentos dos Comentários')
plt.show()