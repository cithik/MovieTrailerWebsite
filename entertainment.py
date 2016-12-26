import fresh_tomatoes
import media

#Creating instances of class Movie
mummyreturns=media.Movie("Mummy Returns",
                         "It is about Egyptian culture",
                         "http://mediaonlinebd.com/wp-content/uploads/2015/09/the-mummy-returns.jpg",
                         "https://www.youtube.com/watch?v=ptmLrNpmcBo")

minion=media.Movie("Minion",
                   "It is about Egyptian culture",
                   "http://www.minionnation.co.uk/images/shareimage.jpg",
                   "https://www.youtube.com/watch?v=dVDk7PXNXB8")

starwars=media.Movie("StarWars",
                     "Star Wars is an American epic space opera franchise, centered on a film series",
                     "https://media.starwars.ea.com/content/starwars-ea-com/en_US/starwars/battlefront/news-articles/collect-iconic-heroes-and-dominate-the-universe-in-star-wars-gal/_jcr_content/featuredImage/renditions/rendition1.img.jpg",
                     "https://www.youtube.com/watch?v=sGbxmsDFVnE")

spiderman=media.Movie("Spiderman",
                      "Spider-Man is a fictional superhero appearing in American comic books published by Marvel Comics",
                      "https://lumiere-a.akamaihd.net/v1/images/image_ccc4b657.jpeg",
                      "https://www.youtube.com/watch?v=vxoJL60Q_vo")

wolverine=media.Movie("The Wolverine",
                      "Wolverine is a mutant who possesses animal-keen senses, enhanced physical capabilities.",
                      "http://cdn.idigitaltimes.com/sites/idigitaltimes.com/files/2016/04/27/wolverinex-menapocalpse.jpg",
                      "https://www.youtube.com/watch?v=rsTTPd09l5M")

frozen=media.Movie("Frozen",
                   "When their kingdom becomes trapped in perpetual winter, fearless Anna joins forces to save their kingdom",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcTIaSaZM-kGnMKWNNMW9-_yv008JrEh58Ab3DAV1geUNJvXeyXS",
                   "https://www.youtube.com/watch?v=TbQm5doF_Uc")

#Creating an array of Movie instances
movies=[mummyreturns, minion, starwars, spiderman, wolverine, frozen]

#Passing the array to fresh_tomatoes file as input
fresh_tomatoes.open_movies_page(movies)

