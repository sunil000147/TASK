from transformers import pipeline

# Initialize Hugging Face summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_use_case_and_description(company_name, snippet):
    """
    Generate relevant use cases and detailed descriptions using summarization.
    """
    use_case_prompt = f"Generate a unique AI use case for {company_name}. Here is some industry info: {snippet}."
    description_prompt = f"Provide a detailed description for this AI use case for {company_name}: {snippet}."

    # Generate the use case
    use_case = summarizer(use_case_prompt, max_length=50, min_length=15, do_sample=False)
    # Generate the description
    description = summarizer(description_prompt, max_length=130, min_length=50, do_sample=False)

    return use_case[0]["summary_text"], description[0]["summary_text"]
