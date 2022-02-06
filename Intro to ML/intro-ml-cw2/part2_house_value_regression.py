import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer
from sklearn.metrics import mean_squared_error

torch.manual_seed(15)


class Regressor(nn.Module):

    def __init__(self, x, layers = 10, hidden_size = 20, batch_size = 50, learning_rate = 0.0001, dropout = 0.3, nb_epoch = 500):
        ### TO DO: edit default values of parameters, add docstrings
        """ 
        Initialise the model.
          
        Arguments:
            - x {pd.DataFrame} -- Raw input data of shape 
                (batch_size, input_size), used to compute the size 
                of the network.
            - nb_epoch {int} -- number of epoch to train the network.

        """

        #######################################################################
        #                       ** START OF YOUR CODE **
        #######################################################################
        super(Regressor, self).__init__ ()

        self.label_binarizer = LabelBinarizer()

        #self.training_means = None
        #self.training_stds = None
        self.training_mins = None
        self.training_maxs = None
        print(f">>>>>>preprocessing called in __init__ method with {type(x)}")
        X, _ = self._preprocessor(x, training = True)
        #print(type(X))
        #print(X.shape)
        self.input_size = X.shape[1]
        self.output_size = 1 # Only one neuron for the output layer
        self.layers = layers 
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.dropout = nn.Dropout(dropout)
        self.nb_epoch = nb_epoch
        
        
        # First tranformation from the network input to the input of first hidden layer
        self.input_layer = nn.Linear(self.input_size, self.hidden_size) 
        # All the hidden transformation
        self.hidden_layers = nn.ModuleList([nn.Linear(self.hidden_size, self.hidden_size) for _ in range(layers-1)])
        # Last tranformation from the last hidden layer output to the network output
        self.output_layer = nn.Linear(self.hidden_size, self.output_size) 


        #######################################################################
        #                       ** END OF YOUR CODE **
        #######################################################################

    def _preprocessor(self, x, y = None, training = False):
        """ 
        Preprocess input of the network.
          
        Arguments:
            - x {pd.DataFrame} -- Raw input array of shape 
                (batch_size, input_size).
            - y {pd.DataFrame} -- Raw target array of shape (batch_size, 1).
            - training {boolean} -- Boolean indicating if we are training or 
                testing the model.

        Returns:
            - {torch.tensor} or {numpy.ndarray} -- Preprocessed input array of
              size (batch_size, input_size).
            - {torch.tensor} or {numpy.ndarray} -- Preprocessed target array of
              size (batch_size, 1).

        """
        #######################################################################
        #                       ** START OF YOUR CODE **
        #######################################################################

        # 1. Store preprocessing parameters based on the training data
        if training:
            # standardization constants
            #self.training_means = x.mean()
            #self.training_stds =  x.std()

            # normalizing constants
            self.training_mins = x.min().iloc[:-1]
            self.training_maxs = x.max().iloc[:-1]
            
            # mapping from categorical values to integer encoding
            self.label_binarizer.fit(x['ocean_proximity'])
        
        # 2. Handle the missing values in the data, for example setting them to a default value.
        median_train_bedrooms = x["total_bedrooms"].median()
        x["total_bedrooms"].fillna(median_train_bedrooms, inplace=True)

        # 3. Eventually normalise the numerical values to improve learning (only for categorical values)
        numerical_df = x.loc[:, x.columns != 'ocean_proximity']
        normalized_data = (numerical_df - self.training_mins) / (self.training_maxs - self.training_mins)

        # 4. Handle the textual values in the data, encoding them using one-hot encoding
        proximity_one_hot_encoding = self.label_binarizer.transform(x['ocean_proximity'])
        # and stacking them to the dataset: each possible category is now a binary feature
        numerical_features = np.hstack((normalized_data, proximity_one_hot_encoding)) .astype(float)  

        # Improvement: If y is na, drop the  in x as well. A non-labeled instance cannot be used for a supervised learning task

        # 6. Return torch.tensors objects
        #y = torch.from_numpy(y.values).float()
        x = torch.Tensor(numerical_features)
        
        # Return preprocessed x and y, return None for y if it was None
        return x, (torch.Tensor(y.values) if isinstance(y, pd.DataFrame) else None)
        # return x, (y if isinstance(y, pd.DataFrame) else None)

        #######################################################################
        #                       ** END OF YOUR CODE **
        #######################################################################


    # Define the forward pass given the input data
    def forward(self, X):
        """
        Get the output of the neural network.
        Input: X {tensor} - one element or a batch of element
        Ouput: X {tensor} - corresponding output
        """
        # Passing through the input layer
        X = self.input_layer(X) 

        # Applying Relu activation
        X = F.relu(X) 

        for layer in self.hidden_layers:
            X = layer(X) # Passing through each hidden layer
            X = F.relu(X) # Applying Relu activation

        # Passing through the output layer
        X = self.output_layer(X) 

        return X


    def fit(self, x, y):
        """
        Regressor training function

        Arguments:
            - x {pd.DataFrame} -- Raw input array of shape 
                (batch_size, input_size).
            - y {pd.DataFrame} -- Raw output array of shape (batch_size, 1).

        Returns:
            self {Regressor} -- Trained model.

        """

        #######################################################################
        #                       ** START OF YOUR CODE **
        #######################################################################
        print(f">>>>>>preprocessing called in fit method with {type(x)}")
        X, Y = self._preprocessor(x, y = y, training = True)
        
        # Create the model 
        criterion = nn.MSELoss() # Use the mean-square error loss
        optimiser = optim.Adam(self.parameters(), lr = self.learning_rate) # Use the Adam optimiser
        
        for epoch in range(self.nb_epoch):
            for data in train_loader:
                inputs, output = data
                
                # Reset the gradients 
                optimiser.zero_grad()   

                # Forward pass
                output_hat = self.forward(inputs)

                # Compute the loss
                loss = criterion(output_hat, output) 

                # Backward pass (compute the gradients)
                loss.backward()

                # Update the parameters
                optimiser.step() 

        # print(list(self.parameters()))
        
        return self

        #######################################################################
        #                       ** END OF YOUR CODE **
        #######################################################################

            
    def predict(self, x):
        """
        Ouput the value corresponding to an input x.

        Arguments:
            x {pd.DataFrame} -- Raw input array of shape 
                (batch_size, input_size).

        Returns:
            {np.darray} -- Predicted value for the given input (batch_size, 1).

        """

        #######################################################################
        #                       ** START OF YOUR CODE **
        #######################################################################
        print(f">>>>>>preprocessing called in predict method with {type(x)}")
        X, _ = self._preprocessor(x, training = False) 
        y_pred = self.forward(X)

        return y_pred.detach().numpy()

        #######################################################################
        #                       ** END OF YOUR CODE **
        #######################################################################

    def score(self, x, y):
        """
        Function to evaluate the model accuracy on a validation dataset.

        Arguments:
            - x {pd.DataFrame} -- Raw input array of shape 
                (batch_size, input_size).
            - y {pd.DataFrame} -- Raw ouput array of shape (batch_size, 1).

        Returns:
            {float} -- Quantification of the efficiency of the model.

        """

        #######################################################################
        #                       ** START OF YOUR CODE **
        #######################################################################
        print(f">>>>>>preprocessing called in score methode with {type(x)}")
        X, Y = self._preprocessor(x, y = y, training = False) 
        Y_pred = self.predict(x)
        print(Y_pred)

        # Compute the mean-squared error
        mse = mean_squared_error(Y.numpy(), Y_pred) 
        return mse

        #######################################################################
        #                       ** END OF YOUR CODE **
        #######################################################################


