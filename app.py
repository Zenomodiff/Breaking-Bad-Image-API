from math import ceil
from random import randint, choice
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return '''
	            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Breaking_Bad Image API ☠️⚗️🧪☢️</h1>
      <h2 class="project-tagline">An API returns Breaking Bad Images</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>The Endpoint Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/breakingbad</c ode> will return Random Images from the series Breaking_Bad</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/breakingbad', methods=['GET'])
def breakingbad_pic():
	im_index = randint(1,121)
	file = f'breakingbad/image{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)