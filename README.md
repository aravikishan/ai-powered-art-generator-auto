# AI-Powered Art Generator

## Overview

The AI-Powered Art Generator is a sophisticated web application that leverages artificial intelligence to create unique art pieces based on user-defined prompts. This project is designed to democratize the art creation process, allowing users from various backgrounds—whether artists, hobbyists, or digital art enthusiasts—to explore and generate art effortlessly. The application provides a seamless experience with a user-friendly interface, enabling users to generate, view, and manage AI-generated artworks.

The backend, powered by FastAPI, efficiently handles requests for art generation, manages user data, and serves dynamic content to the frontend. The frontend, built with HTML, CSS, and JavaScript, offers a responsive and interactive user experience, ensuring accessibility across different devices.

## Features

- **AI Art Generation**: Create unique art pieces based on custom prompts provided by users.
- **Art Gallery**: Browse and explore a collection of AI-generated artworks in a visually appealing gallery.
- **User Profiles**: Manage personal information and view saved artworks in a dedicated profile section.
- **Responsive Design**: Enjoy a consistent and optimized experience across various devices with a responsive layout.
- **Dynamic Content Loading**: Fetch and display artworks dynamically in the gallery without page reloads.
- **Smooth Navigation**: Experience smooth scrolling and intuitive navigation interactions.
- **Form Validation**: Ensure user inputs are valid with client-side form validation mechanisms.

## Tech Stack

| Component       | Technology       |
|-----------------|------------------|
| Backend         | FastAPI          |
| Frontend        | HTML, CSS, JS    |
| Database        | SQLite           |
| ORM             | SQLAlchemy       |
| Templating      | Jinja2           |
| API             | FastAPI          |
| Web Server      | Uvicorn          |

## Architecture

The application follows a client-server architecture where the FastAPI backend serves dynamic content to the frontend. The backend handles HTTP requests, manages database interactions, and serves HTML pages using Jinja2 templates. SQLAlchemy ORM is utilized to manage the database, storing user data and generated artworks.

```plaintext
+-----------------+      +-----------------+
|  Frontend       | <--> |  Backend        |
| (HTML/CSS/JS)   |      | (FastAPI)       |
+-----------------+      +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+      +-----------------+
|  User Requests  |      |  Database       |
|                 | <--> | (SQLite)        |
+-----------------+      +-----------------+
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- Docker (optional for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-art-generator-auto.git
   cd ai-powered-art-generator-auto
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
2. Visit the application at [http://localhost:8000](http://localhost:8000)

## API Endpoints

| Method | Path                | Description                        |
|--------|---------------------|------------------------------------|
| GET    | `/`                 | Home page                          |
| GET    | `/generate`         | Art generation page                |
| GET    | `/gallery`          | View art gallery                   |
| GET    | `/profile`          | User profile page                  |
| GET    | `/about`            | About the project                  |
| POST   | `/api/generate-art` | Generate art from a prompt         |
| GET    | `/api/gallery`      | Retrieve all art pieces            |
| POST   | `/api/save-art`     | Save an art piece by ID            |
| GET    | `/api/user-profile` | Get mock user profile data         |

## Project Structure

```plaintext
ai-powered-art-generator-auto/
├── Dockerfile              # Docker configuration file
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── start.sh                # Shell script to start the application
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet for the application
│   └── js/
│       └── main.js         # JavaScript for interactivity
└── templates/
    ├── about.html          # About page template
    ├── gallery.html        # Gallery page template
    ├── generate.html       # Art generation page template
    ├── index.html          # Home page template
    └── profile.html        # User profile page template
```

## Screenshots

*Screenshots of the application interface will be added here.*

## Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t ai-powered-art-generator .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 ai-powered-art-generator
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

---
Built with Python and FastAPI.