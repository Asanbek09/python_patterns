import sqlite3
from pathlib import Path
from random import randint

import redis
from faker import Faker

fake = Faker()

DB_PATH = Path(__file__).parent / Path("quotes.sqlite3")
cache = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

def setup_db():
    try:
        with sqlite3.connect(DB_PATH) as db:
            cursor = db.cursor()
            cursor.execute(
                """create table quotes(id integer primary key, text text)"""
            )
            db.commit()
            print("Table 'quotes' created")
    except Exception as e:
        print(e)


def add_quotes(quotes_list):
    added = []
    try:
        with sqlite3.connect(DB_PATH) as db:
            cursor = db.cursor()

            for quote_text in quotes_list:
                quote_id = randint(1, 100)
                quote = (quote_id, quote_text)

                cursor.execute(
                    """insert or ignore into quotes(id, text) values(?, ?)""", quote
                )
                added.append(quote)
            db.commit()
    except Exception as e:
        print(e)

    return added

def main():
    msg = "Choose your model! Enter 'init' or 'update_db_only' or 'update_all': "
    mode = input(msg)

    if mode.lower() == "init":
        setup_db()
    
    elif mode.lower() == "update_all":
        quotes_list = [fake.sentence() for _ in range(1, 11)]
        added = add_quotes(quotes_list)
        if added:
            print("New (fake) quotes added to the database: ")
            for q in added:
                print(f"Added to DB: {q}")
                print(" - Also adding to the cache")
                cache.set(str(q[0]), q[1], ex=60)

    elif mode.lower() == "update_db_only":
        quotes_list = [fake.sentence() for _ in range(1, 11)]
        added = add_quotes(quotes_list)
        if added:
            print("New (fake) quotes added to the database ONLY:")
            for q in added:
                print(f"Added to DB: {q}")


if __name__ == "__main__":
    main()