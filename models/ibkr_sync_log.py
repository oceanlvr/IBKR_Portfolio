from datetime import date
from typing import Optional
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class IBKRSyncLog(Base):
    __tablename__ = "ibkr_sync_logs"

    reference_code: Mapped[str] = mapped_column(String, primary_key=True)
    query_id: Mapped[Optional[str]] = mapped_column(String)
    status: Mapped[Optional[str]] = mapped_column(String)
    created_at: Mapped[Optional[date]] = mapped_column(Date)
