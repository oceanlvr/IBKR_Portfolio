from datetime import date
from typing import Optional
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Cash(Base):
    __tablename__ = "ibkr_cash"

    # account metadata
    account_id: Mapped[str] = mapped_column(String, primary_key=True)
    acctAlias: Mapped[Optional[str]] = mapped_column(String)
    currency: Mapped[Optional[str]] = mapped_column(String)
    levelOfDetail: Mapped[Optional[str]] = mapped_column(String)
    fromDate: Mapped[Optional[date]] = mapped_column(Date)
    toDate: Mapped[Optional[date]] = mapped_column(Date)

    # cash activities
    startingCash: Mapped[Optional[float]] = mapped_column()
    depositWithdrawals: Mapped[Optional[float]] = mapped_column()

    # trade related
    netTradesSales: Mapped[Optional[float]] = mapped_column()
    netTradesPurchases: Mapped[Optional[float]] = mapped_column()
    dividends: Mapped[Optional[float]] = mapped_column()
    paymentInLieu: Mapped[Optional[float]] = mapped_column()  # 借券收益替代支出

    # costs and interests
    brokerFees: Mapped[Optional[float]] = mapped_column()
    transactionTax: Mapped[Optional[float]] = mapped_column()
    withholdingTax: Mapped[Optional[float]] = mapped_column()
    withholding871m: Mapped[Optional[float]] = mapped_column()
    brokerInterest: Mapped[Optional[float]] = mapped_column()
    insuredDepositInterest: Mapped[Optional[float]] = mapped_column()

    # translation and ending cash
    fxTranslationGainLoss: Mapped[Optional[float]] = mapped_column()
    endingCash: Mapped[Optional[float]] = mapped_column()
    endingSettledCash: Mapped[Optional[float]] = mapped_column()

    # other
    other: Mapped[Optional[float]] = mapped_column()
