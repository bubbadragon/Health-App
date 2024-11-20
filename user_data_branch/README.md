
# SQL Database Analysis

This repository contains the AI logic and database setup for a health app. The app utilizes SQLite for storing workout data, Python scripts for database interactions, and various Python packages listed in the requirements.

## Files in the Repository

### 1. `enviroment.env`
   - Environment configuration file that includes sensitive credentials and settings needed to run the project.
   - Ensure this file is configured correctly before running the application.

### 2. `load_sql_data.py`
   - A Python script to load workout data into the SQLite database.
   - Use this script to initialize or update your workout data in `workout_data.db`.

### 3. `requirements.txt`
   - Lists all the dependencies needed to run this project.
   - Install dependencies with:
     ```bash
     pip install -r requirements.txt
     ```
   - Key dependencies include libraries for HTTP requests, database management, and data handling.

### 4. `run.py`
   - Main entry point to run the application.
   - This script may include logic to start the app, connect to the database, and utilize various AI functionalities.

### 5. `sql_agents.py`
   - Contains functions or classes to interact with the SQLite database.
   - This file defines agents or modules for handling database queries related to workout data.

### 6. `workout_data.db`
   - SQLite database file that stores workout data.
   - It’s recommended to back up this file regularly as it contains valuable workout information.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bubbadragon/Health-App.git
   cd Health-App/ai_logic
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Environment**:
   - Set up the `enviroment.env` file with the necessary variables. Refer to the file’s template to understand what each variable represents.

4. **Load Data into the Database**:
   Run the `load_sql_data.py` script to populate the database with initial data:
   ```bash
   python load_sql_data.py
   ```

5. **Run the Application**:
   Start the application with:
   ```bash
   python run.py
   ```

## Usage

- **Database Operations**: The `sql_agents.py` file provides functionalities to query and manipulate workout data in `workout_data.db`.
- **Main Application**: Use `run.py` to execute the main logic of the health app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features.

## Contact

For further questions, please contact the repository owner.
