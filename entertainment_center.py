import fresh_tomatoes
import media

twenty_one_jump_street = media.Movie("21 Jump Street",
                            "Two cops go undercover in highschool",
                            "https://upload.wikimedia.org/wikipedia/en/9/93/21JumpStreetfilm.jpg",
                            "https://www.youtube.com/watch?v=nlppOBB3wNY")

twenty_two_jump_street = media.Movie("22 Jump Street",
                             "Two cops go undercover in college",
                             "https://upload.wikimedia.org/wikipedia/en/1/1d/22_Jump_Street_Poster.png",
                             "https://www.youtube.com/watch?v=v9S_dYuq0vE")

goodfellas = media.Movie("Goodfellas",
                         "Living in a mob lifestyle",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=2ilzidi_J8Q")

the_thing = media.Movie("The Thing",
                        "Scientists in the Antartic face an unknown enemy",
                        "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Thing_%281982%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=F7t-919Ec9U")

the_lego_movie = media.Movie("The Lego Movie",
                             "The chosen lego sets out to save the Lego world",
                             "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

oblivion = media.Movie("Oblivion",
                       "A routine patrol takes an unexpected turn",
                       "https://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
                       "https://www.youtube.com/watch?v=XmIIgE7eSak")

interstellar = media.Movie("Interstellar",
                           "A man leaves his family and planet to find a solution for his dying planet",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

saving_private_ryan = media.Movie("Saving Private Ryan",
                                  "A group of soldiers go deep into enemy territoy to save one man",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                                  "https://www.youtube.com/watch?v=HyVuRpjmaAI")

john_wick = media.Movie("John Wick",
                        "A retired assasin goes on revenge after men kill his dog",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")



movies = [twenty_one_jump_street, twenty_two_jump_street, goodfellas,
          the_thing, the_lego_movie, oblivion, interstellar, saving_private_ryan,
          john_wick]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
