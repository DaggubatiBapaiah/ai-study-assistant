AI Study Assistant

An interactive AI-powered Study Assistant that enables users to ask questions and receive explanations in different styles — Friendly or Academic.

The application is built with Gradio, powered by the Google Gemini API, and deployed on Hugging Face Spaces.

🌐 Live Demo

Try the application here:

🔗 https://huggingface.co/spaces/bapaiahchowdary/my-study-assistant

🚀 Features

🧠 Ask questions on any subject

🎭 Select explanation style:

Friendly Mode – Simple, beginner-friendly explanations with relatable examples

Academic Mode – Structured, formal, professor-style responses

⚙️ Controlled response generation using model parameters

🌍 Fully deployed and accessible online

🛠 Tech Stack

Python

Gradio

Google Generative AI (Gemini API)

Hugging Face Spaces

📂 Project Structure
ai-study-assistant/
│
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
└── study_assistant.ipynb  # Development notebook (optional)
⚙️ How It Works

The application dynamically adjusts the system prompt based on the selected personality mode.

Friendly Mode → Encouraging tone, simplified breakdowns

Academic Mode → Formal structure, precise explanations

The selected style is injected into the model configuration before generating the response.

Model parameters such as temperature and token limits are tuned to ensure clarity and consistency.

🖥️ Installation (Run Locally)
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-study-assistant.git
cd ai-study-assistant
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Set your API Key

Linux / macOS:

export GEMINI_API_KEY="your_api_key_here"

Windows:

set GEMINI_API_KEY=your_api_key_here
4️⃣ Run the application
python app.py
📸 Screenshots


📌 Key Learnings

Prompt engineering and system instruction design

API integration with Gemini

Model parameter tuning (temperature, max tokens)

Building interactive AI apps using Gradio

Deploying AI applications on Hugging Face Spaces



🤝 Feedback

Suggestions and improvements are welcome. Feel free to fork the repository or open an issue.
