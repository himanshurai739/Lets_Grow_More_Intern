{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOvfst7zJONoG9Hxv8Khy/C",
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
        "<a href=\"https://colab.research.google.com/github/himanshurai739/Lets_Grow_More_Intern/blob/main/movie_recomendation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "CGUccKZSMPEx",
        "outputId": "ad451d8b-ff3e-4c54-a1a7-554403fd16fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   movieId                               title  \\\n",
            "0        1                    Toy Story (1995)   \n",
            "1        2                      Jumanji (1995)   \n",
            "2        3             Grumpier Old Men (1995)   \n",
            "3        4            Waiting to Exhale (1995)   \n",
            "4        5  Father of the Bride Part II (1995)   \n",
            "\n",
            "                                        genres  \n",
            "0  Adventure|Animation|Children|Comedy|Fantasy  \n",
            "1                   Adventure|Children|Fantasy  \n",
            "2                               Comedy|Romance  \n",
            "3                         Comedy|Drama|Romance  \n",
            "4                                       Comedy  \n",
            "   userId  movieId  rating  timestamp\n",
            "0       1        1     4.0  964982703\n",
            "1       1        3     4.0  964981247\n",
            "2       1        6     4.0  964982224\n",
            "3       1       47     5.0  964983815\n",
            "4       1       50     5.0  964982931\n",
            "title   '71 (2014)  'Hellboy': The Seeds of Creation (2004)  \\\n",
            "userId                                                        \n",
            "1              0.0                                      0.0   \n",
            "2              0.0                                      0.0   \n",
            "3              0.0                                      0.0   \n",
            "4              0.0                                      0.0   \n",
            "5              0.0                                      0.0   \n",
            "\n",
            "title   'Round Midnight (1986)  'Salem's Lot (2004)  \\\n",
            "userId                                                \n",
            "1                          0.0                  0.0   \n",
            "2                          0.0                  0.0   \n",
            "3                          0.0                  0.0   \n",
            "4                          0.0                  0.0   \n",
            "5                          0.0                  0.0   \n",
            "\n",
            "title   'Til There Was You (1997)  'Tis the Season for Love (2015)  \\\n",
            "userId                                                               \n",
            "1                             0.0                              0.0   \n",
            "2                             0.0                              0.0   \n",
            "3                             0.0                              0.0   \n",
            "4                             0.0                              0.0   \n",
            "5                             0.0                              0.0   \n",
            "\n",
            "title   'burbs, The (1989)  'night Mother (1986)  (500) Days of Summer (2009)  \\\n",
            "userId                                                                          \n",
            "1                      0.0                   0.0                          0.0   \n",
            "2                      0.0                   0.0                          0.0   \n",
            "3                      0.0                   0.0                          0.0   \n",
            "4                      0.0                   0.0                          0.0   \n",
            "5                      0.0                   0.0                          0.0   \n",
            "\n",
            "title   *batteries not included (1987)  ...  Zulu (2013)  [REC] (2007)  \\\n",
            "userId                                  ...                              \n",
            "1                                  0.0  ...          0.0           0.0   \n",
            "2                                  0.0  ...          0.0           0.0   \n",
            "3                                  0.0  ...          0.0           0.0   \n",
            "4                                  0.0  ...          0.0           0.0   \n",
            "5                                  0.0  ...          0.0           0.0   \n",
            "\n",
            "title   [REC]² (2009)  [REC]³ 3 Génesis (2012)  \\\n",
            "userId                                           \n",
            "1                 0.0                      0.0   \n",
            "2                 0.0                      0.0   \n",
            "3                 0.0                      0.0   \n",
            "4                 0.0                      0.0   \n",
            "5                 0.0                      0.0   \n",
            "\n",
            "title   anohana: The Flower We Saw That Day - The Movie (2013)  \\\n",
            "userId                                                           \n",
            "1                                                     0.0        \n",
            "2                                                     0.0        \n",
            "3                                                     0.0        \n",
            "4                                                     0.0        \n",
            "5                                                     0.0        \n",
            "\n",
            "title   eXistenZ (1999)  xXx (2002)  xXx: State of the Union (2005)  \\\n",
            "userId                                                                \n",
            "1                   0.0         0.0                             0.0   \n",
            "2                   0.0         0.0                             0.0   \n",
            "3                   0.0         0.0                             0.0   \n",
            "4                   0.0         0.0                             0.0   \n",
            "5                   0.0         0.0                             0.0   \n",
            "\n",
            "title   ¡Three Amigos! (1986)  À nous la liberté (Freedom for Us) (1931)  \n",
            "userId                                                                    \n",
            "1                         4.0                                        0.0  \n",
            "2                         0.0                                        0.0  \n",
            "3                         0.0                                        0.0  \n",
            "4                         0.0                                        0.0  \n",
            "5                         0.0                                        0.0  \n",
            "\n",
            "[5 rows x 9719 columns]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:493: UserWarning: X does not have valid feature names, but NearestNeighbors was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "X has 488 features, but NearestNeighbors is expecting 9719 features as input.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-04607d4079d7>\u001b[0m in \u001b[0;36m<cell line: 44>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     43\u001b[0m \u001b[0;31m# Example usage\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 44\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mget_recommendations\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Toy Story (1995)'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mn_recommendations\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     45\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     46\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mcalculate_rmse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpredictions\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mactual\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-7-04607d4079d7>\u001b[0m in \u001b[0;36mget_recommendations\u001b[0;34m(movie_title, n_recommendations)\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0;31m# Function to get recommendations\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mget_recommendations\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmovie_title\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mn_recommendations\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 37\u001b[0;31m     \u001b[0mdistances\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mindices\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmodel\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkneighbors\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtrain\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mmovie_title\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mn_neighbors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mn_recommendations\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     38\u001b[0m     \u001b[0mrecommended_movies\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdistances\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mflatten\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/neighbors/_base.py\u001b[0m in \u001b[0;36mkneighbors\u001b[0;34m(self, X, n_neighbors, return_distance)\u001b[0m\n\u001b[1;32m    823\u001b[0m                 \u001b[0mX\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_check_precomputed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    824\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 825\u001b[0;31m                 \u001b[0mX\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_validate_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maccept_sparse\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"csr\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreset\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0morder\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"C\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    826\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    827\u001b[0m         \u001b[0mn_samples_fit\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mn_samples_fit_\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/base.py\u001b[0m in \u001b[0;36m_validate_data\u001b[0;34m(self, X, y, reset, validate_separately, cast_to_ndarray, **check_params)\u001b[0m\n\u001b[1;32m    652\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    653\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mno_val_X\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mcheck_params\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"ensure_2d\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 654\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_check_n_features\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreset\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mreset\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    655\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    656\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mout\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/sklearn/base.py\u001b[0m in \u001b[0;36m_check_n_features\u001b[0;34m(self, X, reset)\u001b[0m\n\u001b[1;32m    441\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    442\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mn_features\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mn_features_in_\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 443\u001b[0;31m             raise ValueError(\n\u001b[0m\u001b[1;32m    444\u001b[0m                 \u001b[0;34mf\"X has {n_features} features, but {self.__class__.__name__} \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    445\u001b[0m                 \u001b[0;34mf\"is expecting {self.n_features_in_} features as input.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: X has 488 features, but NearestNeighbors is expecting 9719 features as input."
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import mean_squared_error\n",
        "from sklearn.neighbors import NearestNeighbors\n",
        "\n",
        "# Load MovieLens dataset\n",
        "\n",
        "\n",
        "# Load data\n",
        "movies = pd.read_csv('ml-latest-small/movies.csv')\n",
        "ratings = pd.read_csv('ml-latest-small/ratings.csv')\n",
        "\n",
        "# Display the first few rows\n",
        "print(movies.head())\n",
        "print(ratings.head())\n",
        "\n",
        "# Merge the datasets\n",
        "data = pd.merge(ratings, movies, on='movieId')\n",
        "\n",
        "# Create a pivot table\n",
        "pivot_table = data.pivot_table(index='userId', columns='title', values='rating')\n",
        "pivot_table.fillna(0, inplace=True)\n",
        "\n",
        "# Display the pivot table\n",
        "print(pivot_table.head())\n",
        "\n",
        "# Create a train-test split\n",
        "train, test = train_test_split(pivot_table, test_size=0.2, random_state=42)\n",
        "\n",
        "# Fit the model\n",
        "model = NearestNeighbors(metric='cosine', algorithm='brute')\n",
        "model.fit(train)\n",
        "\n",
        "# Function to get recommendations\n",
        "def get_recommendations(movie_title, n_recommendations=5):\n",
        "    distances, indices = model.kneighbors(train[movie_title].values.reshape(1, -1), n_neighbors=n_recommendations+1)\n",
        "    recommended_movies = []\n",
        "    for i in range(1, len(distances.flatten())):\n",
        "        recommended_movies.append(train.columns[indices.flatten()[i]])\n",
        "    return recommended_movies\n",
        "\n",
        "# Example usage\n",
        "print(get_recommendations('Toy Story (1995)', n_recommendations=5))\n",
        "\n",
        "def calculate_rmse(predictions, actual):\n",
        "    return np.sqrt(mean_squared_error(predictions, actual))\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}