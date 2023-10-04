from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello_world():
    var = """ <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-SJDP26RN0B"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-SJDP26RN0B');
</script>"""

    return "<p>Hello, World!</p>" +var 

@app.route("/logger")
def logger():
    # display a log on the server side
    #app.logger.info("Hi ! I am a log on the server side")
    print('coucou')

    # display a log on the browser side 
    js_code = """
    <script>
        console.log("Hi ! I am a log on the browser side");
    </script>
    """

    return "<p>Welcome to the logging Page</p>" + js_code