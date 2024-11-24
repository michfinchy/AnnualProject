from flask import Flask, render_template
import pandas as pd

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