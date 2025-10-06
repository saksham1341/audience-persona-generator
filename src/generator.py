"""
Persona Generator Module
"""

from config import DEMOGRAPHIC_GENERATOR_LLM
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from src.models import get_model
from src.persona import Persona


class DemographicParserInput(BaseModel):
    """
    Input given to the demographic parsing model.
    """
    
    product_description: str = Field(..., description="Description of the product.")
    target_demographic: str = Field(..., description="Description of the target demographic of the product.")

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

def parse_demographic(inp: DemographicParserInput) -> DemographicParserOutput:
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
        product_description=inp.product_description,
        target_demographic=inp.target_demographic
    ))

if __name__ == "__main__":
    inp = DemographicParserInput(
        product_description="FlexiFlow is an all-in-one financial management app designed specifically for the modern freelancer and gig economy worker. Our platform automates invoicing, tracks business expenses in real-time, and provides clear quarterly tax estimations to eliminate financial surprises. We also offer integrated tools for setting up and contributing to retirement funds like a SEP IRA, helping independent professionals build long-term wealth with an unstable income.",
        target_demographic="Our core audience consists of freelancers, solopreneurs, and independent contractors in creative and tech fields, such as graphic designers, freelance developers, and digital marketing consultants. They are typically between 25 and 40 years old. This group is tech-savvy, values personal freedom and flexibility, and often works remotely from major urban centers. They struggle with the unpredictability of fluctuating income streams and find the complexities of self-employment taxes and retirement planning overwhelming."
    )
    
    print(parse_demographic(inp))
