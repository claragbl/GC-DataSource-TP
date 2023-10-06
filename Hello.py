from flask import Flask, request, render_template
import logging

app = Flask(__name__)

@app.route("/")
def hello_world():

  cookies = request.cookies
  return render_template('helloTemplate.html', cookies=cookies)

@app.route("/logger", methods=['GET', 'POST'])
def logger():
#     # display a log on the server side
#     #app.logger.info("Hi ! I am a log on the server side")
#     print('coucou')

#     # display a log on the browser side 
#     js_code = """
#     <script>
#         console.log("Hi ! I am a log on the browser side");
#     </script>
#     """

  if request.method == 'POST':
    # Retrieve the text from the textarea
    text = request.form.get('textarea')
  
    # Print the text in terminal for verification
    print(text)
  
  return render_template('index.html')
