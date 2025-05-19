import numpy as np

# Funciones de activación y sus derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Datos de ejemplo (XOR)
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Parámetros de la red
input_size = 2
hidden_size = 4
output_size = 1
lr = 0.1  # tasa de aprendizaje
epochs = 10000

# Inicialización de pesos
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# Entrenamiento
for epoch in range(epochs):
    # Forward
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)

    # Cálculo del error
    error = y - output
    loss = np.mean(error ** 2)

    # Backpropagation
    d_output = error * sigmoid_deriv(output)
    d_hidden = np.dot(d_output, W2.T) * sigmoid_deriv(a1)

    # Actualización de pesos
    W2 += np.dot(a1.T, d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += np.dot(X.T, d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Resultados
print("Predicciones finales:")
print(output.round())