# recommendation-engine

I have used movie lense dataset to implement this recommendation system.
link for download : https://grouplens.org/datasets/movielens/

I am using Pearson correlation coefficient to find the related movies, for a quick guide please check https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

In this this implementation you need to pass the input movie based on which you need a recommendation.

print(get_recommendations('Silence of the Lambs, The (1991)', movie_ratings_pivot, 5))

Then above method will return top 5 realted movies which was generated using Pearson correlation coefficient.
