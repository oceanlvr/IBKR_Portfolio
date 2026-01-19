from datetime import date
from typing import Optional
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Account(Base):
    # Account table
    __tablename__ = "ibkr_accounts"

    account_id: Mapped[str] = mapped_column(String, primary_key=True)
    account_alias: Mapped[Optional[str]] = mapped_column(String)
    currency: Mapped[Optional[str]] = mapped_column(String)
    name: Mapped[Optional[str]] = mapped_column(String)
    last_traded_date: Mapped[Optional[date]] = mapped_column(Date)
    status: Mapped[Optional[str]] = mapped_column(String)
    created_at: Mapped[Optional[date]] = mapped_column(Date)