def save_regressor(trained_model): 
    """ 
    Utility function to save the trained regressor model in part2_model.pickle.
    """
    # If you alter this, make sure it works in tandem with load_regressor
    with open('part2_model.pickle', 'wb') as target:
        pickle.dump(trained_model, target)
    print("\nSaved model in part2_model.pickle\n")


def load_regressor(): 
    """ 
    Utility function to load the trained regressor model in part2_model.pickle.
    """
    # If you alter this, make sure it works in tandem with save_regressor
    with open('part2_model.pickle', 'rb') as target:
        trained_model = pickle.load(target)
    print("\nLoaded model in part2_model.pickle\n")
    return trained_model


def crossVal(x, y, layers, hidden_size, batch_size, learning_rate):
    kf = KFold(3) # Do the KFold with K = 3
    mse_results = []
    for train_index, val_index in kf.split(x):
        # Split the training in 2 parts (train & validation)
        x_train, x_val = x[train_index], x[val_index]
        y_train, y_val = y[train_index], y[val_index]
        
        regressor = Regressor(x_train, y_train, layers, hidden_size, batch_size, learning_rate, dropout = 0.3, nb_epoch = 500) # Not tuning drop_out rate, nb_epoch here
        
        mse_results.append(regressor.score(x_val, y_val))
        average_mse = np.mean(np.array(mse_results))
        
        print("The averaged MSE across 3 folds", average_mse)
        return average_mse



