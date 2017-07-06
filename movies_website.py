import movies
import web

toy_story = movies.Movie("Toy Story", "A story of a boy and his toys that comes to life", "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.trailer_youtube_url)

avatar = movies.Movie("Avatar", "A marine on an alien planet", "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

captain_america = movies.Movie("Captain America", "Story of the first avenger", "https://images-na.ssl-images-amazon.com/images/I/91H7VE0pSvL._AC_UL320_SR210,320_.jpg", "https://www.youtube.com/watch?v=JerVrbLldXw")
#captain_america.show_trailer()

the_a_team = movies.Movie("The A Team", "A group of Iraq War vetarans who were falsely accused of murder and theft looks to clear their name", "https://i.ytimg.com/vi/QvAuAba4RH0/movieposter.jpg", "https://www.youtube.com/watch?v=exyzEFrmLuM")

limitless = movies.Movie("Limitless", "Story of a guy who takes a new kind of drug which changes his life", "https://www.flickeringmyth.com/wp-content/uploads/2015/01/limitless-movie-poster-new-2.jpg", "https://www.youtube.com/watch?v=4TLppsfzQH8")

grownups = movies.Movie("Grown ups", "Comedy movie about a group of friends", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0ODYwNzU5Nl5BMl5BanBnXkFtZTcwNTI1MTgxMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=e01NVCveGkg")

movies_list = [toy_story,avatar,captain_america,the_a_team,limitless,grownups]

web.open_movies_page(movies_list)


