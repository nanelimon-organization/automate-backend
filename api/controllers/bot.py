from fastapi import APIRouter, HTTPException
from decouple import config
import requests
import base64


chat_router = APIRouter()
vision_router = APIRouter()


@chat_router.post("/chat_router", response_model=dict)
async def chat(
    text: str,
    choice: str = None,
):
    """
    Knowladge


    Parameters
    ----------
    * text : Str
        - Message sent to LLM
    * choice : Str
        - A flag indicating what type of content the message is being sent for.
        Alternative parameters it can receive: Return from Form1, Return from Form2, message response

    Returns
    -------
    * result : json
        - return LLM

    Raises
    ------
    * HTTPException
        -   If there is an error during processing.
    """
    try:
        results = ''
        return {"result": results}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error processing text: {ex}")


@vision_router.post("/vision_router", response_model=dict)
async def vision(
    question: str,
    url: str,
):
    """
    Analyzes an image from a given URL with a text query using GPT-4 Vision API.

    This endpoint encodes a publicly accessible image from a URL into base64 format and sends it 
    with the text query to the GPT-4 Vision API. Returns the processed response focusing on 
    the AI's interpretation of the image... 
    
    Parameters
    ----------
    question : str
        Description or question about the image to be analyzed.
    url : str
        URL of the publicly accessible image.

    Returns
    -------
    dict
        Extracted content from the API response, containing the AI's interpretation of the image.

    Raises
    ------
    HTTPException
        In case of any error during the request to the API.

    Example
    -------
    >>> response = await vision("Describe this photo.", "http://example.com/photo.jpg")
    >>> print(response)
    """
    try:
        api_key = config('GPT4V_API_KEY')
        gpt4v_endpoint = config('GPT4V_ENDPOINT')

        encoded_image = base64.b64encode(requests.get(url).content).decode('ascii')

        headers = {
            "Content-Type": "application/json",
            "api-key": api_key,
        }

        payload = {
          "messages": [
            {
              "role": "system",
              "content": [
                {
                  "type": "text",
                  "text": "You are an AI assistant that helps people find information."
                }
              ]
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "image_url",
                  "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                  }
                },
                {
                  "type": "text",
                  "text": question
                }
              ]
            }
          ],
          "temperature": 0.3,
          "top_p": 0.95,
          "max_tokens": 800
        }

        response = requests.post(gpt4v_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        return {"result": response_data["choices"][0]["message"]["content"]}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Error processing text: {ex}")
