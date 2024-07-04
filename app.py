import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.managers.db_manager import DBManager
from app.managers.openai_manager import OpenAIManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise KeyError ("Here is error")
    return app

def init_db(app):
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    return db

app = create_app()
db = init_db(app)
db_manager: DBManager = DBManager()
openai_manager: OpenAIManager = OpenAIManager()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
async def ask():
    data = request.get_json()
    question: str = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    try:
        # check if exist before open ai request
        existing_answer: str = db_manager.get_answer_from_database(db, question)
        if existing_answer:
            return jsonify({'message': 'Question got answer successfully', 'answer': existing_answer}), 200

        answer: str = await openai_manager.get_answer(question)
        db_manager.save_question_answer(db, question, answer)
        return jsonify({'message': 'Question got answer successfully', 'answer': answer}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)