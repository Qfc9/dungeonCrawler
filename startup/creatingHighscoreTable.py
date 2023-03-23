import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=password")
# Open a cursor to perform database operations
cur = conn.cursor()

try:
    # To add our table to the DB
    cur.execute("""
        CREATE TABLE public.highscoreDC (
            id serial NOT NULL,
            "name" varchar NOT NULL,
            level int NOT NULL,
            "timestamp" timestamp NOT NULL
        );

        ALTER TABLE public.highscoreDC ADD CONSTRAINT highscoreDC_pk PRIMARY KEY (id);
        
        CREATE INDEX highscoreDC_level_idx ON public.highscoreDC (level);
    """)

    # Push our changes to the table
    conn.commit()

# If it was a duplicate table error
except psycopg2.errors.DuplicateTable as e:
    pass

# If it was any other type of error
except Exception as e:
    print("Oh no, something bad happened!")
    print(e)
    exit()

print("Everything went well")

conn.close()