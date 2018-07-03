from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '13th trial on Azure CD/CI'

if __name__ == '__main__':
  app.run()
