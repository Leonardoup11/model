from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  """Return a friendly HTTO greeting"""
  print("I am inside hello world")
  return 'Hello World'

  @app.route('/echo/<name>')
  def echo(name):
    """echo ,name."""

    return f"Hello{name}"
  if _name_ == '_main_':
      app.run(host='127.0.0.1', port=8080, debug=True) 