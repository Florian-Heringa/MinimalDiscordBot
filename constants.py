import os
from dotenv import load_dotenv

## Set up globals and environment variables
load_dotenv()

EMBED_COLOR = int(os.getenv("EMBED_COLOR"), 16)
ERR_COLOR = int(os.getenv("ERR_COLOR"), 16)
HELP_EMBED_COLOR = int(os.getenv("HELP_EMBED_COLOR"), 16)