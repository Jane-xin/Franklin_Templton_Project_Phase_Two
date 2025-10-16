from typing import Optional
from pydantic import BaseModel, Field # type: ignore

year = 2024

class StatementOfCashFlows2024(BaseModel):
    """
    Statement of Cash Flows for the fiscal year {year}.
    Only extract data from the {year} fiscal period (e.g. statements labeled ‘Fiscal Year {year}').
    Ignore any figures outside this period. Do not extract anything from {year-1}.
     **Only extract values from the cash flow statement or table corresponding to the current year. Do not extract from the financial statement notes or other financial sections. Do not use unrelated financial statements (e.g., income statement, balance sheet, or footnotes).**
    Do not extract anything from the condensed or summary table or statement. Only from the long, fully elaborated statement or table.
    Do not derive or calculate values unless they appear explicitly in the document.
    Extract the number as it is. Don't convert its unit.
    Note: In financial tables, values shown in parentheses (e.g., (3,705)) represent negative numbers or cash outflows.
    """
    total_change_in_net_assets: Optional[float] = Field(
        description=(
            f"Extract the line labeled 'Change in net assets' or 'Total Change in Net Assets' "
            f"from the Statement of Cash Flows for fiscal year {year}. "
            "This amount is typically the first line in the operating activities section, "
            "shown before adjustments to reconcile to net cash from operating activities. "
            "Only extract this figure from the cash flow statement or detailed cash flow table "
            "for the current year, not from the statement of activities, balance sheet, footnotes, "
            "or prior years. "
            "Pay attention to the sign: values in parentheses represent negative numbers. "
            "Extract the number in its original form, without modifying its unit or sign."
        )
    )
    total_non_cash_exp: Optional[int] = Field(
        description=(
            f"Depreciation and amortization expenses without donor restrictions for {year}. "
            "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
            "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
            "EXTRACTION PRIORITY: "
            "1. If 'Statement of Functional Expenses' exists in the PDF, extract 'Depreciation and Amortization', 'Depreciation', 'Amortization', or 'Depreciation Expense' from the total/bottom line of that statement. "
            "2. If no 'Statement of Functional Expenses' exists, search notes after financial statements for functional expense breakdown TABLES "
            "   and extract 'Depreciation and Amortization', 'Depreciation', 'Amortization', or 'Depreciation Expense' from the total line. "
            "3. If neither of the above apply, extract 'Depreciation and Amortization', 'Depreciation', 'Amortization', or 'Depreciation Expense' from the operating expenses section of the 'Statement of Activities'. "
            # "Look for labels including: 'Depreciation and Amortization', 'Depreciation', 'Amortization', 'Depreciation Expense'. "
            "This represents non-cash expenses for the allocation of asset costs over their useful lives. "
            "Extract the raw numeric value only — ignore formatting symbols such as commas, dollar signs, or footnote markers."
        )
    )

    change_in_working_capital: Optional[float] = Field(
        description=(
            f"Extract the change in working capital for fiscal year {year} from the cash flow statement. "
            "This value represents the combined effect of changes in assets and liabilities within the operating activities section. "
            "Follow this order of priority: "
            "1. If the cash flow statement contains a subsection labeled 'Change in Assets and Liabilities', "
            "   'Effect of Changes in Operating Assets and Liabilities', 'Changes in Operating Assets and Liabilities', "
            "   or similar wording, extract all line items indented beneath this subsection and add these line items together. "
            "2. If no such indented subsection exists, calculate the change in working capital by summing all individual line items "
            "   within operating activities that represent changes in current assets and current liabilities. "
            "   Typical line items include: accounts receivable, student receivables, contributions or grants receivable, "
            "   other receivables, prepaid expenses, inventory, accounts payable, accrued expenses, accrued payroll and benefits, "
            "   deferred revenue, deposits, operating lease liabilities, postretirement benefits, split-interest obligations, "
            "   or other similar categories. "
            "3. If the cash flow statement provides a subtotal labeled 'Net change in operating assets and liabilities', "
            "   'Effect of changes in operating assets and liabilities', or equivalent wording, extract that subtotal directly. "
            "   Values shown in parentheses represent negative amounts and must be treated as such. "
            f"Extract only the figure reported for fiscal year {year}; ignore prior years and totals. "
            "Do not include non-cash adjustments such as depreciation, amortization, gains or losses on investments, "
            "or restricted contributions."
        )
    )

    other_changes_in_operating_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Operating Activities' for the {year} fiscal year. "
            "Ignore any amounts outside that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    net_cash_from_operating_activities: Optional[float] = Field(
        description=(
            f"Net cash from operating activities labeled 'Net Cash from Operating Activities' for the {year} fiscal year. "
            "Only use the figure for that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    capital_expenses: Optional[float] = Field(
        description=(
            f"Cash outflow for capital expenditures during the {year} fiscal year. "
            "Extract line items labeled 'Capital Expenses', 'Purchase of Property and Equipment', "
            "'Purchase of Capital Assets', 'Acquisition of Fixed Assets', or similar. "
            "Pay attention to the sign: values in parentheses represent negative numbers. "
            "Extract the exact numeric value as reported for the {year} column, without modifying its unit or sign. "
            "If multiple related line items exist, sum them together into a single total. "
            "Only extract values from the cash flow statement or detailed cash flow table corresponding to the current year. "
            "Do not extract from income statements, balance sheets, footnotes, or narrative sections."
        )
    )
    other_changes_in_investment_activities: Optional[float] = Field(
        description=(
            f"Line item 'Other Changes in Investment Activities' for the {year} fiscal year. "
            "Ignore entries outside that period."
            "Extract the number in its original form, without modifying its unit or sign. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    net_cash_from_investment_activities: Optional[float] = Field(
        description=(
            f"Net cash from investing activities labeled 'Net Cash from Investment Activities' for the {year} fiscal year. "
            "Use only the figure for that period."
            "Extract the number in its original form, without modifying its unit or sign. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )

    long_term_debt_net_proceeds: Optional[float] = Field(
        description=(
            f"Net cash inflows from issuance of long-term debt for fiscal year {year}. "
            "Extract amounts reported as proceeds or net proceeds from issuing bonds, notes payable, lease obligations, loans, or other long-term debt. "
            "Include gross proceeds plus any separately listed incentives, premiums, or additions, "
            "and subtract issuance costs, discounts, or other deductions directly related to the issuance. "
            "Relevant line items include: 'Proceeds from Bonds Payable', 'Proceeds from Notes Payable', "
            "'Proceeds from Notes and Bonds Payable', 'Proceeds from Lease Financing', 'Proceeds from Loan Obligations', "
            "'Proceeds from Debt Issuance', 'Proceeds from Finance Lease Incentives', 'Net Proceeds from Bond Issuance', "
            "'Bond Issuance Costs', or equivalent wording. "
            "If more than one applicable line exists, add these line items together into a single total. "
            "Values in parentheses represent negative amounts (e.g., issuance costs) and must be included as reported without flipping signs. "
            "Exclude principal repayments, refinancing transactions unrelated to new issuance, interest payments, and non-cash adjustments. "
            "Exclude proceeds from loans."
            f"Use only the column for fiscal year {year}; ignore prior years and total columns."
        )
    )

    payments_on_lease_liabilities: Optional[float] = Field(
    description=(
        f"Cash outflow labeled 'Payments on Lease Liabilities (Financing)' for fiscal year {year}. "
        "Extract only from the cash flow statement or statement of cash flows or detailed cash flow table for the current year. "
        "Do not extract from the financial statement notes or other financial sections，only from cash flow part. "
        f"Only use the value for fiscal year {year}, and exclude prior year data or total rows. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    long_term_debt_principal_payments: Optional[float] = Field(
        description=(
            f"Total cash outflows for payments, repayments, or retirements of debt during fiscal year {year}, "
            "including any principal reductions on bonds, notes, loans, or finance lease liabilities. "
            "Focus on items reported under the 'Financing Activities' or 'Capital and Related Financing Activities' sections "
            "of the cash flow statement, as these represent debt-related outflows. "
            "Extract every line item that represents a reduction of borrowing obligations, whether or not the word 'principal' appears, "
            "including all long-term and non-current debt unless explicitly identified as short-term. "
            "Relevant line items include: 'Repayment of Bonds Payable', 'Retirement of Bonds Payable', "
            "'Payments on Bonds Payable', 'Payments on Notes Payable', 'Payments on Notes and Bonds Payable', "
            "'Payments on Long-Term Debt', 'Payments on Debt Obligations', 'Repayment of Long-Term Debt', "
            "'Repayment of Lease Liabilities', 'Repayment of Leases', 'Payments on Financial Leases', "
            "'Payments on Finance Leases', 'Payments under Financing Leases', 'Repayment of Finance Lease Obligations', "
            "'Debt Repayments', 'Repayments of Principal of Indebtedness', 'Principal Payments', "
            "'Principal Payment of Non-Recourse Debt', 'Payments of Notes and Bonds Payable', "
            "'Payments on Bonds, Notes Payable and Finance Leases', or equivalent wording. "
            "If multiple applicable line items exist, add all of these line items together into one total. "
            "Exclude proceeds from new issuances, refinancing transactions unrelated to repayment, interest payments, "
            "non-cash adjustments, and reclassifications (e.g., current-portion adjustments). "
            f"Extract values only from the cash flow statement or detailed cash flow table for fiscal year {year}; "
            "ignore items outside the financing section, such as those under operating or investing activities. "
            "Values shown in parentheses represent negative cash flows and must be recorded as reported, without flipping their sign."
        )
    )

    change_in_long_term_debt: Optional[float] = Field(
        description=(
            f"Net change labeled 'Change in Long-Term Debt' for the {year} fiscal year. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only extract the figure for that period."
            "Extract the number in its original form, without modifying its unit or sign. "
        )
    )
    other_changes_in_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Financing Activities' for the {year} fiscal year. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only use that period's entry."
            "Extract the number in its original form, without modifying its unit or sign. "
        )
    )
    net_cash_from_financing_activities: Optional[float] = Field(
        description=(
            f"Net cash from financing activities labeled 'Net Cash from Financing Activities' for the {year} fiscal year. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "If the both fields 'cash_flows_from_noncapital_financing_activities' and 'cash_flows_from_capital_and_related_financing_activities' are populated, this field should be the combination of these fields."
            "Extract exclusively that period's figure."
            "Extract the number in its original form, without modifying its unit or sign. "
        )
    )
    change_in_cash_and_equivalents: Optional[float] = Field(
        description=(
            f"Overall 'Change in Cash & Equivalents' or 'Net change in cash and cash equivalents' for the {year} fiscal year. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Ignore any data from other periods."
            "Extract the number in its original form, without modifying its unit or sign. "
        )
    )
    cash_flow_2024_unit_multiplier: Optional[float] = Field(
         description=(
            f"Numeric multiplier corresponding to the unit (e.g., 'in thousands', 'in millions') used in the 2024 fiscal year's Statement of Cash Flows. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Return 1 if values are reported in dollars (i.e., no multiplier). "
            "Ensure this is strictly from the 2024 period only; ignore units from other years or sections."
        )
    )
    
