from flask import Flask, jsonify, render_template
import random
import os
import webbrowser
webbrowser.open("http://127.0.0.1:8080/")

# 创建 Flask 应用
app = Flask(__name__, static_folder="static", template_folder="templates")

# 场景和图片的映射
scenarios_with_images = {
    "校园生活": "static/images/5.JPG",
    "网络安全": "static/images/4.JPG",
    "朋友社交": "static/images/3.JPG",
    "金钱物质": "static/images/2.JPG",
    "家庭责任与诚信": "static/images/1.JPG",
}

# API 端点：随机选择一个场景
@app.route("/get_random_scenario")
def get_random_scenario():
    selected_scenario = random.choice(list(scenarios_with_images.keys()))
    selected_image_path = scenarios_with_images[selected_scenario]
    return jsonify({"scenario": selected_scenario, "image": selected_image_path})

# 渲染前端页面
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)