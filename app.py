from flask import Flask, render_template_string, request, jsonify
import subprocess

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Server Web Chat</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background:#111; color:#0f0; font-family:monospace; padding:20px;">
    <h2>Server Interactive Interface</h2>
    <div id="chat" style="height:300px; border:1px solid #0f0; overflow-y:scroll; padding:10px; margin-bottom:10px;"></div>
    <input type="text" id="msg" style="width:80%; padding:10px;" placeholder="فەرمان بنووسە...">
    <button onclick="sendMsg()" style="padding:10px; background:#0f0; color:#000;">ناردن</button>

    <script>
        function sendMsg() {
            let m = document.getElementById('msg').value;
            let chat = document.getElementById('chat');
            chat.innerHTML += "<div>> " + m + "</div>";

            fetch('/cmd', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: m})
            })
            .then(res => res.json())
            .then(data => {
                chat.innerHTML += "<div>Server: " + data.reply + "</div>";
                chat.scrollTop = chat.scrollHeight;
            });
            document.getElementById('msg').value = '';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/cmd', methods=['POST'])
def cmd():
    user_msg = request.json.get('message')
    # لێرەدا دەتوانیت پەیوەندی بە مێشکی سیستمەکەت یان سکریپتەکانتەوە بکەیت
    reply = f"پەیامەکەت گەیشت: {user_msg}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
