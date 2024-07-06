# Open Ai Integration project

This project is a Flask-based web application that integrates with OpenAI to answer user questions. It uses SQLAlchemy for database interactions and includes tests for the application's functionality.

## Features

- Ask questions and get answers from OpenAI.
- Save and retrieve question-answer pairs from a PostgreSQL database.
- Easy configuration through environment variables.
- Includes unit tests for key functionalities.

### Local Setup with docker

1. Clone the repository:
   - git clone https://github.com/Yairb3/open_ai_integration.git
   - cd open_ai_integration

2. Add .env file - will sent by me privately .
3. In docker compose file - add the env content to 'environment' under 'app' service.
4. Run:  docker compose up --build

