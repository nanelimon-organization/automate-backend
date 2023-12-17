
## AutoMate Gen-AI Backend Service

### Description
_Backend service of AutoMate Gen-AI application. Includes API endpoints for chat and vision operations._

### Environment Setup

Please set your Python version to Python 3.11.6:

```bash
python --version
```

- Installation of Virtualenv:

```bash
pip install virtualenv
```
- Creating a Virtualenv:

```bash
virtualenv venv
```
- Activating the Virtualenv:
```bash
source venv/bin/activate
```
- Installing libraries:
```bash
pip install -r requirements.txt
```
- Define Environment Variables.

```
# GPT 4 Vision API
GPT4V_API_KEY=cok_gizli_bisi
GPT4V_ENDPOINT=cok_gizli_bisi

# QDRANT API
QDRANT_URL=cok_gizli_bisi
QDRANT_API_KEY=cok_gizli_bisi

# Azure OpenAI API for GPT-4-8k model
AZURE_OPENAI_ENDPOINT=cok_gizli_bisi
AZURE_OPENAI_API_KEY=cok_gizli_bisi
DEPLOYMENT_NAME_LLM=cok_gizli_bisi

# Azure OpenAI API for embedding model - text-embedding-ada-002
AZURE_OPENAI_EMBD_API_KEY=cok_gizli_bisi
AZURE_OPENAI_EMBD_ENDPOINT=cok_gizli_bisi
```

## Running the Application

```python
python main.py
```

--- 

