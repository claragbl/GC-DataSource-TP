from flask import Flask

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