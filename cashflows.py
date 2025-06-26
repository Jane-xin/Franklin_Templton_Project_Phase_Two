from typing import Optional
from pydantic import BaseModel, Field
year = 2024

class StatementOfCashFlows2024(BaseModel):
    """
    Statement of Cash Flows for the fiscal year {year}.
    Only extract data from the {year} fiscal period (e.g. statements labeled ‘Fiscal Year {year}').
    Ignore any figures outside this period. Do not extract anything from {year-1}.
    Do not extract anything from the condensed or summary table or statement. Only from the long, fully elaborated statement or table.
    Do not derive or calculate values unless they appear explicitly in the document.
    Extract the number as it is. Don't convert its unit.
    """
    total_change_in_net_assets: Optional[float] = Field(
        description=(
            f"Cash amount labeled 'Total Change in Net Assets' for the {year} fiscal year, in US dollars. "
            "Only extract the exact figure for that period."
        )
    )
    total_non_cash_exp: Optional[float] = Field(
        description=(
            f"Aggregate non-cash expenses (e.g., depreciation, amortization) labeled 'Total Non-Cash Exp' for the {year} fiscal year, in US dollars. "
            "Only extract from that statement."
        )
    )
    change_in_working_capital: Optional[float] = Field(
        description=(
            f"Line item 'Change in Working Capital' for the {year} fiscal year, in US dollars. "
            "Extract only the value for that period."
        )
    )
    other_changes_in_operating_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Operating Activities' for the {year} fiscal year, in US dollars. "
            "Ignore any amounts outside that period."
        )
    )
    net_cash_from_operating_activities: Optional[float] = Field(
        description=(
            f"Net cash from operating activities labeled 'Net Cash from Operating Activities' for the {year} fiscal year, in US dollars. "
            "Only use the figure for that period."
        )
    )
    capital_expenses: Optional[float] = Field(
        description=(
            f"Cash outflow for capital expenditures labeled 'Capital Expenses' in the {year} fiscal year, in US dollars. "
            "Extract the exact amount for that period."
        )
    )
    other_changes_in_investment_activities: Optional[float] = Field(
        description=(
            f"Line item 'Other Changes in Investment Activities' for the {year} fiscal year, in US dollars. "
            "Ignore entries outside that period."
        )
    )
    net_cash_from_investment_activities: Optional[float] = Field(
        description=(
            f"Net cash from investing activities labeled 'Net Cash from Investment Activities' for the {year} fiscal year, in US dollars. "
            "Use only the figure for that period."
        )
    )
    long_term_debt_net_proceeds: Optional[float] = Field(
        description=(
            f"Proceeds from long-term debt issuance labeled 'Long-Term Debt Net Proceeds' for the {year} fiscal year, in US dollars. "
            "Extract only that period's value."
        )
    )
    long_term_debt_principal_payments: Optional[float] = Field(
        description=(
            f"Repayments of long-term debt principal labeled 'Long-Term Debt Principal Payments' for the {year} fiscal year, in US dollars. "
            "Ignore payments from other periods."
        )
    )
    change_in_long_term_debt: Optional[float] = Field(
        description=(
            f"Net change labeled 'Change in Long-Term Debt' for the {year} fiscal year, in US dollars. "
            "Only extract the figure for that period."
        )
    )
    other_changes_in_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Financing Activities' for the {year} fiscal year, in US dollars. "
            "Only use that period's entry."
        )
    )
    cash_flows_from_noncapital_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Cash flows from noncapital financing activities' for the {year} fiscal year, in US dollars. "
            "Only use that period's entry."
        )
    )

    cash_flows_from_capital_and_related_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Cash flows from capital and related financing activities' for the {year} fiscal year, in US dollars. "
            "Only use that period's entry."
        )
    )
    net_cash_from_financing_activities: Optional[float] = Field(
        description=(
            f"Net cash from financing activities labeled 'Net Cash from Financing Activities' for the {year} fiscal year, in US dollars. "
            "If the both fields 'cash_flows_from_noncapital_financing_activities' and 'cash_flows_from_capital_and_related_financing_activities' are populated, this field should be the combination of these fields."
            "Extract exclusively that period's figure."
        )
    )
    change_in_cash_and_equivalents: Optional[float] = Field(
        description=(
            f"Overall 'Change in Cash & Equivalents' or 'Net change in cash and cash equivalents' for the {year} fiscal year, in US dollars. "
            "Ignore any data from other periods."
        )
    )


