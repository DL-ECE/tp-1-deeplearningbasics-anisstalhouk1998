{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.9-final"
    },
    "colab": {
      "name": "Copie de rapport.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DL-ECE/tp-1-deeplearningbasics-anisstalhouk1998/blob/master/rapport.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qG4I5LmcFhGQ"
      },
      "source": [
        "# TP-1 DLBasics\n",
        "\n",
        "## Digit classification using the MNIST dataset\n",
        "\n",
        "In this notebook you will train your first neural network. Feel free to look back at the Lecture-1 slides to complete the cells below. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P97X5QauFhGR"
      },
      "source": [
        "#### Install dependencies freeze by poetry \n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OO7TriLpFhGS",
        "outputId": "21fc7eac-c964-4776-bb3f-b17861c3e2d7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "!python3 -m pip install --upgrade pip\n",
        "!python3 -m pip install matplotlib numpy scikit-learn==0.23.2\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting pip\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/cb/28/91f26bd088ce8e22169032100d4260614fc3da435025ff389ef1d396a433/pip-20.2.4-py2.py3-none-any.whl (1.5MB)\n",
            "\u001b[K     |████████████████████████████████| 1.5MB 2.8MB/s \n",
            "\u001b[?25hInstalling collected packages: pip\n",
            "  Found existing installation: pip 19.3.1\n",
            "    Uninstalling pip-19.3.1:\n",
            "      Successfully uninstalled pip-19.3.1\n",
            "Successfully installed pip-20.2.4\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.6/dist-packages (3.2.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (1.18.5)\n",
            "Collecting scikit-learn==0.23.2\n",
            "  Downloading scikit_learn-0.23.2-cp36-cp36m-manylinux1_x86_64.whl (6.8 MB)\n",
            "\u001b[K     |████████████████████████████████| 6.8 MB 2.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (1.3.1)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (2.8.1)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (0.10.0)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (2.4.7)\n",
            "Collecting threadpoolctl>=2.0.0\n",
            "  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: joblib>=0.11 in /usr/local/lib/python3.6/dist-packages (from scikit-learn==0.23.2) (0.17.0)\n",
            "Requirement already satisfied: scipy>=0.19.1 in /usr/local/lib/python3.6/dist-packages (from scikit-learn==0.23.2) (1.4.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.6/dist-packages (from python-dateutil>=2.1->matplotlib) (1.15.0)\n",
            "Installing collected packages: threadpoolctl, scikit-learn\n",
            "  Attempting uninstall: scikit-learn\n",
            "    Found existing installation: scikit-learn 0.22.2.post1\n",
            "    Uninstalling scikit-learn-0.22.2.post1:\n",
            "      Successfully uninstalled scikit-learn-0.22.2.post1\n",
            "Successfully installed scikit-learn-0.23.2 threadpoolctl-2.1.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t66Z3k8oFhGW"
      },
      "source": [
        "#### Import the different module we will need in this notebook \n",
        "\n",
        "All the dependencies are installed. Below we import them and will be using them in all our notebooks.\n",
        "\n",
        "Please feel free to look arround and look at their API. \n",
        "\n",
        "The student should be limited to these imports to complete this work.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3HnsavajFhGX"
      },
      "source": [
        "# We import some python standard librairy utility function \n",
        "# see the [python doc](https://docs.python.org/3.6/library/functools.html?highlight=func#module-functools) for more info \n",
        "from functools import reduce \n",
        "import random \n",
        "\n",
        "# To create some plot and figures: matplolib [matplotlib doc](https://matplotlib.org/)\n",
        "# To do compute on matrix and vectors: [numpy doc](https://numpy.org/)\n",
        "# To do some classical Machine Learning: [sklearn doc](https://scikit-learn.org/stable/index.html)\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from sklearn.datasets import fetch_openml\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YysTRE42FhGa"
      },
      "source": [
        "# In order to have some reproducable results and easier debugging \n",
        "# we fix the seed of random.\n",
        "random.seed(1342)\n",
        "np.random.seed(1342)"
      ],
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PNPO5H0EFhGd"
      },
      "source": [
        "## Data preparation (3 pts)\n",
        "\n",
        "As seen in the lecture one of the earlier use case for deep learning was digit recognition. \n",
        "\n",
        "The dataset we will use today is the MNISTdataset http://yann.lecun.com/exdb/mnist/. \n",
        "\n",
        "One image will be represented a vector (a 28x28 image will be represented as vector with 784 entries).\n",
        "\n",
        "Thus, we will end up with a n_examples x 784 matrix to represent the images in the dataset.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NiaIS0N6FhGe"
      },
      "source": [
        "mnist_data, mnist_target = fetch_openml('mnist_784', version=1, return_X_y=True)"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zck7X3K2FhGg",
        "outputId": "20db57d8-1b04-4e19-cfe1-ecb4236b757b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Let's warmup and answer this first question\n",
        "# Replace the None with you answer.\n",
        "\n",
        "# How many image are in this dataset ? \n",
        "def data_length(dataset: np.array, target: np.array):\n",
        "    \"\"\"Function to compute the length of the dataset and the length of the target labels.\"\"\"\n",
        "    dataset_length = dataset.shape[0]\n",
        "    target_length = target.shape[0]\n",
        "    return dataset_length, target_length\n",
        "    \n",
        "data_length(mnist_data,mnist_target)\n"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(70000, 70000)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MtFDSgdrFhGj",
        "outputId": "5112f3cb-e12b-49ec-fda3-5e2626d4bc96",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        }
      },
      "source": [
        "# Let's look at on image from this dataset \n",
        "def plot_one_image(dataset: np.array, target: np.array, image_index: int):\n",
        "    \"\"\"Function to plot the image at the given index.\"\"\"\n",
        "    image = dataset[image_index].reshape(28,28)\n",
        "    target = target[image_index]\n",
        "    plt.imshow(image, cmap='gray')\n",
        "    plt.title(f\"This is a {target}\")\n",
        "\n",
        "\n",
        "plot_one_image(mnist_data, mnist_target ,6)"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9lkPLQBHFhGl"
      },
      "source": [
        "\n",
        "# In a similar fashion to classical machine learning, we will create a test split to known if the neural network is learning well.\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(mnist_data, mnist_target, test_size=0.33, random_state=1342)\n",
        "\n",
        "# You the 2 function below to check if they are working properly on this divided dataset.\n",
        "\n",
        "X_train_length, y_train_length = data_length(X_train, y_train)\n",
        "X_test_length, y_test_length = data_length(X_test, y_test)\n",
        "\n",
        "assert X_train_length == y_train_length and X_train_length == 46900\n",
        "assert X_test_length == y_test_length and X_test_length == 23100\n"
      ],
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SZziHVWIFhGo",
        "outputId": "9fadc740-80e4-40f4-de92-a7f9c96b20c5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        }
      },
      "source": [
        "plot_one_image(X_train, y_train , 120)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FZxvsLMhFhGr",
        "outputId": "9abdf28b-e4b7-43cf-b88e-db7d4285eddc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        }
      },
      "source": [
        "plot_one_image(X_test, y_test , 250)"
      ],
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C7DvQR_JFhGt",
        "outputId": "92884c32-9b19-486b-9f00-49236db74497",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# It's important to normalize the data before feeding it into the neural network\n",
        "def normalize_data(dataset: np.array) -> np.array:\n",
        "    normalized_dataset =(dataset-np.min(dataset))/(np.max(dataset)-np.min(dataset))\n",
        "    #dataset/255\n",
        "    return normalized_dataset\n",
        "\n",
        "normalize_data(mnist_data)[0]"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.01176471, 0.07058824, 0.07058824,\n",
              "       0.07058824, 0.49411765, 0.53333333, 0.68627451, 0.10196078,\n",
              "       0.65098039, 1.        , 0.96862745, 0.49803922, 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.11764706, 0.14117647, 0.36862745, 0.60392157,\n",
              "       0.66666667, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
              "       0.99215686, 0.88235294, 0.6745098 , 0.99215686, 0.94901961,\n",
              "       0.76470588, 0.25098039, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.19215686, 0.93333333,\n",
              "       0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
              "       0.99215686, 0.99215686, 0.99215686, 0.98431373, 0.36470588,\n",
              "       0.32156863, 0.32156863, 0.21960784, 0.15294118, 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.07058824, 0.85882353, 0.99215686, 0.99215686,\n",
              "       0.99215686, 0.99215686, 0.99215686, 0.77647059, 0.71372549,\n",
              "       0.96862745, 0.94509804, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.31372549, 0.61176471, 0.41960784, 0.99215686, 0.99215686,\n",
              "       0.80392157, 0.04313725, 0.        , 0.16862745, 0.60392157,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.05490196,\n",
              "       0.00392157, 0.60392157, 0.99215686, 0.35294118, 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.54509804,\n",
              "       0.99215686, 0.74509804, 0.00784314, 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.04313725, 0.74509804, 0.99215686,\n",
              "       0.2745098 , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.1372549 , 0.94509804, 0.88235294, 0.62745098,\n",
              "       0.42352941, 0.00392157, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.31764706, 0.94117647, 0.99215686, 0.99215686, 0.46666667,\n",
              "       0.09803922, 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.17647059,\n",
              "       0.72941176, 0.99215686, 0.99215686, 0.58823529, 0.10588235,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.0627451 , 0.36470588,\n",
              "       0.98823529, 0.99215686, 0.73333333, 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.97647059, 0.99215686,\n",
              "       0.97647059, 0.25098039, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.18039216, 0.50980392,\n",
              "       0.71764706, 0.99215686, 0.99215686, 0.81176471, 0.00784314,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.15294118,\n",
              "       0.58039216, 0.89803922, 0.99215686, 0.99215686, 0.99215686,\n",
              "       0.98039216, 0.71372549, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.09411765, 0.44705882, 0.86666667, 0.99215686, 0.99215686,\n",
              "       0.99215686, 0.99215686, 0.78823529, 0.30588235, 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.09019608, 0.25882353, 0.83529412, 0.99215686,\n",
              "       0.99215686, 0.99215686, 0.99215686, 0.77647059, 0.31764706,\n",
              "       0.00784314, 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.07058824, 0.67058824, 0.85882353,\n",
              "       0.99215686, 0.99215686, 0.99215686, 0.99215686, 0.76470588,\n",
              "       0.31372549, 0.03529412, 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.21568627, 0.6745098 ,\n",
              "       0.88627451, 0.99215686, 0.99215686, 0.99215686, 0.99215686,\n",
              "       0.95686275, 0.52156863, 0.04313725, 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.53333333, 0.99215686, 0.99215686, 0.99215686,\n",
              "       0.83137255, 0.52941176, 0.51764706, 0.0627451 , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
              "       0.        , 0.        , 0.        , 0.        ])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5-_KWZskFhGv"
      },
      "source": [
        "It's also important to find a good representation of the target.\n",
        "\n",
        "In this notebook it will be one-hot vector. \n",
        "\n",
        "Complete the below function to turn the target vector into a one-hot matrix.\n",
        "\n",
        "For example, a `[0,1,9]` vector will become the following matrix:\n",
        "\n",
        "`[[1,0,0,0,0,0,0,0,0,0],\n",
        "  [0,1,0,0,0,0,0,0,0,0],\n",
        "  [0,0,0,0,0,0,0,0,0,1]]`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dFDeZ6LGFhGw",
        "outputId": "242c481c-ca65-4914-cc99-ad7ee5a09bf7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "def target_to_one_hot(target: np.array) -> np.array:\n",
        "    one_hot_matrix = np.zeros([target.shape[0],10]) \n",
        "    for i in range(0,target.shape[0]) :\n",
        "     label = int(target[i])\n",
        "     one_hot_matrix[i,label] = 1\n",
        "     #print(label)\n",
        "     # one_hot_matrix[np.arange(len(target)), target] = 1\n",
        "    return one_hot_matrix\n",
        "\n",
        "target_to_one_hot(mnist_target.reshape(-1,1))\n",
        "#target_to_one_hot(np.array([0, 4, 6]))"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0., 0., 0., ..., 0., 0., 0.],\n",
              "       [1., 0., 0., ..., 0., 0., 0.],\n",
              "       [0., 0., 0., ..., 0., 0., 0.],\n",
              "       ...,\n",
              "       [0., 0., 0., ..., 0., 0., 0.],\n",
              "       [0., 0., 0., ..., 0., 0., 0.],\n",
              "       [0., 0., 0., ..., 0., 0., 0.]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "H88q-swuFhGy"
      },
      "source": [
        "## Useful functions (3 pts)\n",
        "\n",
        "Implement the sigmoid function, its derivative and the softmax function:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "97S-e8_7FhGy"
      },
      "source": [
        "def sigmoid(M: np.array) -> np.array:\n",
        "    \"\"\"Apply a sigmoid to the input array\"\"\"\n",
        "    # TODO\n",
        "    Mat_sigmoid = 1/(1+np.exp(-M))\n",
        "    \n",
        "    return Mat_sigmoid\n",
        "\n"
      ],
      "execution_count": 384,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hJlSIQCEFhG0"
      },
      "source": [
        "def d_sigmoid(M: np.array)-> np.array:\n",
        "    \"\"\"Compute the derivative of the sigmoid\"\"\" \n",
        "    # TODO\n",
        "    return (sigmoid(M)*(1-sigmoid(M)))\n",
        "\n"
      ],
      "execution_count": 385,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8nIZmHUvFhG4"
      },
      "source": [
        "def softmax(X: np.array)-> np.array:\n",
        "    \"\"\"Apply a softmax to the input array\"\"\"\n",
        "    # TODO\n",
        "    X_exp=np.exp(X)\n",
        "    X_sum=np.sum(X_exp,axis=1).reshape(-1,1)\n",
        "    Mat_softmax= X_exp/X_sum\n",
        "    return Mat_softmax\n"
      ],
      "execution_count": 386,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bqNRI3ArFhG6"
      },
      "source": [
        "## Feed forward NN\n",
        "\n",
        "Now that the data is prepared it's time to create a neural network to learn on this dataset.\n",
        "\n",
        "You can look back at the lecture slides and need to replace the None in the below function in order to have the building blocks of this first neural network. \n",
        "\n",
        "To do so we are now going to create the FFNN class. It will take list of integers to represent the network.\n",
        "\n",
        "One element in the list corresponds to the number of neurones in the layer.\n",
        "`config = [784, 3, 4, 10]` will be an acceptable config: \n",
        "- inputs are 1x784 vectors \n",
        "- the model output should be a vector of size 10 to classify between 10 classes.\n",
        "- in the middle the hidden layer are fully customizable\n",
        "\n",
        "You have to do some implementations and replace the None assignment (variable = None). Do not do it for the Layer object.\n",
        "\n",
        "Warning: None return type for some methods are not supposed to be affected"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ta-WAx0vFhG7"
      },
      "source": [
        "class Layer:\n",
        "    def __init__(self): #pasbesoin de modif\n",
        "        self.Z = None\n",
        "        self.W = None\n",
        "        self.D = None\n",
        "        self.F = None\n",
        "        self.activation = None"
      ],
      "execution_count": 387,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DD3LSd-iFhG9"
      },
      "source": [
        "class FFNN:\n",
        "    def __init__(self, config, minibatch_size=100, learning_rate=0.1):\n",
        "        self.layers = []\n",
        "        self.config = config\n",
        "        self.nlayers = len(config)\n",
        "        self.minibatch_size = minibatch_size\n",
        "        self.learning_rate = learning_rate\n",
        "        \n",
        "        input_data = Layer()\n",
        "        # TODO: initialize the Z matrix with the a matrix containing only zeros\n",
        "        # its shape should be (minibatch_size, config[0])\n",
        "        input_data.Z = np.zeros((minibatch_size, config[0]))\n",
        "        self.layers.append(input_data)\n",
        "                                        \n",
        "        for i in range(1, len(config)):\n",
        "            nnodes = config[i]\n",
        "            layer  = Layer()\n",
        "            nlines_prev, ncols_prev = self.layers[i - 1].Z.shape\n",
        "            # TODO: initilize the weight matrix W in the layer with a random normal distribution\n",
        "            # its shape should be (ncols_prev, nnodes)\n",
        "            layer.W = np.random.randn(ncols_prev, nnodes) \n",
        "            # TODO: initilize the matrix Z in the layer with a matrix containing only zeros\n",
        "            # its shape should be (nlines_prev, nnodes)\n",
        "            layer.Z = np.zeros((nlines_prev, nnodes))\n",
        "            # TODO: use the sigmoid activation function\n",
        "            layer.activation = sigmoid \n",
        "            self.layers.append(layer)\n",
        "        # TODO: Your last layer activation should be a softmax\n",
        "        self.layers[-1].activation = softmax\n",
        "        \n",
        "    def one_step_forward(self, signal: np.array, cur_layer: Layer)-> np.array:\n",
        "        # Compute the F and Z matrix for the current layer and return Z\n",
        "        # TODO: Compute the dot product betzeen the signal and the current layer W matrix\n",
        "        S = np.dot(signal,cur_layer.W) \n",
        "        # TODO: Compute the F matrix of the current layer\n",
        "        cur_layer.F =d_sigmoid(S).T \n",
        "        # Compute the activation od the current layer\n",
        "        cur_layer.Z = cur_layer.activation(S) \n",
        "        return cur_layer.Z\n",
        "       \n",
        "    def forward_pass(self, input_data: np.array)-> np.array:\n",
        "        # TODO: perform the whole forward pass using the on_step_forward function\n",
        "        self.layers[0].Z = input_data\n",
        "        for i in range(1, len(self.config)):\n",
        "            signal = self.layers[i-1].Z\n",
        "            cur_layer = self.layers[i]\n",
        "            cur_layer.Z = self.one_step_forward(signal, cur_layer) \n",
        "        return self.layers[-1].Z\n",
        "    \n",
        "    def one_step_backward(self, prev_layer: Layer, cur_layer: Layer)-> Layer:\n",
        "        # TODO: Compute the D matrix of the current layer using the previous layer and return the current layer\n",
        "        sig_e = np.dot(prev_layer.W, prev_layer.D)\n",
        "        Di = cur_layer.F *sig_e  \n",
        "        cur_layer.D = Di\n",
        "        return cur_layer\n",
        "        \n",
        "    def backward_pass(self, D_out: np.array)-> np.array: # None:\n",
        "        self.layers[-1].D = D_out.T\n",
        "        # TODO: Compute the D matrix for all the layers (excluding the first one which corresponds to the input itself)\n",
        "        # (you should only use self.layers[1:])\n",
        "        return reduce(self.one_step_backward, self.layers[1 :][: :-1])\n",
        "       \n",
        "    \n",
        "    def update_weights(self, cur_layer: Layer, next_layer: Layer)-> Layer:\n",
        "        # TODO: Update the W matrix of the next_layer using the current_layer and the learning rate\n",
        "        # and return the next_layer\n",
        "        dif=np.dot(next_layer.D, cur_layer.Z).T\n",
        "        next_layer.W += -self.learning_rate*dif\n",
        "        \n",
        "        return next_layer\n",
        "\n",
        "    \n",
        "    def update_all_weights(self)-> Layer:\n",
        "        # TODO: Update all W matrix using the update_weights function\n",
        "        return reduce(self.update_weights, self.layers)\n",
        "        \n",
        "        \n",
        "    def get_error(self, y_pred: np.array, y_batch: np.array)-> float:\n",
        "        # TODO: return the accuracy on the predictions\n",
        "        v_pred = np.argmax(y_pred, axis=1)\n",
        "        v_reel = np.argmax(y_batch, axis=1)\n",
        "        matches = (v_pred == v_reel).sum()\n",
        "        Acc= matches / y_pred.shape[0]\n",
        "        return Acc\n",
        "        # the accuracy should be in the [0.0, 1.0] range\n",
        "        \n",
        "    \n",
        "    def get_test_error(self, X: np.array, y: np.array)-> float:\n",
        "        # TODO: Compute the accuracy using the get_error function\n",
        "        nbatch = X.shape[0]\n",
        "        error_sum = 0.0\n",
        "        for i in range(0, nbatch):\n",
        "            X_batch = X[i,:,:].reshape(self.minibatch_size, -1)\n",
        "            y_batch = y[i,:,:].reshape(self.minibatch_size, -1)           \n",
        "            # TODO: get y_pred using the forward pass\n",
        "            y_pred = self.forward_pass(X_batch)\n",
        "            error_sum += self.get_error(y_pred, y_batch)\n",
        "        return error_sum / nbatch\n",
        "            \n",
        "        \n",
        "    def train(self, nepoch, X_train, y_train, X_test, y_test)-> float:\n",
        "        X_train = X_train.reshape(-1, self.minibatch_size, 784)\n",
        "        y_train = y_train.reshape(-1, self.minibatch_size, 10)\n",
        "        \n",
        "        X_test = X_test.reshape(-1, self.minibatch_size, 784)\n",
        "        y_test = y_test.reshape(-1, self.minibatch_size, 10)\n",
        "        \n",
        "        # TODO: Get the number of batch based on X_train's shape\n",
        "        nbatch = X_train.shape[0] \n",
        "        error_test = 0.0\n",
        "        for epoch in range(0, nepoch):\n",
        "            error_sum_train = 0.0\n",
        "            for i in range(0, nbatch):\n",
        "                X_batch = X_train[i,:, :]\n",
        "                y_batch = y_train[i,:, :]\n",
        "        \n",
        "                y_pred = self.forward_pass(X_batch)\n",
        "                self.backward_pass(y_pred - y_batch)\n",
        "                self.update_all_weights()\n",
        "                error_sum_train += self.get_error(y_pred, y_batch)\n",
        "            error_test = self.get_test_error(X_test, y_test)\n",
        "            print(f\"Training accuracy: {error_sum_train / nbatch:.3f}, Test accuracy: {error_test:.3f}\")\n",
        "        return error_test\n",
        " "
      ],
      "execution_count": 388,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fp0dGasRFhG_"
      },
      "source": [
        "## Training phase (12 pts)\n",
        "\n",
        "Now, it is time to train the model !!\n",
        "\n",
        "You can play with the different parameters (minibatch_size, nepoch, learning_rate and the number of hidden layers)\n",
        "\n",
        "It's on 12 points because there is a lot of functions to fill but also we want the training best training accuracy. \n",
        "\n",
        "To have all the point your neural network needs to have a Test accuracy > 92 % !! "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eJeNKd59FhG_"
      },
      "source": [
        "minibatch_size = 25\n",
        "nepoch = 25\n",
        "learning_rate = 0.0197\n",
        "\n",
        "ffnn = FFNN(config=[784, 100, 100, 10], minibatch_size=minibatch_size, learning_rate=learning_rate)"
      ],
      "execution_count": 395,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mw1Vf9t6FhHC",
        "outputId": "532caff9-a76a-4229-f48b-7da915cd020f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "assert X_train.shape[0] % minibatch_size == 0\n",
        "assert X_test.shape[0] % minibatch_size == 0\n",
        "\n",
        "err = ffnn.train(nepoch, normalize_data(X_train), target_to_one_hot(y_train), normalize_data(X_test), target_to_one_hot(y_test))"
      ],
      "execution_count": 397,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Training accuracy: 0.962, Test accuracy: 0.932\n",
            "Training accuracy: 0.968, Test accuracy: 0.935\n",
            "Training accuracy: 0.973, Test accuracy: 0.937\n",
            "Training accuracy: 0.978, Test accuracy: 0.939\n",
            "Training accuracy: 0.981, Test accuracy: 0.941\n",
            "Training accuracy: 0.984, Test accuracy: 0.941\n",
            "Training accuracy: 0.987, Test accuracy: 0.942\n",
            "Training accuracy: 0.989, Test accuracy: 0.943\n",
            "Training accuracy: 0.991, Test accuracy: 0.943\n",
            "Training accuracy: 0.993, Test accuracy: 0.943\n",
            "Training accuracy: 0.995, Test accuracy: 0.944\n",
            "Training accuracy: 0.995, Test accuracy: 0.944\n",
            "Training accuracy: 0.996, Test accuracy: 0.944\n",
            "Training accuracy: 0.997, Test accuracy: 0.944\n",
            "Training accuracy: 0.998, Test accuracy: 0.945\n",
            "Training accuracy: 0.998, Test accuracy: 0.945\n",
            "Training accuracy: 0.998, Test accuracy: 0.946\n",
            "Training accuracy: 0.999, Test accuracy: 0.946\n",
            "Training accuracy: 0.999, Test accuracy: 0.946\n",
            "Training accuracy: 0.999, Test accuracy: 0.947\n",
            "Training accuracy: 0.999, Test accuracy: 0.947\n",
            "Training accuracy: 0.999, Test accuracy: 0.947\n",
            "Training accuracy: 0.999, Test accuracy: 0.947\n",
            "Training accuracy: 1.000, Test accuracy: 0.947\n",
            "Training accuracy: 1.000, Test accuracy: 0.947\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m_sgZSHeFhHE"
      },
      "source": [
        "## Error analysis (2 pts)\n",
        "\n",
        "Here we use a subset of the test data to try and find some miss classification.\n",
        "\n",
        "It will help us understand why the neural network failed sometimes to classify images. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jPNd64KuFhHE"
      },
      "source": [
        "nsample = 1000\n",
        "X_demo = X_test[:nsample,:]\n",
        "y_demo = ffnn.forward_pass(X_demo)\n",
        "y_true = y_test[:nsample,:]\n",
        "\n",
        "index_to_plot = 50 \n",
        "plot_one_image(X_demo, y_true, index_to_plot)\n",
        "\n",
        "# Compare to the prediction \n",
        "prediction = np.argmax(y_demo[index_to_plot,:])\n",
        "true_target = np.argmax(y_true[index_to_plot,:])\n",
        "\n",
        "# is it the same number ? "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sc0sLDb2FhHH"
      },
      "source": [
        "# loop arround the demo test set and try to find a miss prediction\n",
        "for i in range(0, nsample):   \n",
        "    prediction = None # Todo\n",
        "    true_target = None # Todo\n",
        "    if prediction != true_target:\n",
        "        # TODO\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lAQH9cAoFhHK"
      },
      "source": [
        "## Open analysis\n",
        "\n",
        "in the cell below please explain you choice for all the parameters of your configuration: \n",
        "\n",
        "- minibatch_size\n",
        "- nepoch\n",
        "- config\n",
        "- learning_rate\n",
        "\n",
        "Also explain how the neural network behave when changing them ? "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7UPdasR8FhHK"
      },
      "source": [
        "## Open analysis answer\n",
        "\n",
        "TODO"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-h4RzB2rmq44"
      },
      "source": [
        "J'ai augmenté le nombre de minibatch"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3y1hh385FhHL"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}