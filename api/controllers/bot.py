from fastapi import APIRouter, HTTPException
from api.views.bot import Bot


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
    text: str,
    url: str,
):
    """
    Knowladge


    Parameters
    ----------
    * text : Str
        - Message sent to LLM
    * url : Str
        - Photo url.

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

