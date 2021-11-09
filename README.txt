Design Patterns  

Singleton: I chose to make the Dictionary class in eng_dictionary/dictionary.py a singleton
class. There should only need to be one instance of a dictionary class as all games will share the same dictionary.

Template: Both short_game.py and standard_game.py make use of the game_template.py template.
All games will share the same functions and this allows another game to be added following
the template. (For example, a longer version of the game). All the functions in the template will be required to be implemented in the new version of the game. 

Factory: Since there are two types of games, the obvious solution was to use Factory along side template. This way the user can choose which game they would like to play and the factory will initialize the correct version, either ShortGame or StandardGame.
