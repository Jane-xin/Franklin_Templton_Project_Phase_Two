from typing import Optional
from pydantic import BaseModel, Field # type: ignore

def generate_endowment_schema(fiscal_year: int):
    fy_label = str(fiscal_year)
    fy_label_short = f"FY{fy_label}"
    fy_range = f"{fiscal_year}–{fiscal_year+1}"
    eoy_date = f"June 30, {fiscal_year}"

    class EndowmentAndInvestmentLevels(BaseModel):
         """
        Endowment and investment data extraction for the fiscal year {fy_label}.

        Only extract data explicitly labeled for the {fy_label} fiscal year, including tables that reference '{fy_label}', '{fy_label_short}', or have dates ending with '{eoy_date}'.
        Do not extract figures from prior fiscal years, unaudited statements, summarized overviews, or systemwide rollups.

        Extract from either the primary financial statements (e.g., Statement of Net Position, Statement of Activities) or from detailed, structured tables found in the Notes section. 
        If using tables in the Notes, ensure they are clearly labeled, structured (e.g., matrix format), and correspond directly to the endowment or investment disclosures for the {fy_label} fiscal year.
        Do not extract values from narrative paragraphs, rollforwards, or footnotes unless they are accompanied by structured tables.

        Do not compute, infer, or derive values — extract only if the amount is explicitly stated and clearly labeled.
        Use the number exactly as it appears in the document; only apply unit conversions (e.g., '$000s') if the table context explicitly provides it.
        Values shown in parentheses (e.g., (1,200)) represent negative amounts and should be interpreted as such.
         """

        # ───── ENDOWMENT ASSETS ─────
        
         endowment_net_assets_eoy_total: Optional[float] = Field(
            description=(
                f"Total endowment net assets for the {fy_label} fiscal year (in thousands). "
                "Only extract from a table titled 'Changes in Endowment Net Assets' located in the Notes section. "
                f"Only use data explicitly labeled as '{fy_label}', '{fy_label_short}', or 'as of {eoy_date}'. "
                "Do not extract from general balance sheets, rollforwards, or systemwide summaries. "
                "Standardize all values to $000s using table metadata or heuristics."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions: Optional[float] = Field(
            description=(
                f"Total donor-restricted endowment net assets as of {eoy_date} (in thousands). "
                "Must be extracted from a 'Changes in Endowment Net Assets' table in the Notes section. "
                f"Exclude all {fiscal_year - 1} or earlier data. Must be clearly labeled as {fy_label}."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[float] = Field(
            description=(
                f"Temporarily restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Must appear in a table under Notes with a clear {fy_label} label. Ignore unlabeled or earlier year data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[float] = Field(
            description=(
                f"Permanently restricted portion of donor-restricted endowment net assets for {fy_label_short} (in thousands). "
                f"Only extract from Notes where clearly labeled as {fy_label}."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         endowment_net_assets_eoy_without_donor_restrictions: Optional[float] = Field(
            description=(
                f"Unrestricted portion of endowment net assets for the {fy_range} fiscal year (in thousands). "
                "Must be pulled from a 'Changes in Endowment Net Assets' table in Notes. "
                f"Only extract if labeled as {fy_label}. Ignore prior-year or aggregated system data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

        # ───── ENDOWMENT SPENDING ─────
         appropriation_of_endowment_for_expenditure_total: Optional[float] = Field(
            description=(
                f"Total appropriations or spending from the endowment during {fy_range} (in thousands). "
                "Only extract from the 'Changes in Endowment Net Assets' table in the Notes section. "
                "Do not infer from general text or extract from unlabeled rows."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         appropriation_of_endowment_for_expenditure_with_donor_restrictions: Optional[float] = Field(
            description=(
                f"Appropriations from donor-restricted endowment funds for {fy_label_short} (in thousands). "
                f"Must appear in a {fy_label}-labeled row of the Notes. Ignore prior years and total-only rows."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

         appropriation_of_endowment_for_expenditure_without_donor_restrictions: Optional[float] = Field(
            description=(
                f"Appropriations from unrestricted endowment funds during {fy_range} (in thousands). "
                f"Must appear in a 'Changes in Endowment Net Assets' table and be labeled {fy_label}. Ignore earlier data."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )
        # ───── FAIR VALUE HIERARCHY – ENDOWMENT INVESTMENTS ─────

         investment_level_1: Optional[float] = Field(
            description=(
                f"Fair value of Level 1 investments (quoted prices in active markets) within the endowment portfolio as of {eoy_date} (in thousands). "
                "Only extract if this value is **explicitly labeled as Level 1** and appears in a structured fair value hierarchy table, matrix, or detailed breakdown "
                "specific to **endowment or university investments**. "
                "Do not include any amounts from pension plans, foundations, or other non-endowment entities. "
                "Do not derive totals by adding components. Use only clearly labeled and explicitly reported Level 1 values. "
                "Ensure the source table refers to the current fiscal year ({fy_label}). "
                "Note: Parentheses indicate negative values and should be recorded as negatives."
            )
        )

         investment_level_2: Optional[float] = Field(
            description=(
                f"Fair value of Level 2 investments (significant other observable inputs) within the endowment portfolio as of {eoy_date} (in thousands). "
                "Only extract if this is clearly labeled as Level 2 and found within a fair value hierarchy table or detailed breakdown specifically for university or endowment investments. "
                "Exclude any data related to pension plans, benefit plans, or external foundations. "
                "Do not infer or calculate this value — extract only when presented explicitly as a total Level 2 value. "
                "Use only current fiscal year ({fy_label}) data. "
                "Treat values in parentheses as negative."
            )
        )

         investment_level_3: Optional[float] = Field(
            description=(
                f"Fair value of Level 3 investments (significant unobservable inputs) for endowment investments as of {eoy_date} (in thousands). "
                "Extract only if clearly labeled as Level 3 in a structured table or disclosure tied to university or endowment investments. "
                "Do not include amounts from 'PENSION PLAN ASSETS' or similar. "
                "Avoid any computed values or inferred amounts — only extract the total if explicitly stated. "
                "Only use values from the {fy_label} fiscal year. "
                "Negative values may be shown in parentheses."
            )
        )

         investments_measured_at_nav: Optional[float] = Field(
            description=(
                f"Total value of endowment investments measured at NAV (Net Asset Value) as of {eoy_date} (in thousands). "
                "Only extract when a NAV row or column is clearly labeled within a fair value hierarchy disclosure pertaining to university or endowment investments. "
                "Do not compute NAV as a residual. "
                "Exclude pension/foundation-related NAV disclosures. "
                "If the table includes Life Insurance Cash Surrender Value as part of NAV, only include it when clearly tagged and tied to the endowment. "
                "Use data only from the {fy_label} fiscal year. "
                "Treat values in parentheses as negative."
            )
        )

         investments_total_fair_value: Optional[float] = Field(
            description=(
                f"Total fair value of all endowment investments as of {eoy_date} (in thousands). "
                "Extract only if explicitly presented in a row labeled 'Total Fair Value', 'Total Investments', or equivalent within the fair value hierarchy or investment valuation table. "
                "The value must pertain to endowment or university assets only — exclude any totals labeled for pensions, foundations, or consolidated entities. "
                "Do not calculate this by summing Level 1,2,3 or NAV. "
                "Only extract if the table or disclosure is from the {fy_label} fiscal year. "
                "Parentheses indicate negative values."
            )
        )


      
        # ───── LONG TERM DEBT ───── 
         total_outstanding_principal_long_term_debt: Optional[float] = Field(
            description=(
                f"Total outstanding principal of long-term debt or bonds payable as of {eoy_date} (in thousands). "
                "Extract this only from the 'Long-Term Debt' or 'Bonds Payable' section in the Notes. "
                f"Only use figures clearly labeled as pertaining to {fy_label} or {fy_label_short}. "
                "Exclude any amortization schedules, summaries from other fiscal years, or consolidated entities."
                "Note: Values in parentheses (e.g., (3,705)) represent negative cash flows and should be treated as such."
            )
        )

    return EndowmentAndInvestmentLevels
