import numpy as np

learning_rate = 0.1
epochs = 10000
    
input_size = 2
hidden_size = 3
output_size = 1

weights_input_hidden = np.random.randn(input_size, hidden_size)
bias_hidden = np.zeros((1, hidden_size))

weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_output = np.zeros((1, output_size))

hidden_output = np.zeros((4, 3)) # for sake of global variable.

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
def sigmoid_derivative(x):
    return x * (1 - x)
    
def forward(x):
    
    hidden_input = np.dot(x, weights_input_hidden) + bias_hidden
    global hidden_output
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_input)
    
    return final_output
    
def backpropagation(x, y, output):

    error = y - output
    
    d_output = error * sigmoid_derivative(output)

    global weights_hidden_output
    global weights_input_hidden
    
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    
    weights_hidden_output += learning_rate * hidden_output.T.dot(d_output)
    weights_input_hidden  += learning_rate * x.T.dot(d_hidden)
    
    global bias_hidden
    global bias_output
    
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
    
def trainnn():
    # training
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    for epoch in range(epochs):
        output = forward(X)
        backpropagation(X, y, output)
    
    # typical traing flow in pytorch
    # for epoch in range(epochs):
        # optimizer.init()
        
        # pred = forward(X)
        # loss = loss_fn(pred, y)
        # backpropagation(loss)
        # optimizer.step()
    
    print("training done.")
    tX = np.array([[0, 0], [1, 1]])
    t2X = np.array([[1, 0], [0, 1]])
    output = forward(t2X)
    print("NN prediction after trainging...")
    print(output)
    
    
    
    
    