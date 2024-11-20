import os
from textwrap import dedent

from crewai import Crew
from decouple import config

from nutrition_branch.agents import CustomAgents
from nutrition_branch.tasks import CustomTasks

from tkinter import Tk, filedialog

os.environ["OPENAI_API_KEY"] = "API_KEY"

def select_pdf_file():
    """Opens a file dialog for the user to select a PDF file."""
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF files", "*.pdf")],
    )
    return file_path

class CustomCrew:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        pdf_agent = agents.pdf_agent(self.pdf_path)
        nutrition_agent = agents.writer_agent()
        

        # Custom tasks include agent name and variables as input
        pdf_extraction_task = tasks.pdf_task(
            pdf_agent, self.pdf_path
            )
        
        nutrition_analysis_task = tasks.nutrition_analysis_task(
            nutrition_agent
            )

        # task1 = tasks.pdf_task(
        #     pdf_agent,
        #     self.var1
        # )

        # task2 = tasks.writer_task(
        #     writer_agent,
        # )

        # Define your custom crew here
        crew = Crew(
            agents=[pdf_agent, nutrition_agent],
            tasks=[pdf_extraction_task, nutrition_analysis_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Nutrition Analysis via PDF")
    print("---------------------------------------")
    
    pdf_path = select_pdf_file()

    if not pdf_path:
        print("Error: No file selected. Please select a valid PDF file.")
    elif not os.path.exists(pdf_path):
        print("Error: File not found. Please select a valid PDF file.")
    else:
        custom_crew = CustomCrew(pdf_path)
        result = custom_crew.run()
        print("\n\n########################")
        print("## Nutrition Analysis Result:")
        print("########################\n")
        print(result)
