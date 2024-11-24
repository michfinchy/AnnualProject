from flask import Flask, render_template
import pandas as pd
<<<<<<< HEAD
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
=======

app = Flask(__name__)

@app.route('/')
def index():
    # 读取所有CSV文件
    calculus_df = pd.read_csv('data/calculus.csv')
    cet_df = pd.read_csv('data/CET4_CET6.csv')
    linear_algebra_df = pd.read_csv('data/linear_algebra.csv')
    history_df = pd.read_csv('data/Outline of Modern and Contemporary Chinese History.csv')
    physics_df = pd.read_csv('data/university_physics.csv')
    
    # 为每个数据集准备数据
    subjects = {
        '微积分': calculus_df.to_dict('records'),
        '大学英语四六级': cet_df.to_dict('records'),
        '线性代数': linear_algebra_df.to_dict('records'),
        '中国近现代史纲要': history_df.to_dict('records'),
        '大学物理': physics_df.to_dict('records')
    }
    
    return render_template('index.html', subjects=subjects)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> f366fb29dbf09d8283ad9c275ca4f499f3a02a09
