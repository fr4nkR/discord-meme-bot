from db_commands import create_tables
from reddit_brain import get_memes
def main():
    create_tables()
    get_memes()
