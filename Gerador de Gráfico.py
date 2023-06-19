import matplotlib.pyplot as plt
import numpy as np

def generate_chart(data, title, x_label, y_label):
    categories = [f'Categoria {i+1}' for i in range(len(data))]
    plt.bar(categories, data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

if __name__ == '__main__':
    data = [10, 20, 30, 40]
    generate_chart(data, 'Meu Gráfico', 'Categorias', 'Valores')
