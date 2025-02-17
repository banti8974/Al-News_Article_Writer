# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import uvicorn
# from typing import Optional
# from datetime import datetime
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv


# load_dotenv()


# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))



# app = FastAPI(
#     title="News Article Generator API",
#     description="API for generating news articles from headlines using Gemini",
#     version="1.0.0"
# )

# class HeadlineRequest(BaseModel):
#     headline: str
#     tone: Optional[str] = "neutral"
#     length: Optional[int] = 500

# class ArticleResponse(BaseModel):
#     headline: str
#     article: str
#     generated_at: str
#     word_count: int

# def create_prompt(headline: str) -> str:
#     return f"""Generate a news article based on the following headline. 
#     Make sure the article is factual, well-structured.
    
#     Headline: {headline}
    
#     Please follow these guidelines:
#     - Write in a journalistic style
#     - Include relevant details and context
#     - Maintain objectivity
#     - Use clear and concise language
#     - Follow proper news article structure (lead paragraph, body, conclusion)
#     """

# @app.post("/generate-article", response_model=ArticleResponse)
# async def generate_article(request: HeadlineRequest):
#     try:
   
#         model = genai.GenerativeModel("tunedModels/new-model-uxen6rexyhu7")
        
     
#         prompt = create_prompt(request.headline)
        

#         response = model.generate_content(
#             prompt,
#             generation_config={
#                 'temperature': 0.7,
#                 'top_p': 0.8,
#                 'top_k': 40,
#                 'max_output_tokens': request.length * 4  
#             }
#         )
        
        
#         article = response.text.strip()
       
        
       
#         word_count = len(article.split())
        
#         return ArticleResponse(
#             headline=request.headline,
#             article=article,
#             generated_at=datetime.now().isoformat(),
#             word_count=word_count
#         )
#     except Exception as e:
       
#         raise HTTPException(
#             status_code=500,
#             detail=f"Error generating article: {str(e)}"
#         )


# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "model": "gemini-pro"}










from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Optional
from datetime import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

# Configure Google Generative AI API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set. Please configure your environment variables.")
genai.configure(api_key=GOOGLE_API_KEY)

# FastAPI app initialization
app = FastAPI(
    title="News Article Generator API",
    description="API for generating news articles from headlines using Gemini",
    version="1.0.0"
)

# Request model
class HeadlineRequest(BaseModel):
    headline: str
    tone: Optional[str] = "neutral"
    length: Optional[int] = 500

# Response model
class ArticleResponse(BaseModel):
    headline: str
    article: str
    generated_at: str
    word_count: int

# Function to create the article prompt
def create_prompt(headline: str) -> str:
    return f"""Generate a news article based on the following headline. 
    Make sure the article is factual and well-structured.
    
    Headline: {headline}
    
    Please follow these guidelines:
    - Write in a journalistic style
    - Include relevant details and context
    - Maintain objectivity
    - Use clear and concise language
    - Follow proper news article structure (lead paragraph, body, conclusion)
    """

# API endpoint to generate the article
@app.post("/generate-article", response_model=ArticleResponse)
async def generate_article(request: HeadlineRequest):
    try:
        # Load the generative AI model
        model = genai.GenerativeModel("gemini-pro")  # Ensure the model name is correct

        # Create prompt
        prompt = create_prompt(request.headline)

        # Generate response
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.7,
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': request.length * 4  
            }
        )
        
        # Extract generated article
        article = response.text.strip()
        word_count = len(article.split())

        return ArticleResponse(
            headline=request.headline,
            article=article,
            generated_at=datetime.now().isoformat(),
            word_count=word_count
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating article: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "gemini-pro"}

# Ensure correct port binding for deployment
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Defaults to 8000 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)
