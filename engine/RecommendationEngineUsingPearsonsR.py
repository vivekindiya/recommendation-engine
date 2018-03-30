'''
Created on 30-Mar-2018

@author: Vivek Shah
'''
import pandas as pd
import numpy as np


def replace_id_with_title(movies, ratings):
    """We are replacing movieId in dataset ratings with the movie title from movies dataset."""
    ratings['movieId'] = ratings['movieId'].map(movies.set_index('movieId')['title'])
    return ratings


def pearson_correlation_coefficient(s1, s2):
    """We are finding pearson's correlation coefficient here between two movies. If calulated value is towards negative then the 
    movies are not related where as if the value is positive the movie is related. Increasing and decreasing value determines the how far the two movies are related"""
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))


def get_recommendations(movie_name, pivot, num):
    """Here we will generate the recommendations for a given movie name using the pivot table. num defines top n number of movies to recommend"""
    reviews = []
    for title in pivot.columns:
        if title == movie_name:
            continue
        cor = pearson_correlation_coefficient(pivot[movie_name], pivot[title])
        if np.isnan(cor):
            continue
        else:
            reviews.append((title, cor))
    reviews.sort(key=lambda tup:tup[1], reverse=True)
    return reviews[:num]


movies = pd.read_csv("replace it with movies.csv file path")
ratings = pd.read_csv("replace it with ratings.csv file path")

ratings = replace_id_with_title(movies, ratings)
movie_ratings_pivot = ratings.pivot_table(index=['userId'], columns=['movieId'], values='rating')
print(get_recommendations('Silence of the Lambs, The (1991)', movie_ratings_pivot, 5))
