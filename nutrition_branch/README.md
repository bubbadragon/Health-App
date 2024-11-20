# Nutrition Analysis via PDF

This project is designed to analyze dietary and health information extracted from PDFs. It uses custom AI agents and tasks to extract, process, and summarize nutritional data. The app integrates various AI functionalities using Python, and dependencies are listed in requirements.txt.

## Files in the Repository

### 1. `agents.py`
Defines custom agents for AI tasks, such as:
   - PDF Agent: Extracts and summarizes meaningful content from a PDF.
   - Writer Task: Analyzes and summarizes dietary information.
   - Nutrition Analysis Agent: Analyzes dietary information and provides actionable recommendations.

### 2. `tasks.py`
Contains custom tasks linked to agents:
   - PDF Task: Extracts nutritional information from a PDF file.
   - Writer Agent: Summarizes extracted information.
   - Nutrition Analysis Task: Provides a detailed breakdown of calories, macro- and micronutrients, and dietary recommendations.


### 3. `main.py`
The main script for executing the project workflow:
   - Prompts the user to select a PDF file.
   - Initializes agents and tasks.
   - Runs the workflow to process and analyze nutritional information.
   - Outputs the results to the user.


### 4. `requirements.txt`
   - Lists all dependencies for the project, including libraries for AI, database management, and file handling.

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

## Usage

- Use this application to analyze PDF-based dietary logs or health-related documents.
- The AI agents work collaboratively to extract, summarize, and provide actionable insights into nutritional data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features.

## Contact

For further questions, please contact the repository owner.
