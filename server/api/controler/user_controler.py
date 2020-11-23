from flask_restful import Resource, reqparse
from ..model.user_model import User
from server.constant import Constant

class User_controler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def get(self):
        data = User_controler.parser.parse_args()

        # if User.find_by_username(data['username']):
        #         #     return {"message": "A user with that username already exists"}, 400
        #         #
        #         # user = User(data['username'], data['password'])
        #         # user.save_to_db()

        return {"message": "User created successfully."}, Constant.STATUS_CODE['OK']