import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # "task", "note", "deadline", "study_material", "practice_question"
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)  # Body/description/study text/file path
    status = Column(String, default="todo")   # "todo", "in_progress", "done", "weak", "mastered"
    priority = Column(String, nullable=True)  # "high", "medium", "low"
    due_date = Column(DateTime, nullable=True)
    metadata_json = Column(JSON, default=dict) # For storing explainability traces, AI annotations, test metrics, etc.
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Connection(Base):
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    target_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    connection_type = Column(String, nullable=False) # "converted_from", "relates_to", "practice_of", "weakness_of"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    source = relationship("Item", foreign_keys=[source_id], backref="outgoing_connections")
    target = relationship("Item", foreign_keys=[target_id], backref="incoming_connections")

class StudyReview(Base):
    __tablename__ = "study_reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    concept_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    interval_days = Column(Integer, default=1)  # 1 -> 3 -> 7 -> 14 -> 30 days
    due_date = Column(DateTime, nullable=False)
    last_reviewed_at = Column(DateTime, nullable=True)
    status = Column(String, default="learning")  # "learning", "learned"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship
    concept = relationship("Item", foreign_keys=[concept_id], backref="study_reviews")
    user = relationship("User", foreign_keys=[user_id], backref="study_reviews")

class UserIntegration(Base):
    __tablename__ = "user_integrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)  # "google_calendar"
    is_connected = Column(Boolean, default=False)
    scopes = Column(JSON, default=list)
    credentials_encrypted = Column(String, nullable=True)
    metadata_json = Column(JSON, default=dict)
    health_status = Column(String, default="healthy")  # "healthy", "broken"
    error_message = Column(String, nullable=True)
    last_sync_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationship
    user = relationship("User", backref="integrations")


