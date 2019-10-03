# Hashtag Recommendation Tool
A hashtag recommendation tool implemented using Neuro-Linguistic Programming and Python.

### Tools and Technologies used:
tweepy, nltk, scikit-learn, keras, tensorflow, pandas, numpy.

## Implementation
### Data Extraction:
To begin with our project we extracted our dataset i.e. tweets from Twitter with the help of functions of tweepy library. The data is collected from a live stream of twitter data for a desired no. of tweets. The tweets are retrieved with the help of stream function and then filtered accordingly.

### Data Preprocessing:
The tweets extracted can’t be used as it is in our neural network model. For suitable features to be utilized data has to be preprocessed.
Firstly, the data is retrieved from the stored csv file into three different lists: date, tweets and hashtags. Now, tweets are treated as input and hashtags as output. These tweets are then tokenized with tokenize function and are broken into tokens. For this keras tokenizer library is used. We have raw text, but we want to make
predictions on a per-word basis. This means we must tokenize our comments into sentences, and sentences into words. We could just split each of the comments by spaces, but that wouldn’t handle punctuation properly. The sentence “He left!” should be 3 tokens: “He”, “left”, “!”.
Although, tweets are broken into useable tokens, these are still not ready for use as input features. These tokens contain many unrequired and repetitive tokens called stop words which have to be removed. After removing stop words we get the final set of features which is suitable to use for training model.

### Forming Dictionary:
With the help of Tokenized words a dictionary is formed containing tweets and hashtags. In which each word is mapped with a unique index.

### Vectorization of Features:
Vectorization is performed with the help of tokenizer.sequences_to_matrix, Label Encoder, keras.utils.to_categorical. Tokenizer sequence to matrix class allows to vectorize a text corpus, by turning each text into either a sequence of integers (each integer being the index of a token in a dictionary) or into a vector where the coefficient for each token could be binary, based on word count, based on tf-idf. Label Encoder is used to transform non-numerical labels (as long as they are hash able and comparable) to numerical labels. keras.utils.to_categorical Converts a class vector (integers) to binary class matrix.

### Training through RNN:
The idea behind RNNs is to make use of sequential information. In a traditional neural network we assume that all inputs (and outputs) are independent of each other. RNNs are called recurrent because they perform the same task for every element of a sequence, with the output being depended on the previous computations.
Another way to think about RNNs is that they have a “memory” which captures information about what has been calculated so far. A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. Often, sigmoid function refers to the special case of the logistic function shown in the first figure and defined by the formula Sigmoid functions have domain of all real numbers, with return value monotonically increasing most often from 0 to 1. The ReLU is the most used activation function in the world right now. Since, it is used in almost all the convolutional neural networks or deep learning. Its range is from 0 to infinity.

### Training through LSTM:
The key to LSTMs is the cell state. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged. The LSTM does have the ability to remove or add information to the cell state, carefully regulated by structures called gates. A sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. Often, sigmoid function refers to the special case of the logistic function shown in the first figure and defined by the formula Sigmoid functions have domain of all real numbers, with return value monotonically increasing most often from 0 to 1. The ReLU is the most used activation function in the world right now. Since, it is used in almost all the convolutional neural networks or deep learning. Its range is from 0 to infinity.
