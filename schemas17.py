from typing import Optional
from pydantic import BaseModel, Field # type: ignore

YEAR = 2024
NEXT_ACAD = f"{YEAR}-{YEAR+1}"

class Enrollment2024_25(BaseModel):
    """
    Statement of Cash Flows for the fiscal year 2024 or 2023–2024.
    Only extract data from the 2023–2024 fiscal period (e.g. statements labeled ‘Fiscal Year 2024’ or date ranges covering 2023–2024).
    Ignore any figures outside this period.
    """
    Undergraduate_Headcount: Optional[int] = Field(
        description=(
            f"Total undergraduate headcount for the {NEXT_ACAD} academic year "
            "(Different than undergraduate FTE. Sometimes you need to combine both full-time and part time). "
            "Search around the tables to locate what type of enrollment information it is. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count or online and in-person count if applicable. "
            "If it didn't specify what kind of headcount it is, do not assume it's undergraduate headcount!!! "
            "Combine online and in-person if applicable. "
            "look around the table to see what type of data it is. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    
    Undergraduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            f"Undergraduate full-time or FT headcount for the {NEXT_ACAD} academic year. "
            "This is different than FTE(full-time equivalent). "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "Combine across all campuses if the institution has multiple locations. "
            "Don't assume it's undergraduate full time unless it says undergraduate in the data description. "
            "When there is no specification of what kind of full-time it is, it should be total full-time."
        )
    )
    Undergraduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            f"Undergraduate part-time (PT) headcount for the {NEXT_ACAD} academic year. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "Combine across all campuses if the institution has multiple locations. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "Don't assume it's undergraduate part time unless it says undergraduate in the data description. "
            "When there is no specification of what kind of part-time it is, it should be total part-time."
        )
    )
    Graduate_Headcount: Optional[int] = Field(
        description=(
            f"Total graduate headcount for the {NEXT_ACAD} academic year. "
            "Post baccalaureate is considered a graduate headcount. "
            "(Different than graduate FTE. Sometimes you need to combine both full-time and part time), "
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.), "
            "if the graduate headcount included both professional and graduate headcount, it's fine to just put them under graduate headcount. "
            "Combine online and in-person if applicable. "
            "which may be labeled “GR”, “Grad”, or “Graduate”. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count or online and in-person count if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            f"Graduate full-time (FT) headcount for the {NEXT_ACAD} academic year. "
            "Post baccalaureate is considered a graduate headcount. "
            "This is different than FTE(full-time equivalent). "
            "Combine across all graduate schools. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "Combine across campuses if needed. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "Don't assume it's graduate full-time unless it says undergraduate in the data description. "
            "When there is no specification of what kind of full-time it is, it should be total full-time."
        )
    )
    Graduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            f"Graduate part-time (PT) headcount for the {NEXT_ACAD} academic year. "
            "Post baccalaureate is considered a graduate headcount. "
            "Combine across all graduate schools. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "Combine across campuses if needed. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "Don't assume it's graduate part time unless it says undergraduate in the data description. "
            "When there is no specification of what kind of part-time it is, it should be total part-time."
        )
    )
    Professional_Headcount: Optional[int] = Field(
        description=(
            f"Combined professional school headcount (e.g. med, law) for the {NEXT_ACAD} academic year. "
            "(Different than professional FTE. Sometimes you need to combine both full-time and part time). "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Non_Degree_Headcount: Optional[int] = Field(
        description=(
            "(Different than Non-Degree FTE. Sometimes you need to combine both full-time and part time). "
            "Sometimes, Non-Degree is listed as Non-credit. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Total_Headcount: Optional[int] = Field(
        description=(
            f"Overall student headcount for the {NEXT_ACAD} academic year. "
            "do **not** compute it by adding Undergraduate, Graduate, Professional, etc. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Total_Headcount_Full_Time: Optional[int] = Field(
        description=(
            f"Total full-time headcount for the {NEXT_ACAD} academic year across all student categories. "
            "This is different than FTE(full-time equivalent). "
            "If not explicitly provided, sum Undergraduate_Headcount_Full_Time + Graduate_Headcount_Full_Time. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "do **not** derive it by summing individual full-time headcounts. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "When there is no specification of what kind of full-time it is, it should be total full-time."
        )
    )
    Total_Headcount_Part_Time: Optional[int] = Field(
        description=(
            f"Total part-time headcount for the {NEXT_ACAD} academic year across all student categories. "
            "If not explicitly provided, sum Undergraduate_Headcount_Part_Time + Graduate_Headcount_Part_Time. "
            f"Only extract data for the {NEXT_ACAD} year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data from other years or terms (e.g. 2023, 2023–2024, Fall 2023, Fall 2022, 2022). "
            "do **not** derive it by summing individual part-time headcounts. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "When there is no specification of what kind of part-time it is, it should be total part-time."
        )
    )


    Undergraduate_FTE: Optional[int] = Field(
        description=(
            f"Undergraduate full-time equivalent headcount or FTE for the {NEXT_ACAD} academic year. "
            "FTE (full-time equivalent) is different than full-time, or FT. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_FTE: Optional[int] = Field(
        description=(
            f"Graduate full-time headcount or FTE for the {NEXT_ACAD} academic year. "
            "Post baccalaureate is considered a graduate headcount. "
            "FTE (full-time equivalent) is different than full-time, or FT. "
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.). "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Professional_FTE: Optional[int] = Field(
        description=(
            f"Professional school full-time headcount or FTE for the {NEXT_ACAD} academic year. "
            "FTE (full-time equivalent) is different than full-time, or FT. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Total_Full_Time_Equivalent_Students: Optional[int] = Field(
        description=(
            f"Total full-time equivalent students (FTE) for the {NEXT_ACAD} academic year. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive it by summing individual FTE fields. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Undergraduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            f"Total undergraduate applications received for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            f"Total graduate applications received for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Applications_Rcvd: Optional[int] = Field(
        description=(
            f"Total transfer applications received for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Undergraduate_Acceptances: Optional[int] = Field(
        description=(
            f"Total undergraduate acceptances for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Acceptances: Optional[int] = Field(
        description=(
            f"Total graduate acceptances for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Acceptances: Optional[int] = Field(
        description=(
            f"Total transfer acceptances for the {NEXT_ACAD} cycle (e.g. Fall {YEAR}). "
            "Ignore other years/terms. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Undergraduate_Matriculants: Optional[int] = Field(
        description=(
            f"Number of undergraduate students who matriculated in Fall {YEAR} / {NEXT_ACAD}. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Matriculants: Optional[int] = Field(
        description=(
            f"Number of graduate students who matriculated in Fall {YEAR} / {NEXT_ACAD}. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Matriculants: Optional[int] = Field(
        description=(
            f"Number of transfer students who matriculated in Fall {YEAR} / {NEXT_ACAD}. "
            f"ignore any data from other years or terms (e.g. {YEAR-1}, {YEAR}-{YEAR}, Fall {YEAR-1}, Fall {YEAR-2}, 2022). "
            "Combine all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Retention_Rate: Optional[float] = Field(
        description=(
            f"Retention rate % for the {NEXT_ACAD} entering class (Fall {YEAR}). "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data outside this period. "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Full_Time_Employee_Equivalents: Optional[int] = Field(
        description=(
            f"Full-time employee equivalents (staff/faculty) for the {NEXT_ACAD} academic year. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data outside this period. "
            "It's possible for a school to have multiple campuses, so combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Tuition: Optional[int] = Field(
        description=(
            f"Undergraduate tuition rate for the {NEXT_ACAD} academic year. "
            "This is different than revenue generated by tuition or any financial accounting data. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data outside this period. "
            "If multiple campuses, average the tuition per student per campus. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Room_and_Board_20_meals: Optional[int] = Field(
        description=(
            f"Room & board cost (20-meal plan) for the {NEXT_ACAD} academic year. "
            f"Only extract data for the {NEXT_ACAD} academic year or terms labeled Fall {YEAR}, etc.; "
            "ignore any data outside this period. "
            "If multiple campuses, combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

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
            f"Cash amount labeled 'Total Change in Net Assets' for the {year} fiscal year, in US dollars. "
            "Only extract the exact figure for that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    total_non_cash_exp: Optional[float] = Field(
        description=(
            f"Total non-cash expenses for the {year} fiscal year, in US dollars. "
            "If the line item 'Total Non-Cash Exp' appears explicitly in the cash flow statement or its related table, extract that value. "
            "If not, calculate this as the sum of 'Depreciation' and 'Amortization' within the operating activities section of the cash flow statement. "
            "Only extract from the cash flow statement or table corresponding to the current year. "
            "Ignore values from income statements, balance sheets, footnotes, or prior years."
        )
    )
    change_in_working_capital: Optional[float] = Field(
        description=(
            f"Total Change in Working Capital for the {year} fiscal year, in US dollars. "
            "We will calculate this value from the detailed 'Cash Flows from Operating Activities' section, specifically from the subsection "
            "titled 'Change in assets and liabilities', 'Changes in operating assets and liabilities', 'changes in' or any equivalent label. "
            "calculate it by summing **all individual line items** listed under this subsection. These typically include:\n"
            "- Accounts receivable (net)\n"
            "- Contributions receivable\n"
            "- Prepaid expenses and other assets\n"
            "- Accounts payable and accrued expenses\n"
            "- Deferred revenue and other liabilities\n"
            "- Deferred charges, deferred benefits\n"
            "- Funds held in trust by others\n"
            "- Obligations under split-interest agreements\n"
            "- Other similar items"
            "**Section Identification Instructions:**\n"
            "- Look for a section within the operating cash flow titled 'Change in assets and liabilities', 'Changes in operating assets and liabilities', or similar.\n"
            "- Include **only and all** the rows that are visually indented under this block, up until the next subtotal line (e.g., 'Net cash provided by operating activities').\n"
            "- Include **every line under the block** exactly once; do not omit or duplicate."
            "\nReturn the final total as a float. Do not perform partial estimation or inference outside this section."
        )
    )
    other_changes_in_operating_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Operating Activities' for the {year} fiscal year, in US dollars. "
            "Ignore any amounts outside that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    net_cash_from_operating_activities: Optional[float] = Field(
        description=(
            f"Net cash from operating activities labeled 'Net Cash from Operating Activities' for the {year} fiscal year, in US dollars. "
            "Only use the figure for that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    capital_expenses: Optional[float] = Field(
        description=(
            f"Cash outflow for capital expenditures labeled 'Capital Expenses' in the {year} fiscal year, in US dollars. "
            "Extract the exact amount for that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    other_changes_in_investment_activities: Optional[float] = Field(
        description=(
            f"Line item 'Other Changes in Investment Activities' for the {year} fiscal year, in US dollars. "
            "Ignore entries outside that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    net_cash_from_investment_activities: Optional[float] = Field(
        description=(
            f"Net cash from investing activities labeled 'Net Cash from Investment Activities' for the {year} fiscal year, in US dollars. "
            "Use only the figure for that period."
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
        )
    )
    long_term_debt_net_proceeds: Optional[float] = Field(
    description=(
        f"Net cash inflow from long-term debt activities during the {year} fiscal year, in US dollars (not in thousands). "
        "Extract only from the cash flow statement or detailed cash flow table for the current year. "
        "Do not use the income statement, balance sheet, or footnotes. "
        "Compute this as the net of long-term debt issuances (e.g., 'Proceeds from Bonds/Notes/Leases') minus repayments or retirements (e.g., 'Repayment of Bonds Payable'). "
        "Do not confuse scheduled repayments with early extinguishment or refinancing. "
        "Exclude interest payments and non-cash adjustments. "
        "Only extract values explicitly labeled for fiscal year {year}. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    payments_on_bonds_payable: Optional[float] = Field(
    description=(
        f"Cash outflow labeled 'Payments on Bonds Payable' for fiscal year {year}, in US dollars (not in thousands). "
        "Extract only from the cash flow statement or detailed cash flow table for the current fiscal year. "
        "Do not use other sections of the financial report. "
        "Only extract the value corresponding to fiscal year {year}, not prior-year columns or totals. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    payments_on_notes_payable: Optional[float] = Field(
    description=(
        f"Cash outflow labeled 'Payments on Notes Payable' for fiscal year {year}, in US dollars (not in thousands). "
        "Extract only from the cash flow statement or detailed cash flow table for the current fiscal year. "
        "Do not use data from the balance sheet, income statement, or footnotes. "
        "Ensure the figure is labeled specifically for the {year} period. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    payments_on_lease_liabilities: Optional[float] = Field(
    description=(
        f"Cash outflow labeled 'Payments on Lease Liabilities (Financing)' for fiscal year {year}, in US dollars (not in thousands). "
        "Extract only from the cash flow statement or statement of cash flows or detailed cash flow table for the current year. "
        "Do not extract from the financial statement notes or other financial sections，only from cash flow part. "
        "Only use the value for fiscal year {year}, and exclude prior year data or total rows. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    long_term_debt_principal_payments: Optional[float] = Field(
    description=(
        f"Total principal repayments on long-term debt during the {year} fiscal year, in US dollars (not in thousands). "
        "Include all relevant cash outflows clearly identified as long-term debt principal repayments, even if labeled as bonds, notes, leases, or loans. "
        "If multiple related line items exist, sum them to obtain the total. "
        "if there are proceeds of bond issuance, do not include bond principle payments"
        "Exclude any interest payments, refinancing charges, or non-cash adjustments. "
        "Extract only from the cash flow statement or detailed table for the current year. "
        "Do not extract from income statement, balance sheet, footnotes, or other sections. "
        "Only use the value specifically labeled for the {year} period. "
        "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
        )
    )

    change_in_long_term_debt: Optional[float] = Field(
        description=(
            f"Net change labeled 'Change in Long-Term Debt' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only extract the figure for that period."
        )
    )
    other_changes_in_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Other Changes in Financing Activities' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only use that period's entry."
        )
    )
    cash_flows_from_noncapital_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Cash flows from noncapital financing activities' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only use that period's entry."
        )
    )

    cash_flows_from_capital_and_related_financing_activities: Optional[float] = Field(
        description=(
            f"Figure labeled 'Cash flows from capital and related financing activities' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Only use that period's entry."
        )
    )
    net_cash_from_financing_activities: Optional[float] = Field(
        description=(
            f"Net cash from financing activities labeled 'Net Cash from Financing Activities' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "If the both fields 'cash_flows_from_noncapital_financing_activities' and 'cash_flows_from_capital_and_related_financing_activities' are populated, this field should be the combination of these fields."
            "Extract exclusively that period's figure."
        )
    )
    change_in_cash_and_equivalents: Optional[float] = Field(
        description=(
            f"Overall 'Change in Cash & Equivalents' or 'Net change in cash and cash equivalents' for the {year} fiscal year, in US dollars. "
            "Only extract values from the cash flow statement or table corresponding to the current year. Do not use other sections of the PDF or unrelated financial statements (e.g., income statement, balance sheet, or footnotes)"
            "Ignore any data from other periods."
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
