from datetime import date
from typing import Optional
from sqlalchemy import BigInteger, Numeric, String, Date, Index
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Position(Base):
    __tablename__ = "ibkr_positions"

    # --- 身份识别 (Identification) ---
    # 使用复合主键：同一份合约在不同日期的持仓是唯一的记录
    conid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    reportDate: Mapped[date] = mapped_column(Date, primary_key=True)

    symbol: Mapped[str] = mapped_column(String(16), index=True)
    isin: Mapped[Optional[str]] = mapped_column(String(12), index=True)

    # --- 核心数据 (Core Data) ---
    # 金额和价格建议使用 Numeric/Decimal 以确保财务精度，避免 Float 的舍入误差
    position: Mapped[float] = mapped_column(Numeric(18, 4))
    markPrice: Mapped[float] = mapped_column(Numeric(18, 6))
    positionValue: Mapped[float] = mapped_column(Numeric(18, 2))
    openPrice: Mapped[float] = mapped_column(Numeric(18, 6))
    costBasisPrice: Mapped[float] = mapped_column(Numeric(18, 6))
    costBasisMoney: Mapped[float] = mapped_column(Numeric(18, 2))
    fifoPnlUnrealized: Mapped[float] = mapped_column(Numeric(18, 2))
    percentOfNAV: Mapped[float] = mapped_column(Numeric(8, 4))

    # --- 资产属性 (Asset Attributes) ---
    assetCategory: Mapped[str] = mapped_column(String(10))
    subCategory: Mapped[Optional[str]] = mapped_column(String(20))
    listingExchange: Mapped[Optional[str]] = mapped_column(String(10))
    currency: Mapped[str] = mapped_column(String(3))
    fxRateToBase: Mapped[float] = mapped_column(Numeric(18, 8), default=1.0)

    # 显式建立复合索引，优化基于日期的查询性能
    __table_args__ = (Index("ix_symbol_report_date", "symbol", "reportDate"),)

    def __repr__(self) -> str:
        # 便于调试和日志记录
        return f"Position(symbol={self.symbol!r}, qty={self.position}, date={self.reportDate})"
