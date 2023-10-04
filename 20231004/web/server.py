#!/usr/bin/env python
# coding: utf-8

# flask web server를 사용할 수 있게 해주는 라이브러리를 import 한다.
# pip install flask
from flask import Flask, render_template, request
# 추가로 필요한 라이브러리를 import 한다.
import warnings
warnings.filterwarnings(action='ignore')
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import pandas as pd
# ===================================================================================================

# flask 객체를 선언한다.
app = Flask(__name__)

# 입력 데이터를 저장할 placeholder, 가중치 a, 바이어스 b, 배추 가격을 예측하는 수식 y
X = tf.placeholder(dtype=tf.float32, shape=[None, 4])
a = tf.Variable(tf.random_uniform([4, 1]), dtype=tf.float32)
b = tf.Variable(tf.random_uniform([1]), dtype=tf.float32)
y = tf.matmul(X, a) + b

# 텐서플로우 세션을 선언하고 변수 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 디스크에 저장된 학습 모델을 불러와 적용시킨다.
saver = tf.train.Saver()
saver.restore(sess, './model/baechu.ckpt')

# flask의 기본 포트인 5000번 포트의 기본 경로('/')에 사용자가 GET, POST 방식으로 요청했을 때
# render_template() 함수를 이용해서 특정 페이지(index.html)를 브라우저에 표시할 수 있도록 한다.
@app.route('/', methods=['GET', 'POST'])
def index():
    # GET 방식으로 요청하면 index.html 파일을 화면에 표시한다. => 처음 접속할 때
    if request.method == 'GET':
        return render_template('index.html')
    # POST 방식으로 요청하면 사용자가 입력한 데이터를 받는다. => submit 버튼을 클릭했을 때
    else:
        # form에 입력한 데이터를 받는다.
        avg_temp = float(request.form['avg_temp']) # 평균 기온
        min_temp = float(request.form['min_temp']) # 최저 기온
        max_temp = float(request.form['max_temp']) # 최고 기온
        rain_fall = float(request.form['rain_fall']) # 강수량

        # form에 입력된 데이터를 불러온 학습 모델에서 사용하기 위해서 2차원 리스트 형태로 만든다.
        data = [[avg_temp, min_temp, max_temp, rain_fall]]
        # form에 입력한 데이터를 적용시켜 배추 가격을 예측한다.
        result = sess.run(y, feed_dict={X: data})
        # 예측된 배추 가격을 저장한다.
        price = result[0]

        # 예측된 배추 가격이 웹 문서에 출력될 수 있도록 웹 문서로 배추 가격을 넘긴다.
        return render_template('index.html', price = price)

if __name__ == '__main__':
    # flask web server를 실행한다.
    app.run(debug=True)











