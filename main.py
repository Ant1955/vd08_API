# только с VPN для работы
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None
   quotes = det_quotes()
#формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.
   if request.method == 'POST':
#этот определенный город мы будем брать для запроса API
       city = request.form['city']
   # прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
   return render_template("index.html", weather=weather, quotes=quotes)

def get_weather(city):
   api_key = "fda902a077e24b262b0187ca6bc24204"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

def det_quotes():
    # api_key_q = "8b6eeda3fcc07dfce3a83c8da0595131"  for https://favqs.com/api
    url = f"https://favqs.com/api/qotd"
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
   app.run(debug=True)