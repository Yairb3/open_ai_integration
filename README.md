# Open Ai Integration project

This project is a Flask-based web application that integrates with OpenAI to answer user questions. It uses SQLAlchemy for database interactions and includes tests for the application's functionality.

## Features

- Ask questions and get answers from OpenAI.
- Save and retrieve question-answer pairs from a PostgreSQL database.
- Easy configuration through environment variables.
- Includes unit tests for key functionalities.

### Local Setup with docker

1. Clone the repository:
   https://github.com/Yairb3/open_ai_integration.git
   cd open_ai_integration
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   install alembic and psycopg2 and upgrade alembic:
   pip3 install alembic
   pip3 install psycopg2
   alembic upgrade head

3. Add env file - will sent by me privatly.
4. In docker compose file - add the env content to 'environment' under 'app' service.
5. Run:  docker compose up --build
6. Tests:
   After running:
      cd .\tests
      pytest
