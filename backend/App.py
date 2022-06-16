import pymysql as mysql
from flask import jsonify,Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_cors import CORS

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app)
api = Api(app)
@api.route('/test')  # 데코레이터 이용, '/test' 경로에 클래스 등록
class test(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        db = mysql.connect(host='localhost',user='admin',password='1234',charset='utf8',database='blog',cursorclass=mysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute('select * from test;')
        return cursor.fetchall()





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)