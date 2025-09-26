import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        print(f"Trying to save {self.name} with price {self.price}")
        conn = psycopg2.connect(
            dbname="restaurant_db",
            user="postgres",
            password="noha",
            host="localhost",
            port=5433,
            options='-c client_encoding=UTF8'
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
            (self.name, self.price)
        )
        conn.commit()
        print("Item saved!")
        cur.close()
        conn.close()

    def delete(self):
        print(f"Trying to delete {self.name}")
        conn = psycopg2.connect(
            dbname="restaurant_db",
            user="postgres",
            password="noha",
            host="localhost",
            port=5433,
            options='-c client_encoding=UTF8'
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        print("Item deleted!")
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        print(f"Trying to update {self.name} to {new_name} with price {new_price}")
        conn = psycopg2.connect(
            dbname="restaurant_db",
            user="postgres",
            password="noha",
            host="localhost",
            port=5433,
            options='-c client_encoding=UTF8'
        )
        cur = conn.cursor()
        cur.execute(
            "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
            (new_name, new_price, self.name)
        )
        conn.commit()
        print("Item updated!")
        cur.close()
        conn.close()
        self.name = new_name
        self.price = new_price
