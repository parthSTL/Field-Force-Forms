from flask import Flask
import asyncio
app = Flask(__name__)
async def async_get_data():
    asyncio.sleep(10)
    print(1)
@app.route("/")
async def get_data():
    data = async_get_data()
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.run(debug=True)