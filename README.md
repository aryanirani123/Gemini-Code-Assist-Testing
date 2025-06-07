# Gemini-Code-Assist-Testing

This project is a simple web application that displays event information and a schedule of talks for a fictional tech conference. It allows users to view event details, browse the talk schedule, and search for talks by title, speaker, category, or keywords in the description.

The application is built using Python with the Flask framework for the backend and HTML, CSS, and JavaScript for the frontend. Event and talk data is loaded from a `event_data.json` file.

## Features

*   **Event Information Display (FR1.0):** Shows the main event's name, date, time, venue, and description.
*   **Talk Schedule Display (FR2.0):** Lists all scheduled talks.
*   **Talk Details (FR2.1):** For each talk, displays:
    *   Title
    *   Description
    *   Start Time, End Time, Duration
    *   Speaker(s) (First Name, Last Name, Company)
    *   Categories
*   **Search Functionality (FR3.0):**
    *   **Dynamic Filtering (FR3.1):** Filters talks in real-time as the user types.
    *   **Search by Title (FR3.2):** Matches against talk titles.
    *   **Search by Speaker (FR3.3):** Matches against speaker names.
    *   **Search by Category (FR3.4):** Matches against talk categories.
    *   **Search by Keyword (FR3.5):** Matches keywords within talk descriptions.
    *   **Case-Insensitive Search (FR3.6):** Search is not case-sensitive.
    *   **Clear Search (FR3.7):** A button to clear the search input and reset the talk list.
    *   **No Results Message:** Displays a message if no talks match the search criteria.
*   **Speaker Information Modal (FR5.0):**
    *   Clicking on a speaker's name in the talk details now opens a modal window.
    *   The modal displays the speaker's full name, company, a short biography, and their image.
*   **Deployment Ready (FR4.0):** Configured for deployment to Google Cloud Run.

## Data Structure (`event_data.json`)

The `event_data.json` file contains the core data for the event and talks. The `talks` array includes a list of talk objects, and each talk object can have one or more speakers. The structure for a speaker object within the `talk.speakers` array has been updated as follows:

```json
{
  "firstName": "Priya",
  "lastName": "Sharma",
  "companyName": "InnovateAI Corp",
  "bio": "A short biography of the speaker. This field contains a string, which can include details about the speaker's expertise, experience, and contributions.",
  "imageUrl": "A URL to the speaker's image (e.g., https://via.placeholder.com/150/0000FF/FFFFFF?Text=PriyaS)"
}
```
*   `firstName`: The first name of the speaker.
*   `lastName`: The last name of the speaker.
*   `companyName`: The company or organization the speaker is affiliated with.
*   `bio`: A textual biography of the speaker.
*   `imageUrl`: A direct URL to an image of the speaker.

## Technologies Used

*   **Backend:** Python, Flask, Gunicorn (for production)
*   **Frontend:** HTML, CSS, JavaScript
*   **Data:** JSON
*   **Deployment:** Docker (optional, for Cloud Run), Google Cloud Run, Google Cloud Buildpacks

## Setup and Running Locally

1.  **Clone the repository (if applicable).**
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate.bat  # On Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
5.  Open your browser and navigate to `http://127.0.0.1:5000/`.

## Deployment

This application is configured for deployment to Google Cloud Run.

### Using Source Deployment (with Buildpacks and Procfile)

1.  Ensure you have the Google Cloud SDK installed and configured (`gcloud init`).
2.  Enable necessary APIs (`run.googleapis.com`, `cloudbuild.googleapis.com`).
3.  Navigate to the project root directory.
4.  Deploy using the `gcloud` command:
    ```bash
    gcloud run deploy YOUR_SERVICE_NAME \
        --source . \
        --platform managed \
        --region YOUR_REGION \
        --allow-unauthenticated
    ```
    (Replace `YOUR_SERVICE_NAME` and `YOUR_REGION` accordingly.)

Refer to the Google Cloud Run documentation for more details on deployment options.