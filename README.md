# AI News Article Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://4add4csappvnxszctodwnhz.streamlit.app/)

## Quick Links
- 🌐 **Live Demo**: [Streamlit Frontend](https://4add4csappvnxszctodwnhz.streamlit.app/)
- 🚀 **API Endpoint**: [Backend API](https://al-news-article-writer.onrender.com/health)
- 📂 **GitHub Repository**: [GitHub](https://github.com/s11saurabh/Al-News_Article_Writer)
- 🎥 **Demo Video**: [Watch Demo](https://drive)

## Overview

An advanced AI-powered news article generator that leverages multiple machine learning frameworks and libraries to create high-quality, contextually relevant news articles from headlines. The system combines the power of Hugging Face's transformers, LangChain, and various NLP tools to deliver sophisticated article generation capabilities.


<img width="1228" alt="image" src="https://github.com/user-attachments/assets/cdf6165d-834b-4c34-8668-08f1bc06e06c" />
<img width="1210" alt="image" src="https://github.com/user-attachments/assets/ed8eae1e-dedb-40ff-9ccf-fcc0b0216eb4" />
<img width="1225" alt="image" src="https://github.com/user-attachments/assets/52fe7068-8f91-4625-a6fe-eeb3ec4f4658" />
<img width="1229" alt="image" src="https://github.com/user-attachments/assets/4e57b8c3-a1c4-4d71-a570-88f6044dc1df" />




## Features
- 🎯 Headline to Article Generation
- 🎨 Customizable Tone & Style
- ⚡ Real-time Processing
- 📊 Article Analytics
- 💾 Export Functionality
- 🔄 History Tracking

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Model Training](#model-training)
- [API Documentation](#api-documentation)
- [Frontend Details](#frontend-details)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)

## Deployment Information

The project is deployed across multiple platforms for optimal performance and accessibility:

### Frontend (Streamlit Cloud)
- **URL**: [https://4add4csappvnxszctodwnhz.streamlit.app/](https://4add4csappvnxszctodwnhz.streamlit.app/)
- **Platform**: Streamlit Cloud
- **Features**:
  - Interactive UI
  - Real-time Processing
  - Responsive Design
  - Custom Styling

### Backend (Render)
- **URL**: [https://al-news-article-writer.onrender.com/health](https://al-news-article-writer.onrender.com/health)
- **Platform**: Render
- **Features**:
  - RESTful API
  - Swagger Documentation
  - Health Monitoring
  - Scalable Infrastructure

## Technology Stack

### Backend Technologies
1. **FastAPI Framework**
   - High-performance asynchronous framework for building APIs
   - Built-in data validation and OpenAPI documentation
   - WebSocket support for real-time communications
   - Dependency injection system for clean architecture
   - Automatic API documentation with Swagger UI

2. **Natural Language Processing Libraries**
   - **Hugging Face Transformers**: Pre-trained models and fine-tuning capabilities
   - **LangChain**: Framework for developing applications powered by language models
   - **spaCy**: Industrial-strength NLP for text processing
   - **NLTK**: Comprehensive suite of text processing libraries

3. **Machine Learning Frameworks**
   - **TensorFlow**: End-to-end ML platform for model training
   - **PyTorch**: Dynamic neural networks and deep learning
   - **OpenAI API**: Integration for advanced language models

4. **Data Validation & Environment Management**
   - **Pydantic**: Data validation using Python type annotations
     - Request/Response model validation
     - Configuration management
     - Environment variable validation
     - Complex data schemas
   
   - **Python-dotenv**: Environment variable management
     - Secure credential storage
     - Configuration separation
     - Development/production environment handling
     - API key management

5. **Python 3.13**
   - Latest language features and optimizations
   - Improved type hinting
   - Enhanced asyncio support
   - Performance improvements

### Frontend Technologies
1. **Streamlit Framework**
   - Interactive web application development
   - Real-time data visualization
   - Session state management for user data persistence
   - Component caching for performance
   - Custom theming and styling capabilities

2. **User Interface Components**
   - Custom CSS styling for modern design
   - Responsive layout management
   - Interactive widgets and forms
   - Real-time updates and notifications
   - Data visualization components

3. **State Management**
   - Session state for user preferences
   - Caching mechanisms for performance
   - Data persistence between reruns
   - Component lifecycle management

4. **Interactive Features**
   - Real-time article generation
   - Dynamic parameter adjustment
   - Progress tracking and status updates
   - Error handling and user feedback
   - Export functionality for generated content

### Model & Training Infrastructure

1. **Model Architecture**
   - **Base Model**: Google Gemini Pro
   - **Fine-tuning Framework**: Hugging Face Transformers
   - **Training Infrastructure**: Google Colab Pro
   - **Model Optimization**: Mixed precision training

2. **Training Pipeline**
   - Data preprocessing and cleaning
   - Token optimization
   - Model checkpointing
   - Evaluation metrics tracking
   - Hyperparameter optimization

3. **Datasets and Resources**
   - **Primary Sources**:
     - Kaggle news article datasets
     - Hugging Face Hub datasets
     - UCI ML Repository
   - **Data Processing**:
     - Text cleaning and normalization
     - Feature extraction
     - Dataset balancing
     - Validation split strategies

4. **Training Process**
   - **Environment**: Google Colab with GPU acceleration
   - **Optimization**: Learning rate scheduling
   - **Validation**: Cross-validation techniques
   - **Metrics**: ROUGE, BLEU, and custom metrics
   - **Testing**: Comprehensive test suite

## Project Structure

```
project_root/
├── backend/
│   ├── __pycache__/
│   ├── main.cpython-313.pyc
│   ├── .env
│   └── main.py
├── frontend/
│   └── app.py
├── venv/
│   ├── bin/
│   ├── etc/
│   │   └── jupyter/nbconfig/notebook.d/
│   │       └── pydeck.json
│   ├── include/
│   │   └── python3.13/
│   ├── lib/
│   └── share/
│       ├── jupyter/nbextensions/pydeck/
│       └── man/man1/
├── .gitignore
├── pyenv.cfg
└── requirements.txt
```

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/s11saurabh/Al-News_Article_Writer.git
cd Al-News_Article_Writer
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install additional NLP dependencies:
```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader all
```

5. Set up environment variables:
Create a `.env` file in the backend directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

6. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

7. Start the frontend (in a new terminal):
```bash
cd frontend
streamlit run app.py
```

## Model Training Details

### Data Preparation
1. **Dataset Collection**
   - Gathered news articles from Kaggle
   - Filtered and cleaned data
   - Created headline-article pairs
   - Implemented data augmentation techniques

2. **Preprocessing Pipeline**
   - Text normalization
   - Tokenization
   - Feature extraction
   - Data splitting (train/validation/test)

### Training Process
1. **Environment Setup**
   - Google Colab Pro with GPU acceleration
   - Required library installation
   - Data mounting and preprocessing

2. **Model Configuration**
   - Base model selection (Gemini Pro)
   - Hyperparameter optimization
   - Training strategy definition
   - Evaluation metric selection

3. **Training Execution**
   - Batch processing
   - Learning rate scheduling
   - Gradient accumulation
   - Model checkpointing

4. **Evaluation and Refinement**
   - Performance metrics tracking
   - Error analysis
   - Model iteration
   - Final model selection

## Author

**Saurabh Kumar**
Indian Institute of Information Technology, Bhagalpur

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
