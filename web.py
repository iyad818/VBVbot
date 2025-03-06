import os
import subprocess
import threading
from flask import Flask

app = Flask(__name__)

# دالة لتشغيل bot.py وإعادة تشغيله عند التوقف
def run_bot():
    while True:
        process = subprocess.Popen(["python", "bot.py"])
        process.wait()  # ينتظر انتهاء العملية قبل إعادة تشغيلها

# تشغيل البوت في Thread منفصل
threading.Thread(target=run_bot, daemon=True).start()

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
