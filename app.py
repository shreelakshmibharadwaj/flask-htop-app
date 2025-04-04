from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask App is Running!</h1><p>Try accessing <a href='/htop'>/htop</a></p>"

@app.route('/htop')
def htop_info():
    name = "Shreelakshmi Bharadwaj"  
    username = os.getenv("USER", "unknown")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = str(e)

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

