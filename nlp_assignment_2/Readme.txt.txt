# NLP Assignment 2 Q1

Ensure you are inside the word_language_model directory
To train the FNN model for 6 epochs run the first command\
To train the FNN 8 gram model run the second command\
To train the FNN model without weight sharing specify tie_weights=false in the FNNmodel constructor\
To generate text with the saved model use the last command

```bash 
python main.py --cuda --lr 2 --epochs 6 --model FNN
python main.py --cuda --lr 2 --epochs 6 --model FNN --bptt 8
python generate.py --cuda --checkpoint model.pt
```

# NLP Assignment 2 Q2
To run the ipython notebook call '''jupyter notebook''' in the terminal in the End-to-end-Sequence-Labeling-via-Bi-directional-LSTM-CNNs-CRF-Tutorial directory. 
Glove files were excluded and are fetched in the jupyter notebook itself so just select run all.

To change parameters to test for different layers specify them in the constructor of the BiLSTM_CRF class. Examples would be as follows:
* model = BiLSTM_CRF(vocab_size=len(word_to_id),
                    ...
                    ...
                    n_layers=2,
                    CNN_mode='2D',
                    window_size=11)

For some of the experiments listed in the report, hyperparameters were changed in the code itself. For example, changing the kernel size of different layers.
