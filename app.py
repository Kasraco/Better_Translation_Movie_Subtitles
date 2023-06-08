from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
   ''' this is a main page of the Better translate videos subtitle
   '''
   return 'Hello World'
