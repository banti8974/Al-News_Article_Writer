# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import uvicorn
# from typing import Optional
# from datetime import datetime
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# from fastapi.middleware.cors import CORSMiddleware

# load_dotenv()


# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# if not GOOGLE_API_KEY:
#     raise RuntimeError("GOOGLE_API_KEY is not set. Please configure your environment variables.")
# genai.configure(api_key=GOOGLE_API_KEY)

# app = FastAPI(
#     title="News Article Generator API",
#     description="API for generating news articles from headlines using Gemini",
#     version="1.0.0"
# )


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
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
#     Make sure the article is factual and well-structured.
    
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
      
#         model = genai.GenerativeModel("gemini-pro")  


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


# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8000))  
#     uvicorn.run(app, host="0.0.0.0", port=port)











from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Optional
from datetime import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set. Please configure your environment variables.")

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize FastAPI app
app = FastAPI(
    title="News Article Generator API",
    description="API for generating news articles from headlines using Gemini",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class HeadlineRequest(BaseModel):
    headline: str
    tone: Optional[str] = "neutral"
    length: Optional[int] = 500

class ArticleResponse(BaseModel):
    headline: str
    article: str
    generated_at: str
    word_count: int

def create_prompt(headline: str, tone: str) -> str:
    tone_guidance = {
        "formal": "Write in a formal, professional tone.",
        "casual": "Write in a casual, conversational tone.",
        "neutral": "Write in a balanced, neutral tone."
    }
    
    return f"""Generate a news article based on the following headline.
    {tone_guidance.get(tone.lower(), "Write in a balanced, neutral tone.")}
    
    Headline: {headline}
    
    Please follow these guidelines:
    - Write in a journalistic style
    - Include relevant details and context
    - Maintain objectivity
    - Use clear and concise language
    - Follow proper news article structure (lead paragraph, body, conclusion)
    """

@app.post("/generate-article", response_model=ArticleResponse)
async def generate_article(request: HeadlineRequest):
    try:
        # Configure the model
        model = genai.GenerativeModel(model_name="models/text-bison-001")
        
        # Generate the prompt
        prompt = create_prompt(request.headline, request.tone)
        
        # Generate content
        response = model.generate_content(
            contents=prompt,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": request.length * 4
            }
        )
        
        # Extract and process the response
        article = response.text.strip()
        word_count = len(article.split())
        
        return ArticleResponse(
            headline=request.headline,
            article=article,
            generated_at=datetime.now().isoformat(),
            word_count=word_count
        )
        
    except Exception as e:
        print(f"Error details: {str(e)}")  # Add detailed logging
        raise HTTPException(
            status_code=500,
            detail=f"Error generating article: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model": "models/text-bison-001",
        "api_configured": bool(GOOGLE_API_KEY)
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
