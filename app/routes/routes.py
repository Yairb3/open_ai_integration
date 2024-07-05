

from flask import jsonify, render_template, request


def configure_routes(app, db, db_manager, openai_manager):
    

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