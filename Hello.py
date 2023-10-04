from flask import Flask, request, render_template
import logging

app = Flask(__name__)

@app.route("/")
def hello_world():
#     var = """ <!-- Google tag (gtag.js) -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=G-SJDP26RN0B"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){dataLayer.push(arguments);}
#   gtag('js', new Date());

#   gtag('config', 'G-SJDP26RN0B');
# </script>"""

#     return "<p>Hello, World!</p>" +var 

  # var = """
  #   <!-- Google tag (gtag.js) -->
  #   <script async src="https://www.googletagmanager.com/gtag/js?id=G-FVQS2TWEVX"></script>
  #   <script>
  #     window.dataLayer = window.dataLayer || [];
  #     function gtag(){dataLayer.push(arguments);}
  #     gtag('js', new Date());

  #     gtag('config', 'G-FVQS2TWEVX');
  #   </script>
    
  #   <button onclick="makeGoogleRequest()">Make Google Request</button> <!-- Add the button -->

  #   <script>
  #     function makeGoogleRequest() {
  #       // Use JavaScript to make a request to Google when the button is clicked
  #       var req = new XMLHttpRequest();
  #       req.open("GET", "https://www.google.com/", true);
  #       req.send();
  #     }
  #   </script>
  #   """
  # return "<p>Hello, World! :)</p>" + var
  return render_template('helloTemplate.html')

@app.route("/logger", methods=['GET', 'POST'])
# def logger():
#     # display a log on the server side
#     #app.logger.info("Hi ! I am a log on the server side")
#     print('coucou')

#     # display a log on the browser side 
#     js_code = """
#     <script>
#         console.log("Hi ! I am a log on the browser side");
#     </script>
#     """

#     form = """
#     <form method="POST">
#         <label for="message">Enter a message:</label>
#         <input type="text" id="message" name="message">
#         <input type="submit" value="Submit">
#     </form>
#     """

#     return "<p>Welcome to the logging Page</p>" + js_code + form
def logger():
    if request.method == 'POST':
        # Retrieve the text from the textarea
        text = request.form.get('textarea')
  
        # Print the text in terminal for verification
        print(text)
  
    return render_template('index.html')
