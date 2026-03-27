from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """Lit products.json et retourne une liste de dicts."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Lit products.csv et retourne une liste de dicts."""
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_sql():
    """Lit la table Products depuis products.db et retourne une liste de dicts."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row          # rows accessibles comme des dicts
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Choisir la source de données
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # 2. Filtrer par id si fourni (identique task 03)
    if product_id is not None:
        data = [p for p in data if str(p['id']) == str(product_id)]
        if not data:
            return render_template('product_display.html', error="Product not found")

    # 3. Afficher
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)