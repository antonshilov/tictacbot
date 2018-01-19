from flask import Flask, request, make_response, abort
from flask_restful import Resource, Api
import  nf

import tictactoe


app = Flask(__name__)
api = Api(app)


class Game(Resource):
    def post(self, room):
        data = request.get_data(True, True)
        try:
            board = nf.bot(data)
            print(board)
            return make_response(board)
        except NameError:
            return abort(418)
        except ValueError:
            return abort(418)


class Name(Resource):
    def get(self):  # param is pulled from url string
        # try:
        #     header = request.headers.get('Authorization')
        #     header == "Bearer TOKEN"
        # except:
        #     return abort(403)
        # if header == 'Bearer':
        result = "SUPA BOT"
        return make_response(result)
        # else:
        #     abort(403)


api.add_resource(Game, '/api/v1/<string:room>')  # bind url identifier to class
api.add_resource(Name, '/')  # bind url identifier to class

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
