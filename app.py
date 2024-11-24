from flask import Flask, render_template
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

app = Flask(__name__)

def load_data():
    """加载所有CSV数据文件"""
    try:
        data = {}
        files = {
            '微积分': 'calculus.csv',
            '大学英语四六级': 'CET4_CET6.csv',
            '线性代数': 'linear_algebra.csv',
            '中国近现代史纲要': 'Outline of Modern and Contemporary Chinese History.csv',
            '大学物理': 'university_physics.csv'
        }
        for key, filename in files.items():
            df = pd.read_csv(os.path.join(DATA_DIR, filename))
            # 清理列名
            df.columns = df.columns.str.strip()
            # 转换为字典列表
            data[key] = df.to_dict('records')
        return data
    except Exception as e:
        app.logger.error(f"Error loading data: {str(e)}")
        return {}

@app.route('/')
def index():
    try:
        subjects = load_data()
        return render_template('index.html', subjects=subjects)
    except Exception as e:
        app.logger.error(f"Error rendering index: {str(e)}")
        return "服务器错误，请稍后再试", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)