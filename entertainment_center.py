import media
import fresh_tomatoes

# create new movie objects (one object per movie)...
to_kill_a_mockingbird = media.Movie("To Kill a Mockingbird",
                                    1962,
                                    "Atticus Finch, a lawyer in the "
                                    "Depression-era South, defends a black "
                                    "man against an undeserved rape charge, "
                                    "and his kids against prejudice.",
                                    "http://upload.wikimedia.org/wikipedia/en"
                                    "/8/8e/To_Kill_a_Mockingbird_poster.jpg",
                                    "https://www.youtube.com/"
                                    "watch?v=KR7loA_oziY")

johnny_got_his_gun = media.Movie("Johnny Got His Gun",
                                 1971,
                                 "A young American soldier (Joe) in WW I "
                                 "is wounded by a landmine. He loses his "
                                 "arms, legs and eyes as well as his "
                                 "ability to hear, speak or smell. Lying "
                                 "in hospital, he is not able to distinguish "
                                 "if he is awake or if he is dreaming. "
                                 "Trying to find out, he relives his story "
                                 "in strange dreams and memories.",
                                 "https://upload.wikimedia.org/wikipedia/"
                                 "en/2/29/Johnny_Got_His_Gun_poster.jpg",
                                 "https://www.youtube.com/"
                                 "watch?v=qB7j4C6hBBA")

blazing_saddles = media.Movie("Blazing Saddles",
                              1974,
                              "To ruin a western town, a corrupt "
                              "political boss appoints a black sheriff, who "
                              "promptly becomes his most formidable "
                              "adversary.",
                              "http://upload.wikimedia.org/wikipedia/en/thumb"
                              "/7/7b/Blazing_saddles_movie_poster.jpg/"
                              "225px-Blazing_saddles_movie_poster.jpg",
                              "https://www.youtube.com/watch?v=iLNQv19YpG4")

airplane = media.Movie("Airplane!",
                       1980,
                       "An airplane crew takes ill. Surely the only person "
                       "capable of landing the plane is an ex-pilot afraid "
                       "to fly. But don't call him Shirley.",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/f/f5/"
                       "Airplane%21.jpg/220px-Airplane%21.jpg",
                       "https://www.youtube.com/watch?v=rzRJWy-3_Dc")

top_gun = media.Movie("Top Gun",
                      1986,
                      "As students at the United States Navy's elite fighter "
                      "weapons school compete to be best in the class, one "
                      "daring young pilot learns a few things from a "
                      "civilian instructor that are not taught in the "
                      "classroom.",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/"
                      "4/46/Top_Gun_Movie.jpg/220px-Top_Gun_Movie.jpg",
                      "https://www.youtube.com/watch?v=qAfbp3YX9F0")

naked_gun = media.Movie("The Naked Gun",
                        1988,
                        "Incompetent cop Frank Drebin has to foil an attempt "
                        "to assassinate Queen Elizabeth II.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/5/5f/"
                        "The_Naked_Gun_Poster.jpg/"
                        "220px-The_Naked_Gun_Poster.jpg",
                        "https://www.youtube.com/watch?v=PACTQutbow4")

glory = media.Movie("Glory",
                    1989,
                    "Robert Gould Shaw leads the US Civil War's first "
                    "all-black volunteer company, fighting prejudices of "
                    "both his own Union army and the Confederates.",
                    "https://upload.wikimedia.org/wikipedia/en/e/e6/"
                    "Glory_ver1.jpg",
                    "https://www.youtube.com/watch?v=iTyyvQA_5h4")

unforgiven = media.Movie("Unforgiven",
                         1992,
                         "Retired Old West gunslinger William Munny "
                         "reluctantly takes on one last job, with the help "
                         "of his old partner and a young man.",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/4/"
                         "4e/Unforgiven_2.jpg/220px-Unforgiven_2.jpg",
                         "https://www.youtube.com/watch?v=yrCuOdc5AGM")

schindlers_list = media.Movie("Schindler's List",
                              1993,
                              "In Poland during World War II, Oskar "
                              "Schindler gradually becomes concerned for his "
                              "Jewish workforce after witnessing their "
                              "persecution by the Nazis.",
                              "http://upload.wikimedia.org/wikipedia/en/"
                              "thumb/3/38/Schindler%27s_List_movie.jpg/"
                              "220px-Schindler%27s_List_movie.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA")

# generate HTML file based on above movie objects above and 
# open in a web browser
# the open_movies_page method accepts one argument: a list of movie objects
fresh_tomatoes.open_movies_page([to_kill_a_mockingbird,
                                 johnny_got_his_gun,
                                 blazing_saddles,
                                 airplane,
                                 top_gun,
                                 naked_gun,
                                 glory,
                                 unforgiven,
                                 schindlers_list])