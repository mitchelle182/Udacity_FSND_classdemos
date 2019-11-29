import psycopg2

connection = psycopg2.connect('dbname=Example1 user=postgres')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE todo (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO todo (id, completed) VALUES (1, true);')

connection.commit()

connection.close()
cursor.close()