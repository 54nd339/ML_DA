# Machine Learning Algorithms and Data Analysis

This repository contains the implementation of various Machine Learning Algorithms and Data Analysis techniques in Python.

### Index
- [Basics](https://github.com/54nd339/ML_DA/tree/master/Basics) - Contains the basic programs to get started with. It includes regression, classification, clustering, dimensionality reduction, etc from scratch.
- [DA](https://github.com/54nd339/ML_DA/tree/master/DA) - Contains the programs related to Data Analysis like data cleaning, data visualization, etc.
- [NLP](https://github.com/54nd339/ML_DA/tree/master/NLP) - Contains the programs related to Natural Language Processing like Viterbi Algorithm, Hidden Markov Model, etc.
- [Colabs](https://github.com/54nd339/ML_DA/tree/master/Colabs) - Contains the programs that are implemented in Google Colaboratory, mostly related to Deep Learning and Computer Vision. It includes Image Captioning, Denoising, Enhancements, etc.
- [Minor](https://github.com/54nd339/ML_DA/tree/master/Minor) - Contains the programs related to the Minor Project. It is a comparative study of various GAN models on the MNIST dataset.
- [Test](https://github.com/54nd339/ML_DA/tree/master/Test) - Contains the programs for automation of data entry to [Konnexions](https://konnexions.netlify.app) Society of KIIT.

#### Advanced Topics
- [GAN](https://github.com/54nd339/ML_DA/tree/master/Basics) - Contains the programs related to Generative Adversarial Networks optimising algos on non-convex loss functions.
- [Proctoring-AI](https://github.com/54nd339/ML_DA/tree/master/Proctoring-AI) - Contains the programs related to Proctoring AI. It includes Face Recognition, Eye Tracking, etc.
- [QuantumComp](https://github.com/54nd339/ML_DA/tree/master/QuantumComp) - An optimisation Algorithm for Quantum gate insertion in Quantum Circuits using genetic algorithm.

### Pre-requisites
To run the programs in this repo, do the following:
- create a virtual environment using conda or venv.
    - `conda create -n <env_name> python=3.7`
    - `python -m venv <env_name>`
- activate the virtual environment
    - `conda activate <env_name>`
    - `cd ./venv/Scripts/activate` (windows users)
    - `source ./venv/bin/activate` (mac and linux users)
- install the requirements
  - `pip install --upgrade pip` (to upgrade pip)
  - `pip install -r requirements.txt`

Once the requirements have been installed, The programs will run successfully.

### Library Used and their description
#### For Data Analysis
- [Numpy](https://numpy.org/) - NumPy is the fundamental package for scientific computing with Python.
- [Pandas](https://pandas.pydata.org/) - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
- [Matplotlib](https://matplotlib.org/) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
- [Seaborn](https://seaborn.pydata.org/) - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- [Scikit-Learn](https://scikit-learn.org/stable/) - Scikit-learn is a free software machine learning library for the Python programming language.

#### For Machine Learning and Deep Learning
- [Tensorflow](https://www.tensorflow.org/) - TensorFlow is an end-to-end open source platform for machine learning.
- [Keras](https://keras.io/) - Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.

#### For Natural Language Processing
- [NLTK](https://www.nltk.org/) - NLTK is a leading platform for building Python programs to work with human language data.
- [Spacy](https://spacy.io/) - Industrial-strength Natural Language Processing (NLP) with Python and Cython.
- [hmmlearn](https://hmmlearn.readthedocs.io/en/latest/) - Hidden Markov Models in Python, with scikit-learn like API.

#### For Computer Vision
- [OpenCV](https://opencv.org/) - OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
- [Scikit-Image](https://scikit-image.org/) - Scikit-image is a collection of algorithms for image processing.

#### Others
- [Jupyter Notebook](https://jupyter.org/) - Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
- [Autograd](https://github.com/HIPS/autograd) - Autograd is a Python library that provides automatic differentiation for numpy code.
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
- [Keras Preprocessing](https://keras.io/api/preprocessing/) - Keras Preprocessing is a collection of utilities for preprocessing data.
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - SpeechRecognition is a library for performing speech recognition, with support for several engines and APIs, online and offline.
