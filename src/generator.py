"""
Persona Generator Module
"""

from config import DEMOGRAPHIC_GENERATOR_LLM, PERSONA_GENERATOR_LLM
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from src.models import get_model

class DemographicParserOutput(BaseModel):
    """
    Output given by the demographic parsing model.
    """
    
    minage: float = Field(..., description="Minimum age of the target demographic, if any.")
    maxage: float = Field(..., description="Maximum age of the target demographic, if any.")
    gender: str = Field(..., description="Preferred gender of the target demographic, if any.")
    religion: str = Field(..., description="Preferred religion of the target demographic, if any.")
    occupations: list[str] = Field(..., description="Preferred occupations of the target demographic, if any.")
    lifestyle: str = Field(..., description="Lifestyle of the target demographic, if any.")
    interests: list[str] = Field(..., description="Interests of the target demographic, if any.")

def parse_demographic(product_description: str, target_demographic: str) -> DemographicParserOutput:
    model = get_model(key=DEMOGRAPHIC_GENERATOR_LLM)
    prompt = PromptTemplate(
        template="""
You are an expert market research analyst specializing in data extraction and demographic parsing.
Your task is to analyze the provided product description and target demographic text, then structure the key demographic attributes into a single, clean JSON object.

**CONTEXT**
Product Description: {product_description}
Target Demographic: {target_demographic}

**INSTRUCTIONS**
Based on the context above, extract the required information. Infer logical details where necessary. For example, if the demographic is "university students," infer an age range of 18-22 and the occupation "Student". If the product is for "hardcore gamers," infer interests like "esports, technology, streaming".

**RULES**
1. Your output MUST be ONLY the valid JSON object. Do not include any explanatory text before or after the JSON.
2. If a specific piece of information cannot be found or inferred from the text (e.g., religion), use `null` as the value.

**OUTPUT**
""",
        input_variables=["product_description", "target_demographic"],
    )
    
    return model.langchain_model.with_structured_output(DemographicParserOutput).invoke(prompt.format(
        product_description=product_description,
        target_demographic=target_demographic
    ))
    
class PersonaGeneratorOutput(BaseModel):
    name: str = Field(..., description="Name of the person.")
    age: str = Field(..., description="Age of the person")
    job: str = Field(..., description="Job of the person.")
    location: str = Field(..., description="Location of the person.")
    education: str = Field(..., description="Education of the person.")
    background: str = Field(..., description="A short paragraph that tells their story. Where did they come from? What is their current life situation? This provides crucial context for their motivations.")
    personality: list[str] = Field(..., description="A list of 3-5 descriptive adjectives that define their character. (e.g., 'Creative', 'Tech-Savvy', 'Introverted', 'Detail-Oriented').")
    goals: list[str] = Field(..., description="""List of what this person is actively trying to achieve? These should be relevant to the product. (e.g., "Grow their client base by 20%," "Achieve a better work-life balance," "Save enough for a down payment on an apartment").""")
    frustrations: list[str] = Field(..., description="""List of the specific daily obstacles and annoyances they face. These should be related to the product. (e.g., "Managing multiple projects with different billing cycles," "Feeling overwhelmed by tax compliance," "Struggling to separate business and personal expenses").""")

def generate_persona(product_description: str, parsed_demographic: DemographicParserOutput) -> PersonaGeneratorOutput:
    model = get_model(key=PERSONA_GENERATOR_LLM)
    prompt = PromptTemplate(
        template="""
You are a senior market research analyst and expert storyteller. Your task is to create a single, detailed, realistic, and empathetic user persona based on the provided product description and target audience.

**CONTEXT**
- **Product Description:** {product_description}
- **Target Demographic:** {target_demographic}

**INSTRUCTIONS**
Generate a persona that plausibly lives and works in or around **Noida, Uttar Pradesh, India**. Your entire response must be a single, valid JSON object that adheres strictly to the schema below. Do not include any text, explanations, or markdown formatting before or after the JSON.
""",
        input_variables=["product_description", "target_demographic"],
    )
    
    return model.langchain_model.with_structured_output(PersonaGeneratorOutput).invoke(prompt.format(
        product_description=product_description,
        target_demographic=parsed_demographic
    ))

if __name__ == "__main__":
    product_description = "FlexiFlow is an all-in-one financial management app designed specifically for the modern freelancer and gig economy worker. Our platform automates invoicing, tracks business expenses in real-time, and provides clear quarterly tax estimations to eliminate financial surprises. We also offer integrated tools for setting up and contributing to retirement funds like a SEP IRA, helping independent professionals build long-term wealth with an unstable income."
    target_demographic = "Our core audience consists of freelancers, solopreneurs, and independent contractors in creative and tech fields, such as graphic designers, freelance developers, and digital marketing consultants. They are typically between 25 and 40 years old. This group is tech-savvy, values personal freedom and flexibility, and often works remotely from major urban centers. They struggle with the unpredictability of fluctuating income streams and find the complexities of self-employment taxes and retirement planning overwhelming."
    parsed_demographic = parse_demographic(target_demographic, target_demographic)
    generated_persona = generate_persona(product_description, parsed_demographic)
    
    print("\n" + "=" * 50 + "\n" + "Product Description" + "\n" + "=" * 50 + "\n", product_description)
    print("\n" + "=" * 50 + "\n" + "Target Demographic" + "\n" + "=" * 50 + "\n", target_demographic)
    print("\n" + "=" * 50 + "\n" + "Parsed Demographic" + "\n" + "=" * 50 + "\n", parsed_demographic)
    print("\n" + "=" * 50 + "\n" + "Generated Persona" + "\n" + "=" * 50 + "\n", generated_persona)
