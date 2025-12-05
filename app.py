from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Главная страница"""
    with open('templates/index.html', 'r', encoding='utf-8') as file:
        return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/catalog', methods=['GET'])
def catalog():
    """Страница каталога"""
    with open('templates/catalog.html', 'r', encoding='utf-8') as file:
        return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/category', methods=['GET'])
def category():
    """Страница категории"""
    with open('templates/category.html', 'r', encoding='utf-8') as file:
        return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/contacts', methods=['GET'])
def contacts():
    """Страница контактов"""
    with open('templates/contacts.html', 'r', encoding='utf-8') as file:
        return file.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, port=5000)