def RegressorHyperParameterSearch(x, y, params): 
    # TO DO: add arguments to the docstring
    """
    Performs a hyper-parameter grid-search for fine-tuning the regressor implemented 
    in the Regressor class.

    Arguments:
        # TO BE ADDED
        
    Returns:
        The function should return your optimised hyper-parameters. 

    """

    #######################################################################
    #                       ** START OF YOUR CODE **
    #######################################################################
    best_mse = 10000000000
    best_hidden_size, best_layers, best_batch, best_lr = 0, 0, 0, 0
    new_dict = {}
    
    # Find the best hyperparameters with for loops
    for i in range(len(params[’layers’])):
        for j in range(len(params[’hidden_size’])):
            for k in range(len(params[’batch_size’])):
                for u in range(len(params[’learning_rate’])):
                    mse = crossVal(x, y, params[’layers’][i], params[’hidden_size’][j], \
                                      params[’batch_size’][k], params[’learning_rate’][u])
                    new_dict['(params[’layers’][i], params[’hidden_size’][j], \
                               params[’batch_size’][k], params[’learning_rate ’][u])'] = mse
                    
                    if mse < best_mse:
                        best_mse = mse
                        best_layers = params[’layers’][i]
                        best_hidden = params[’hidden_size’][j]
                        best_batch_size = params[’batch_size’][k]
                        best_lr = params[’learning_rate’][u]
                        
    print(best_layers, best_hidden_size, best_batch_size, best_mse)
    
    return best_layers, best_hidden_size, best_batch_size, best_lr, best_mse

    #######################################################################
    #                       ** END OF YOUR CODE **
    #######################################################################



def example_main():

    output_label = "median_house_value"

    # Use pandas to read CSV data as it contains various object types
    # Feel free to use another CSV reader tool
    # But remember that LabTS tests take Pandas Dataframe as inputs
    data = pd.read_csv("housing.csv") 

    # Leave out some held-out test set (25% of data) to make sure the model isn't overfitting
    # 25% is chosen so that in 3-fold CV, the validation set is around the same set as the test set
    training_data = data.sample(frac=0.75, random_state=25)
    testing_data = data.drop(training_data.index)

    # Spliting input and output
    x_train = training_data.loc[:, training_data.columns != output_label]
    y_train = training_data.loc[:, [output_label]]
    x_test = testing_data.loc[:, testing_data.columns != output_label]
    y_test = testing_data.loc[:, [output_label]]

    # Training
    regressor = Regressor(x_train, nb_epoch = 100)
    regressor.fit(x_train, y_train)
    save_regressor(regressor)

    # Error
    error = regressor.score(x_train, y_train)
    print("\nRegressor error: {}\n".format(error))


    # Parameters used in our RegressorHyperParameterSearch
    params= {’hidden_size’: [i for i in range (10, 50, 10)],
             ’layers’: [4,5,6,7],
             ’batch_size’: [30,40,50,60],
             ’learning_rate’: [0.5, 0.1, 0.01, 0.001]}

    grid_search_res = RegressorHyperParameterSearch(x_train, y_train, params)


if __name__ == "__main__":
    example_main()

