from flask import Blueprint, render_template, request, redirect, url_for
from config import get_db_connection

menu_bp = Blueprint('menu', __name__)

# ---------- Show Menu ----------
@menu_bp.route('/menu')
def menu():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu_items")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('menu.html', items=items)

# ---------- Add Item ----------
@menu_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)", (name, price))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('menu.menu'))
    return render_template('add_item.html')

# ---------- Delete Item ----------
@menu_bp.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu_items WHERE item_id = %s", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('menu.menu'))

# ---------- Update Item ----------
@menu_bp.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        cur.execute(
            "UPDATE menu_items SET item_name=%s, item_price=%s WHERE item_id=%s",
            (name, price, item_id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('menu.menu'))

    cur.execute("SELECT * FROM menu_items WHERE item_id = %s", (item_id,))
    item = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('update_item.html', item=item)
