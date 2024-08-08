{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNTYsxsJIkQlcP/pMSMDGAd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/sushant-chivale/Blockchain_1/blob/main/mean_var_std.py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "byjXRjx7JF-G"
      },
      "outputs": [],
      "source": [
        "import sys\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QPlXaXaqSahb",
        "outputId": "de56ed66-f2df-4da5-b479-8ac6931bea02"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'mean_flat': 5.0, 'variance_flat': 6.666666666666667, 'std_dev_flat': 2.581988897471611, 'max_flat': 9, 'min_flat': 1, 'sum_flat': 45, 'mean_axis0': [4.0, 5.0, 6.0], 'variance_axis0': [6.0, 6.0, 6.0], 'std_dev_axis0': [2.449489742783178, 2.449489742783178, 2.449489742783178], 'max_axis0': [7, 8, 9], 'min_axis0': [1, 2, 3], 'sum_axis0': [12, 15, 18], 'mean_axis1': [2.0, 5.0, 8.0], 'variance_axis1': [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 'std_dev_axis1': [0.816496580927726, 0.816496580927726, 0.816496580927726], 'max_axis1': [3, 6, 9], 'min_axis1': [1, 4, 7], 'sum_axis1': [6, 15, 24]}\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def analyze_matrix(data_list):\n",
        "    # Check if the input list has exactly 9 elements\n",
        "    if len(data_list) != 9:\n",
        "        raise ValueError(\"List must contain nine numbers.\")\n",
        "\n",
        "    # Convert the list into a 3x3 NumPy array\n",
        "    matrix = np.array(data_list).reshape(3, 3)\n",
        "\n",
        "    # Calculate statistics\n",
        "    stats = {\n",
        "        'mean_flat': np.mean(matrix).tolist(),\n",
        "        'variance_flat': np.var(matrix).tolist(),\n",
        "        'std_dev_flat': np.std(matrix).tolist(),\n",
        "        'max_flat': np.max(matrix).tolist(),\n",
        "        'min_flat': np.min(matrix).tolist(),\n",
        "        'sum_flat': np.sum(matrix).tolist(),\n",
        "\n",
        "        'mean_axis0': np.mean(matrix, axis=0).tolist(),\n",
        "        'variance_axis0': np.var(matrix, axis=0).tolist(),\n",
        "        'std_dev_axis0': np.std(matrix, axis=0).tolist(),\n",
        "        'max_axis0': np.max(matrix, axis=0).tolist(),\n",
        "        'min_axis0': np.min(matrix, axis=0).tolist(),\n",
        "        'sum_axis0': np.sum(matrix, axis=0).tolist(),\n",
        "\n",
        "        'mean_axis1': np.mean(matrix, axis=1).tolist(),\n",
        "        'variance_axis1': np.var(matrix, axis=1).tolist(),\n",
        "        'std_dev_axis1': np.std(matrix, axis=1).tolist(),\n",
        "        'max_axis1': np.max(matrix, axis=1).tolist(),\n",
        "        'min_axis1': np.min(matrix, axis=1).tolist(),\n",
        "        'sum_axis1': np.sum(matrix, axis=1).tolist(),\n",
        "    }\n",
        "\n",
        "    return stats\n",
        "\n",
        "# Example usage\n",
        "try:\n",
        "    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # This list is too short\n",
        "    statistics = analyze_matrix(data_list)\n",
        "    print(statistics)\n",
        "except ValueError as e:\n",
        "    print(e)"
      ]
    }
  ]
}