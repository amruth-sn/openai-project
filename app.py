from flask import Flask, render_template, request
import config
import script

def page_not_found(e):
    return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'form1' in request.form:
            prompt = request.form['videoTitle']
            vidT = script.generateVideoTitles(prompt)
            videoTitleIdeas = vidT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['videoScript']
            vidT = script.generateVideoScripts(prompt)
            videoScript = vidT.replace('\n', '<br>')
        
        if 'form3' in request.form:
            prompt = request.form['videoIntroOutro']
            vidT = script.videoExpander(prompt)
            videoInOut = vidT.replace('\n', '<br>')
    
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
