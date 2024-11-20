from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "Focus on accuracy and detail to provide actionable health insights!"

    def pdf_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
                Extract dietary and health-related information from the PDF provided.
                Use this PDF file as input: {var1}

                {self.__tip_section()}

                Make sure to focus on nutritional data, including calories, macronutrients, micronutrients, and any dietary patterns.
            """
            ),
            expected_output="Extracted dietary and health information.",
            agent=agent,
        )


    def writer_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Analyze the extracted dietary information and write a detailed report.

                Include the following:
                - Caloric intake analysis.
                - Macronutrient (carbs, proteins, fats) breakdown.
                - Micronutrient deficiencies (e.g., vitamins, minerals).
                - Identification of unhealthy dietary patterns.
                - Actionable dietary recommendations for improvement.

                {self.__tip_section()}
            """
            ),
            expected_output="A detailed nutritional analysis and actionable recommendations.",
            agent=agent,
        )


    def nutrition_analysis_task(self, agent):
        return Task(
        description=dedent(
            """
            Use the text extracted from the PDF (Task 1) to analyze the user's dietary habits.
            
            Provide a detailed breakdown of:
            - Calories.
            - Macro-nutrients (carbs, proteins, fats).
            - Micro-nutrients (e.g., vitamins, minerals).
            - Unhealthy eating patterns or deficiencies.

            Suggest actionable dietary improvements.
            """
        ),
        expected_output="Detailed nutritional analysis with actionable recommendations.",
        agent=agent,
    )