# NLP Assignment 1

NLP Assignment 1 source codes

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the [requirements.txt](SourceCode/requirements.txt) file.

```bash
cd SourceCode/
pip install -r requirements.txt
```
or using conda:
```bash
cd SourceCode/
conda install --file requirements.txt
```

## Usage

Part 1 - source code in the jupyer notebook [file](SourceCode/part_1/part1.ipynb). All sample outputs are available in the notebook.
```bash
cd SourceCode/part_1/
jupyter notebook

```


```bash
cd SourceCode/part_3/training
jupyter notebook
```

Part 2 - Source code in the jupyer notebook [file](SourceCode/part_2/). Outputs and explanations are given in the code.

- Webscrapper to get dataset is located in enola_holmes_imdb_review_scraper.py [file](SourceCode/part_2/enola_holmes_imdb_review_scraper.py).

- Dataset analysis can be loaded using:
```bash
cd SourceCode/part_2/
jupyter notebook

```
Part 3 - source code for training in the jupyer notebook [sentiment_analysis_keras_classical](SourceCode\part_3\training\sentiment_analysis_keras_classical.ipynb) and [sentiment_analysis_bert](SourceCode\part_3\training\sentiment_analysis_bert.ipynb). All sample outputs are available in the notebook. 
- Note that for training the bidirectional LSTM in sentiment_analysis_keras_classical.ipynb, glove weights 'glove.6B.100d.txt' needs to be downloaded from https://nlp.stanford.edu/projects/glove/.

## Instructions on how to use the sentiment analysis application

1) Ensure python>=3.6 is used.
2) ```cd SourceCode/```
3) Run ```pip install -r requirements.txt``` in the working directory and then run ```pip install torch===1.7.0 torchvision===0.8.1 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html``` or check pytorch.org for your version of a stable update. Installation will take a few minutes.
4) ```cd part_3/application/```
5) Download model weights using this [link](https://drive.google.com/file/d/1GuDtqzlRqpO6L-McD-jMZr3OuPYrjaTH/view?usp=sharing) and add it under the application directory.
6) Run ```python ./deep_sentiment_analysis.py```
7) Follow the instructions in the application.
8) Outputs are probabilities of negative, neutral or positive class for the given review and the max probability is its predicted class.

Note: model weights may take up to a few minutes to load into your device, ensure some RAM is free to run the application.

## Report
Our report can be found [here](report.pdf).

## License
[Apache 2.0](LICENSE)
