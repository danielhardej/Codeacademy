# The batch size is a hyperparameter that determines how many training samples are
# seen before updating the network’s parameters (weight and bias matrices).
#
# When the batch contains all the training examples, the process is called batch
# gradient descent. If the batch has one sample, it is called the stochastic
# gradient descent. And finally, when 1 < batch size < number of training points,
# is called mini-batch gradient descent. An advantage of using batches is for GPU
# computation that can parallelize neural network computations.
#
# So how do we choose the batch size for our model?

from model import features_train, labels_train, design_model
import matplotlib.pyplot as plt

def fit_model(f_train, l_train, learning_rate, num_epochs, batch_size, ax):
    model = design_model(features_train, learning_rate)
    #train the model on the training data
    history = model.fit(features_train, labels_train, epochs=num_epochs, batch_size = batch_size, verbose=0, validation_split = 0.3)
    # plot learning curves
    ax.plot(history.history['mae'], label='train')
    ax.plot(history.history['val_mae'], label='validation')
    ax.set_title('batch = ' + str(batch_size), fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('# epochs')
    ax.set_ylabel('mae')
    ax.legend()

#fixed learning rate
learning_rate = 0.1
#fixed number of epochs
num_epochs = 100
#we choose a number of batch sizes to try out
batches = [4, 32, 64] 
print("Learning rate fixed to:", learning_rate)

#plotting code
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0.7, 'wspace': 0.4}) #preparing axes for plotting
axes = [ax1, ax2, ax3]

#iterate through all the batch values
for i in range(len(batches)):
  fit_model(features_train, labels_train, learning_rate, num_epochs, batches[i], axes[i])

plt.savefig('static/images/my_plot.png')
print("See the plot on the right with batch sizes", batches)
import app
