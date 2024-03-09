from fastapi import APIRouter, Depends, HTTPException, status
from models.todos import Todo
from models.user import User, UpdateUser
from config.database import user_collection, collection_name
from schema.schemas import list_serial
from bson import ObjectId
import bcrypt
from transformers import pipeline
from fastapi import File, UploadFile
import shutil
import os
from typing import List, Dict
from ..models.serapi_scraping import extract_search_results,indiamart_scraper,ebay_scraper,flipkart_scraper
UPLOAD_DIR = "profile_photos"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)
router = APIRouter()
# model = pipeline("sentiment-analysis")

# Authentication function
async def authenticate_user(username: str, password: str):
    user_data = user_collection.find_one({"username": username})
    if user_data:
        hashed_password = user_data.get("password", "")
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
    return False

# Error handling
def get_current_user(user: User = Depends(authenticate_user)):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return user

# # sentiment analysis HuggingFace Model
# @router.post("/analyze_sentiment")
# async def analyze_sentiment(text: str):
    # Run inference
    result = model(text)
    
    # Process output
    sentiment = result[0]['label']
    
    # Return response
    return {"sentiment": sentiment}

# Signup route
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = user.dict()
    user_data['password'] = hashed_password
    user_collection.insert_one(user_data)
    return {"message": "User created successfully"}

# Login route
@router.post("/login")
async def login(user: User):
    if await authenticate_user(user.username, user.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

# Update user endpoint
@router.put("/user/{user_id}")
async def update_user(user_id: str, updated_user: UpdateUser, current_user: User = Depends(get_current_user)):
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user.dict()})
    if result.modified_count == 1:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# Delete user endpoint
@router.delete("/user/{user_id}")
async def delete_user(user_id: str, current_user: User = Depends(get_current_user)):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/scrape/")
async def scrape_data(query: str, platform: str):
    if platform not in ["flipkart", "ebay", "indiamart"]:
        raise HTTPException(status_code=400, detail="Invalid platform")

    try:
        flipkart_links, ebay_links, indiamart_links = extract_search_results(query, platform)
        scraped_data = []
        
        if platform == "flipkart":
            for link in flipkart_links:
                product_data = flipkart_scraper(link)
                scraped_data.append(product_data)
        elif platform == "ebay":
            for link in ebay_links:
                product_data = ebay_scraper(link)
                scraped_data.append(product_data)
        elif platform == "indiamart":
            for link in indiamart_links:
                product_data = indiamart_scraper(link)
                scraped_data.append(product_data)
        
        return {"data": scraped_data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/search_users/{username}")
async def search_users(username: str):
    users = user_collection.find({"username": {"$regex": username, "$options": "i"}})
    if users:
        # Convert ObjectId to string for serialization
        users = [user | {"_id": str(user["_id"])} for user in users]
        return users
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found with the provided username")
    

@router.post("/upload_profile_photo/{user_id}")
async def upload_profile_photo(user_id: str, file: UploadFile = File(...)):
    # Generate a unique filename for the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save the uploaded file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Update the user record in the database with the file path of the uploaded photo
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"profile_photo": file_path}})
    
    # Check if the user record was updated successfully
    if result.modified_count == 1:
        return {"message": "Profile photo uploaded successfully"}
    else:
        # If the user record was not updated, delete the uploaded file
        os.remove(file_path)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
# Todo endpoints
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

@router.post("/")
async def post_todo(todo:Todo):
    collection_name.insert_one(dict(todo))
    
@router.put("/{id}")
async def put_todo(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
