import fresh_tomatoes
import media

twenty_one_jump_street = media.Movie("21 Jump Street",
                            "Two cops go undercover in highschool",
                            "https://upload.wikimedia.org/wikipedia/en/9/93/21JumpStreetfilm.jpg",
                            "https://www.youtube.com/watch?v=nlppOBB3wNY")

#print(21_jump_street.storyline)
#21_jump_street.show_trailer()

twenty_two_jump_street = media.Movie("22 Jump Street",
                             "Two cops go undercover in college",
                             "https://upload.wikimedia.org/wikipedia/en/1/1d/22_Jump_Street_Poster.png",
                             "https://www.youtube.com/watch?v=v9S_dYuq0vE")

mission_impossible_ghost_protocol = media.Movie("Mission Impossible: Ghost Protocol",
                                                "Spy group goes on their own to save the world",
                                                "https://upload.wikimedia.org/wikipedia/en/b/b5/Mission_impossible_ghost_protocol.jpg",
                                                "https://www.youtube.com/watch?v=EDGYVFZxsXQ")

mission_impossible_rouge_nation = media.Movie("Mission Impossible: Rouge Nation",
                                              "Spy team takes on secret organization to stop global destruction",
                                              "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                                              "https://www.youtube.com/watch?v=pXwaKB7YOjw")

the_lego_movie = media.Movie("The Lego Movie",
                             "The chosen lego sets out to save the Lego world",
                             "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

oblivion = media.Movie("Oblivion",
                       "In a post-apocolyptic world, a routine patrol takes an unexpected turn",
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



movies = [twenty_one_jump_street, twenty_two_jump_street, mission_impossible_ghost_protocol, mission_impossible_rouge_nation, the_lego_movie, oblivion, interstellar, saving_private_ryan, john_wick]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
