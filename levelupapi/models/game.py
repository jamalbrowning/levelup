from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    skill_level = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE)
    game_type = models.ForeignKey("GameType", on_delete=CASCADE)
    number_of_players = models.IntegerField()
# title,game_type,maker,number_of_players,gamer,skill_level
