from flask import Flask,request,render_template,jsonify
import subprocess
app = Flask(__name__,template_folder='template',static_folder='static')
@app.route("/", methods=["GET"])
def home():
    return render_template('paper.html')
@app.route("/result", methods=["POST"])
def result():
    code = request.form['text']
    fh=open('p1.py','w+')
    fh.write(code)
    fh.close()
    subprocess.run('cat input_filepython.txt | python p1.py >& outputpython.txt',shell=True)
    fh=open('outputpython.txt','r+')
    k=fh.read()
    fh.close()
    return jsonify({'output':k})
if __name__ == "__main__":
    app.run()
