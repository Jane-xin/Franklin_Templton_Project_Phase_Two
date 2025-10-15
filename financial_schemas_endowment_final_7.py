from typing import Optional
from pydantic import BaseModel, Field # type: ignore

def generate_endowment_schema(fiscal_year: int):
    fy_label = str(fiscal_year)
    fy_label_short = f"FY{fy_label}"
    fy_range = f"{fiscal_year}–{fiscal_year+1}"
    eoy_date = f"June 30, {fiscal_year}"

    class EndowmentAndInvestmentLevels(BaseModel):
         """
        Endowment and Investment data extraction for the fiscal year {fy_label}.

        Only extract data explicitly labeled for the {fy_label} fiscal year, including tables labeled '{fy_label}', '{fy_label_short}', or ending on '{eoy_date}'.
        Do not extract figures from prior fiscal years or any unaudited, summarized, or systemwide statements.
        Extract only from fully detailed tables within the Notes section (e.g., 'Changes in Endowment Net Assets' or 'Fair Value Hierarchy'), not from summary tables or rollforwards.
        Do not compute, infer, or derive values unless the amount is clearly and directly labeled.
        Use the number exactly as shown; do not convert units unless table context (e.g., '$000s') explicitly applies.
        If a table shows negative values using parentheses (e.g., (1,200)), interpret them as negative numbers.
        """
        # ───── ENDOWMENT ASSETS ─────
        
         endowment_net_assets_eoy_total: Optional[int] = Field(
            description=(
                f"Total endowment net assets for the {fy_label} fiscal year (in thousands). "
                "Only extract from a table titled 'Changes in Endowment Net Assets' located in the Notes section. "
                f"Only use data explicitly labeled as '{fy_label}', '{fy_label_short}', or 'as of {eoy_date}'. "
                "Do not extract from general balance sheets, rollforwards, or systemwide summaries. "
                "Standardize all values to $000s using table metadata or heuristics."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions: Optional[int] = Field(
            description=(
                f"Total donor-restricted endowment net assets as of {eoy_date} (in thousands). "
                "Must be extracted from a 'Changes in Endowment Net Assets' table in the Notes section. "
                f"Exclude all {fiscal_year - 1} or earlier data. Must be clearly labeled as {fy_label}."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[int] = Field(
            description=(
                f"Temporarily restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Must appear in a table under Notes with a clear {fy_label} label. Ignore unlabeled or earlier year data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[int] = Field(
            description=(
                f"Permanently restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Only extract from Notes where clearly labeled as {fy_label}."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_without_donor_restrictions: Optional[int] = Field(
            description=(
                f"Unrestricted portion of endowment net assets for the {fy_range} fiscal year (in thousands). "
                "Must be pulled from a 'Changes in Endowment Net Assets' table in Notes. "
                f"Only extract if labeled as {fy_label}. Ignore prior-year or aggregated system data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

        # ───── ENDOWMENT SPENDING ─────
         appropriation_of_endowment_for_expenditure_total: Optional[int] = Field(
            description=(
                f"Total appropriations or spending from the endowment during {fy_range} (in thousands). "
                "Only extract from the 'Changes in Endowment Net Assets' table in the Notes section. "
                "Do not infer from general text or extract from unlabeled rows."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         appropriation_of_endowment_for_expenditure_with_donor_restrictions: Optional[int] = Field(
            description=(
                f"Appropriations from donor-restricted endowment funds for {fy_label_short} (in thousands). "
                f"Must appear in a {fy_label}-labeled row of the Notes. Ignore prior years and total-only rows."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         appropriation_of_endowment_for_expenditure_without_donor_restrictions: Optional[int] = Field(
            description=(
                f"Appropriations from unrestricted endowment funds during {fy_range} (in thousands). "
                f"Must appear in a 'Changes in Endowment Net Assets' table and be labeled {fy_label}. Ignore earlier data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

        # ───── INVESTMENT VALUATION (FAIR VALUE HIERARCHY) ─────
         investment_level_1: Optional[int] = Field(
            description=(
                f"Fair value of Level 1 investments (quoted market prices) at {eoy_date} (in thousands). "
                "Extract from a fair value hierarchy table or any equivalent disclosure in the Notes section that classifies investment inputs by level. "
                "Ensure the table is for the university, not an enterprise or foundation. "
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         investment_level_2: Optional[int] = Field(
            description=(
                f"Fair value of Level 2 investments (observable inputs) as of the end of {fy_label_short} (in thousands). "
                "Extract from a fair value hierarchy table or any equivalent disclosure in the Notes section that classifies investment inputs by level. "
                "Must be extracted from the same fair value hierarchy table in the Notes section. "
                f"Only use data labeled {fy_label}. Avoid mixing rows from different years or sources."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         investment_level_3: Optional[int] = Field(
            description=(
                f"Fair value of Level 3 investments (unobservable inputs) at year-end {fy_label} (in thousands). "
                "Extract from a fair value hierarchy table or any equivalent disclosure in the Notes section that classifies investment inputs by level. "
                f"Only extract from {fy_label}-labeled fair value tables in the Notes. Ignore mixed-year summaries."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

        # ───── NAV & TOTAL FAIR VALUE ─────
         investments_measured_at_nav: Optional[int] = Field(
            description=(
                f"Total value of investments measured at Net Asset Value (NAV) at {eoy_date} (in thousands). "
                "Only extract if the value is explicitly shown in a fair value hierarchy table or clearly labeled NAV-related row in the Notes section. "
                "Do not infer, calculate, or combine values across multiple tables or years. "
                "If the NAV value is not present in the fair value table for the current fiscal year, leave this field blank—even if other narrative mentions NAV. "
                "Strictly prohibit computing NAV by subtracting Level 1–3 totals from the overall investment total. "
                "Include Life Insurance Cash Surrender value only if it is explicitly stated as NAV-based. "
                "Ensure all values are from the {fy_label} period and not from consolidated or foundation-level data. "
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )



         investments_total_fair_value: Optional[int] = Field(
            description=(
                f"Total fair value of all university investments as of fiscal year end {fy_range} (in thousands). "
                "Extract this number from the table that breaks down investments by type (e.g., common stock, mutual funds, fixed income, etc.), "
                "which may or may not include NAV or Level 1–3 information. "
                "Ignore totals from prior years, foundations, or consolidated entities. "
                "Do not infer or estimate values—only extract if the total is explicitly shown in a tabular form. "
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )
        # ───── LONG TERM DEBT ───── 
         total_outstanding_principal_long_term_debt: Optional[int] = Field(
            description=(
                f"Total outstanding principal of long-term debt or bonds payable as of {eoy_date} (in thousands). "
                "Extract this only from the 'Long-Term Debt' or 'Bonds Payable' section in the Notes. "
                f"Only use figures clearly labeled as pertaining to {fy_label} or {fy_label_short}. "
                "Exclude any amortization schedules, summaries from other fiscal years, or consolidated entities."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )


    return EndowmentAndInvestmentLevels
