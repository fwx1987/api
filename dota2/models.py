from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Player(models.Model):
    # Dota2 ID
    dota2_id = models.CharField(max_length=255, db_index=True,primary_key=True)
    # name of player
    name = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    mmr = models.CharField(max_length=255,blank = True)
    mmr_esitmated = models.CharField(max_length=255,blank = True)
    rank_tier = models.CharField(max_length=255,blank = True)
    leaderboard_rank = models.TextField(blank = True)
    account_id = models.CharField(max_length=255,blank = True)
    personaname = models.TextField(blank = True)
    cheese = models.CharField(max_length=255,blank = True)
    steamid = models.TextField(blank = True)
    avatar = models.TextField(blank = True)
    avatarmedium = models.TextField(blank = True)
    avatarfull = models.TextField(blank = True)
    profileurl = models.TextField(blank = True)
    last_login = models.TextField(blank = True)
    loccountrycode = models.TextField(blank = True)
    is_contributor = models.TextField(blank = True)
    openapi_hash = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return "{} - {}".format(self.dota2_id, self.name)

class Matches(models.Model):
    match_id = models.CharField(max_length=255, db_index=True,primary_key=True)
    barracks_status_dire = models.CharField(max_length=255,blank=True)
    barracks_status_radiant= models.CharField(max_length=255,blank=True)
    chat = models.TextField(blank=True)
    cluster = models.CharField(max_length=255,blank=True)
    cosmetics = models.CharField(max_length=255,blank=True)
    dire_score = models.CharField(max_length=255,blank=True)
    draft_timings = models.TextField(blank=True)
    duration = models.CharField(max_length=255,blank=True)
    engine = models.CharField(max_length=255,blank=True)
    first_blood_time = models.CharField(max_length=255,blank=True)
    game_mode = models.CharField(max_length=255,blank=True)
    human_players = models.CharField(max_length=255,blank=True)
    leagueid = models.CharField(max_length=255,blank=True)
    lobby_type = models.CharField(max_length=255,blank=True)
    match_sequ_num = models.CharField(max_length=255,blank=True)
    negative_votes = models.CharField(max_length=255,blank=True)
    objectives = models.CharField(max_length=255,blank=True)
    picks_bans = models.CharField(max_length=255,blank=True)
    positive_votes = models.CharField(max_length=255,blank=True)
    #Array of the Radiant gold advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their gold disadv

    radiant_gold_adv = models.CharField(max_length=255,blank=True)
    radiant_score = models.CharField(max_length=255,blank=True)

    radiant_win = models.CharField(max_length=255,blank=True)
    radiant_xp_adv = models.CharField(max_length=255,blank=True)
    start_time = models.CharField(max_length=255,blank=True)
    teamfights = models.CharField(max_length=255,blank=True)
    tower_status_dire = models.CharField(max_length=255,blank=True)
    tower_status_radiant = models.CharField(max_length=255,blank=True)
    version = models.CharField(max_length=255,blank=True)

    replay_salt = models.CharField(max_length=255,blank=True)
    series_id = models.CharField(max_length=255,blank=True)
    series_type = models.CharField(max_length=255,blank=True)
    radiant_team = models.CharField(max_length=255,blank=True)
    dire_team = models.CharField(max_length=255,blank=True)
    league = models.CharField(max_length=255,blank=True)

    skill = models.CharField(max_length=255,blank=True)
    players = models.TextField(blank=True)
    patch = models.CharField(max_length=255,blank=True)
    region = models.CharField(max_length=255,blank=True)
    all_word_counts = models.CharField(max_length=255,blank=True)
    throw = models.CharField(max_length=255,blank=True)
    #Maximum gold disadvantage of the player's team if they lost the match
    loss = models.CharField(max_length=255,blank=True)
    #Maximum gold advantage of the player's team if they won the match
    win = models.CharField(max_length=255,blank=True)
    replay_url = models.CharField(max_length=255,blank=True)

    class Meta:
        ordering = ('match_id',)
    def __str__(self):
        return "{} - {}".format(self.match_sequ_num, self.match_id)