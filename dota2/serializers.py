from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (("dota2_id","name","created","updated","mmr","mmr_esitmated","rank_tier", "leaderboard_rank", "account_id", "personaname", "cheese", "steamid", "avatar", "avatarmedium", "avatarfull", "profileurl", "last_login", "loccountrycode","is_contributor", "openapi_hash"))


    # name of player
