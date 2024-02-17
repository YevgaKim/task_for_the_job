import requests
import psycopg2
import pycountry

headers = {'X-Auth-Token': "79d4dd1151e84ad9ba749f8367eb8bd6"}
 
name = []
nationality = []
position = []
shirtnumber = []


try:
    for i in range(44,51):
        response = requests.get(f"http://api.football-data.org/v4/persons/{i}", headers=headers)
        player = response.json()

        name.append(player["name"])
        country = pycountry.countries.get(name = player["nationality"])
        nationality.append(country.alpha_2.upper())
        position.append(player["position"])
        shirtnumber.append(int(player["shirtNumber"]))
  
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")




from pathlib import Path
import os
import environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))







try:
    conn = psycopg2.connect(database=env("POSTGRES_NAME"), user=env("POSTGRES_USER"), password=env("POSTGRES_PASSWORD"),port=env("POSTGRES_PORT"), host=env("POSTGRES_HOST"))

    print("Успешно подключено к PostgreSQL")
    cur = conn.cursor()
    count=0
    for name2, nationality2, position2, shirtnumber2 in zip(name, nationality, position, shirtnumber):
        postgres_insert_query = """INSERT INTO example_1_footballplayer 
                                (name, nationality, position, shirtnumber) 
                                VALUES 
                                (%s, %s, %s, %s)"""

        record_to_insert = (name2, nationality2, position2, int(shirtnumber2))
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
    cur.close()
    conn.close()
    print("Соединение с PostgreSQL закрыто")


        

    
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if conn:
        conn.close()
        print("[INFO] PostgreSQL connection closed")