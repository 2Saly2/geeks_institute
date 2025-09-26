import requests
import psycopg2
import random

DB_CONFIG = {
    "dbname": "restaurant_db",
    "user": "postgres",
    "password": "noha",
    "host": "localhost",
    "port": 5433,
    "options": "-c client_encoding=UTF8"
}

def save_random_countries():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
        response = requests.get(url)
        response.raise_for_status()
        countries = response.json()

        sample_countries = random.sample(countries, 10)

        for country in sample_countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A'
            flag_url = country.get('flags', {}).get('png', '')
            subregion = country.get('subregion', 'N/A')
            population = country.get('population', 0)

            cur.execute("""
                INSERT INTO countries (name, capital, flag, subregion, population)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, capital, flag_url, subregion, population))
            print(f"Added: {name} ({capital})")

        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    save_random_countries()

# j'ai cree la table countries dans la base de donnees restraurant_db 
# pip install requests psycopg2
