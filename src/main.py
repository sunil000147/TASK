import pandas as pd
from src.research_agent import research_industry
from src.use_case_agent import generate_use_case_and_description

def main():
    # List of companies and industries
    companies = [
        ("Tesla", "Automotive"),
        ("Nvidia", "Technology"),
        ("OpenAI", "AI Research"),
        ("Microsoft", "Software"),
        ("Apple", "Consumer Electronics"),
        ("Amazon", "E-commerce"),
        ("Google", "Technology"),
        ("Meta", "Social Media"),
        ("IBM", "Technology"),
        ("Intel", "Semiconductors"),
    ]

    all_data = []

    # Process each company
    for company_name, industry_name in companies:
        print(f"\nResearching {company_name}...")

        # Research Industry
        industry_info = research_industry(company_name, industry_name)

        if isinstance(industry_info, dict) and "error" in industry_info:
            print(f"Error: {industry_info['error']}")
            continue

        # Generate Use Cases and Descriptions
        for idx, item in enumerate(industry_info):
            use_case, description = generate_use_case_and_description(company_name, item["snippet"])
            all_data.append({
                "Company": company_name,
                "Research Link": item["link"],
                "Use Case": use_case,
                "Description": description,
            })

    # Save results to CSV
    df = pd.DataFrame(all_data)
    output_file = "company_use_cases.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"\nResults saved as '{output_file}'")

if __name__ == "__main__":
    main()
