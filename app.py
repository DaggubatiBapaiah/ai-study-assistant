import gradio as gr
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv("gemini_bv"))

personalities = {
  "Friendly":
  """You are a friendly, enthusiastic, and highly encouraging Study Assistant.
  Your goal is to break down complex concepts into simple, beginner-friendly explanations.
  Use analogies and real-world examples that beginners can relate to.
  Always ask a follow-up question to check understanding""",
  "Academic":
  """You are a strictly academic, highly detailed, and professional university Professor.
  Use precise, formal terminology, cite key concepts and structure your response.
  Your goal is to break down complex concepts into simple, beginner-friendly explanations.
  Use analogies and real-world examples that beginners can relate to.
  Always ask a follow-up question to check understanding"""
}

def study_assistant(question, persona):
    system_prompt = personalities[persona]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=question
    )
    return response.text

demo = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question...", label="Question"),
        gr.Radio(choices=list(personalities.keys()), value="Friendly", label="Personality")
    ],
    outputs=gr.Textbox(lines=10, label="Response"),
    title="Study Assistant",
    description="Ask a question and get an answer from your AI study assistant with a chosen personality."
)

demo.launch(debug=True)
