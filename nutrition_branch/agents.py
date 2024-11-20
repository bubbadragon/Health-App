from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def pdf_agent(self, pdf_path):

        pdf_tool = PDFSearchTool(pdf_path)

        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent(f"""You are an expert at finding relevant information in PDF files."""),
            goal=dedent(f"""Extract and summarize meaningful content from the provided PDF file."""),
            tools=[pdf_tool],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def writer_agent(self):
        return Agent(
            role="Writer",
            backstory=dedent(f"""All your life you have loved writing summaries."""),
            goal=dedent(f"""Take the information from the pdf agent and summarize it nicely."""),
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def nutrition_analysis_agent(self, extracted_text):
         return Agent(
            role="Nutrition Analyst",
            backstory=dedent("""
                You are an expert in nutrition. Your goal is to analyze dietary logs for caloric and nutrient intake, 
                highlight deficiencies, and provide actionable insights for better health.
            """),
            goal=dedent("""
                Provide a detailed breakdown of calories, macro-nutrients (carbs, proteins, fats), and micro-nutrients.
                Identify unhealthy eating patterns and suggest improvements.
            """),
            verbose=True,
            llm=self.OpenAIGPT4,
        )