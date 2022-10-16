import json


def read(db_name: str = 'database.json') -> dict:
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.loads(f.read())
            return db
    except Exception as e:
        print(e)


def write(db_name: str, key: str, value: str, column: str = 'books'):
    try:
        db = read(db_name)
        db[column][key] = value
        with open('database.json', 'w', encoding='utf-8') as f:
            json.dump(db, f, indent=4)
    except Exception as e:
        print(e)
