import os
import sqlite3
from copy import deepcopy
from dotenv import load_dotenv

from discord import Embed

from constants import EMBED_COLOR, ERR_COLOR

#########=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Embed helper functions

def get_embed_from_dict(ctx, fields, name=None, description=None):
    emb = Embed(color=EMBED_COLOR, description=description)
    for title, value in fields.items():
        emb.add_field(name=title, value=value, inline=True)
    return emb

def get_embed_from_list_of_cover_item(ctx, fields, name=None, description=None):
    artists = "\n".join([f"{c.artist}" for c in fields])
    titles = "\n".join([f"{c.title}" for c in fields])
    emb = Embed(color=EMBED_COLOR, description=description)
    emb.add_field(name="Artist", value=artists)
    emb.add_field(name="Title", value=titles)
    return emb

def get_message_embed(ctx, message):
    emb = Embed(color=EMBED_COLOR, description=message)
    return emb

def get_err_embed(ctx, message):
    emb = Embed(color=ERR_COLOR, description=message)
    return emb

##===================================================================================