from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas 


def create(db: Session, recipe):
    # Create a new instance of the Recipe model with the provided data
    # Field names used: sandwich_id, resource_id, and amount (from your models.py)
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    # Add the newly created Recipe object to the database session
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update(db: Session, recipe_id, recipe):
    # Query the database for the specific recipe to update
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    
    # Check if the recipe exists before updating
    if not db_recipe.first():
        raise HTTPException(status_code=404, detail="Recipe not found")
        
    # Extract the update data from the provided 'recipe' object
    update_data = recipe.model_dump(exclude_unset=True)
    
    # Update the database record with the new data, without synchronizing the session
    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()


def delete(db: Session, recipe_id):
    # Query the database for the specific recipe to delete
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    
    # Check if the recipe exists before deleting
    if not db_recipe.first():
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Delete the database record without synchronizing the session
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)