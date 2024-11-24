from flask import Flask, render_template
import pandas as pd
import os

# 设置基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

app = Flask(__name__)

def load_data():
    """加载所有CSV数据文件"""
    try:
        data = {
            '微积分': pd.read_csv(os.path.join(DATA_DIR, 'calculus.csv')),
            '大学英语四六级': pd.read_csv(os.path.join(DATA_DIR, 'CET4_CET6.csv')),
            '线性代数': pd.read_csv(os.path.join(DATA_DIR, 'linear_algebra.csv')),
            '中国近现代史纲要': pd.read_csv(os.path.join(DATA_DIR, 'Outline of Modern and Contemporary Chinese History.csv')),
            '大学物理': pd.read_csv(os.path.join(DATA_DIR, 'university_physics.csv'))
        }
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

# 仅在直接运行时使用，生产环境使用 wsgi
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)