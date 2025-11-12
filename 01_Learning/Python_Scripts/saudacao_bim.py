def saudacao_bim():
    """Saudação Personalizada para projetos BIM"""
    mensagem = "Bem-vindo ao Sistema BIM - Fábio Petronilho"
    return mensagem

def saudacao_personalizada(nome, projeto):
    """Saudação com dados do projeto"""
    return f"Olá {nome}! Trabalhando no projeto: {projeto}"

#Usando as funções
print(saudacao_bim())
print(saudacao_personalizada("Fábio", "Edifício Comercial"))