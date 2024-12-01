from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utlis import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post("")
async def run(data: ImageData):
    """
    Analyze the given image and interpret the mathematical expressions, equations, and graphical problems it contains.
    
    Parameters:
    data (ImageData): The input image and dictionary of user-assigned variables.
    
    Returns:
    A detailed analysis of the image content, including step-by-step solutions and explanations.
    """
    
    # Decode the base64 image data
    img = Image.open(BytesIO(base64.b64decode(data.image.split(",")[1])))
    
    # Analyze the image and return the results
    responses = analyze_image(img, dict_of_vars=data.dict_of_vars)
    data = []
    for response in responses:
        data.append(response)
    print(f"Response in route : {response}")
    return {
        "message": "Image proccessed successfully",
        "type": "success",
        "data": data
    }
