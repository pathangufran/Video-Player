# Video-Player
# Interactive Video Player with Custom Subtitles

This project is an interactive web application that allows users to upload videos, add custom subtitles, and view these subtitles in sync with the video. It is developed using Vue.js for the frontend and Django for the backend.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Frontend Development](#frontend-development)
- [Backend Development](#backend-development)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload video files.
- Add custom subtitles with timestamps.
- Play videos with synchronized subtitles.

## Getting Started

### Prerequisites

- Node.js and npm
- Python (3.6 or higher)
- [Django](https://www.djangoproject.com/)
- [Vue CLI](https://cli.vuejs.org/guide/installation.html)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pathangufran/Video-Player.git
   cd Video-Player
2. **frontend:
cd frontend
npm install
3 **backend:
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Usage
1 Run the frontend:
cd frontend
npm run serve
2 Run the backend:
python manage.py runserver

### Frontend Development
The frontend is developed using Vue.js.
front-end interface where users can:
a. Upload a video file.
b. Add custom subtitles at specific timestamps in the video using a text box.
c. Play the uploaded video.
d. View existing subtitles in sync with the video.

### Backend Development
The backend is built using Django, a high-level Python web framework.
API endpoints are defined to manage video and subtitle uploads, along with retrieving subtitles.
Created an API endpoint that can:
a. Receive the uploaded video file from backend and store it.
b. Create and store a subtitles file using the data that is submitted by the user.
This file will contain the subtitles text and associate it with specific timestamps
on the video.
c. Retrieve subtitles file associated with the video for user to play it. 

### Contributing
Contributions are encouraged! Fork the repository and create pull requests to propose improvements.


