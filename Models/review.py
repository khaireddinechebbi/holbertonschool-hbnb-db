import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models.base_model import BaseModel, Base
from app import db
class Review(BaseModel, Base, db.Model):
    """
    Review class representing a review for a place

    Attributes:
        user_id (str): The ID of the user who wrote the review.
        place_id (str): The ID of the place being reviewed.
        text (str): The text content of the review.
        rating (int): The rating given in the review.
    """
    __tablename__ = 'reviews'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(60), db.ForeignKey('places.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


    def __init__(self, user_id, place_id, text, rating):
        """
        Initialize a new Review instance

        Args:
            user_id (str): The ID of the user who wrote the review.
            place_id (str): The ID of the place being reviewed.
            text (str): The text content of the review.
            rating (int): The rating given in the review.
        """
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
    
    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        review_dict = super().to_dict()
        review_dict.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'rating': self.rating,
        })
        return review_dict
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=db.engine)
