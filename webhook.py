from flask import Flask, request, jsonify, make_response, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/img/<class_name>/<target>/<studentbook>/<task>')
def get_image(target, class_name, studentbook, task):
  filename = f'./{class_name}/{target}/{studentbook}/{task}/1.png'
  return send_file(filename, mimetype='image/gif')

@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(force=True)
  print(req)
  image_url = "https://gdzbot.ivananikin2011.repl.co/img/6_klass/russkiy/ladyzhenskaya-fgos-2023-465/1"
  response = {"fulfillmentMessages": [{"image": {"imageUri": image_url}}]}

  return jsonify(response)


app.run(host='0.0.0.0', port=81)