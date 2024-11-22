# **AI Workflow for Multi-Agent Automation**

## **Objective**
The goal of this project is to create a multi-agent workflow using Streamlit that:
1. Fetches research information about a company and its industry using the Serper API.
2. Utilizes AI models to generate unique use cases and detailed descriptions based on the research data.
3. Provides a seamless and interactive user experience in a web-based application.

---

## **Project Use Case**
This project automates the generation of actionable AI use cases tailored to a specific company and its industry. 
It is ideal for:
- Market research teams looking to explore AI implementation opportunities.
- Businesses aiming to identify innovative AI-driven solutions.
- Developers creating proof-of-concept AI use cases for clients.

For example:
- **Company Name:** GreenTech  
- **Industry:** Renewable Energy  
- **Output Use Case:**  
  "AI-powered solar energy optimization system."  
- **Detailed Description:**  
  "This use case focuses on leveraging AI to analyze weather patterns and optimize solar energy generation, ensuring maximum efficiency and cost-effectiveness for renewable energy providers."

---

## **Project Structure**
```plaintext
TASK/
├── app.py                  # Main Streamlit app
├── src/
│   ├── research_agent.py   # Fetches industry information using an API
│   ├── use_case_agent.py   # Generates use cases using Hugging Face models
│   └── utils.py            # Common utility functions
├── config.py               # API keys and configurations
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions
