# NumberNinja - Math Problem Generator

NumberNinja is a web application that generates customized math problems across various math disciplines including algebra, geometry, calculus, and more. It features both a React frontend and Python backend.

## Features

- Generate customized math problems with different difficulty levels
- Support for multiple math topics: Algebra, Geometry, Trigonometry, Calculus, and more
- Interactive user interface
- View and toggle solutions
- Mobile-friendly design

## Project Structure

The project consists of two main parts:

1. **Python Backend**:
   - Flask API for serving JSON data
   - Streamlit app for local testing

2. **React Frontend**:
   - Modern UI based on the design mockups
   - Connection to the Flask API

## Setup Instructions

### Prerequisites

- Node.js and npm (for the React frontend)
- Python 3.8+ (for the Flask and Streamlit backends)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/adamkai7/hackdavis25.git
   cd hackdavis25
   ```

2. Install Python dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install flask streamlit
   ```

3. Install Node.js dependencies:
   ```
   npm install
   ```

### Running the Application

1. Start the Flask backend:
   ```
   python app.py
   ```
   The Flask server will run on http://localhost:5000

2. (Optional) Run the Streamlit app for testing:
   ```
   streamlit run streamlit_app.py
   ```
   The Streamlit app will run on http://localhost:8501

3. Start the React development server:
   ```
   npm start
   ```
   The React app will run on http://localhost:3000

### Building for Production

1. Build the React app:
   ```
   npm run build
   ```
   This will create a `build` directory with the production-ready files.

2. The Flask app is configured to serve these static files from the `build` directory.

## Deployment

To deploy the application:

1. Build the React app as described above.
2. Copy all files to your server.
3. Run the Flask app on your server:
   ```
   python app.py
   ```

## Project Structure

```
hackdavis25/
├── app.py                  # Flask application
├── streamlit_app.py        # Streamlit application
├── algebra.py              # Algebra problem generator
├── basic_arithmetic.py     # Arithmetic problem generator
├── calculus.py             # Calculus problem generator
├── geometry.py             # Geometry problem generator
├── trignometry.py          # Trigonometry problem generator
├── package.json            # Node.js package configuration
├── webpack.config.js       # Webpack configuration
├── src/                    # React source files
│   ├── index.js            # React entry point
│   ├── App.jsx             # Main React component
│   ├── style.css           # Main CSS styles
│   ├── components/         # React components
│   │   ├── Home.jsx        # Home page component
│   │   ├── Navbar.jsx      # Navigation component
│   │   └── ProblemGenerator.jsx # Problem generator component
├── public/                 # Static files
│   └── index.html          # HTML template
└── build/                  # Production build (after npm run build)
```