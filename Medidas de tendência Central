import statistics

# Função para calcular a média
def calcularMedia(valores):
    return statistics.mean(valores)

# Função para calcular a mediana
def calcularMediana(valores):
    return statistics.median(valores)

# Função para calcular o desvio padrão
def calcularDesvioPadrao(valores):
    return statistics.stdev(valores)

# Função para calcular a moda
def calcularModa(valores):
    try:
        return statistics.mode(valores)
    except statistics.StatisticsError:
        return "Nenhuma moda encontrada"

# Função principal
def main():
    print("Calculadora de Estatísticas Simples em Python")
    
    # Solicitar ao usuário que insira os números separados por espaços
    entrada = input("Digite os números separados por espaços: ")
    
    # Converter a entrada em uma lista de números
    valores = [float(x) for x in entrada.split()]
    
    # Verificar se a entrada é válida
    if len(valores) == 0:
        print("Entrada inválida. Certifique-se de inserir números separados por espaços.")
        return
    
    # Calcular e exibir a média, mediana, moda e desvio padrão
    media = calcularMedia(valores)
    mediana = calcularMediana(valores)
    moda = calcularModa(valores)
    desvio_padrao = calcularDesvioPadrao(valores)
    
    print("\nResultados:")
    print("Média:", media)
    print("Mediana:", mediana)
    print("Moda:", moda)
    print("Desvio Padrão:", desvio_padrao)

# Chamada da função principal
if __name__ == "__main__":
    main()
