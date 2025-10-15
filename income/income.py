from typing import Optional
from pydantic import BaseModel, Field, model_validator

def generate_income_statement_schema(fiscal_year: int):
    fy_label = str(fiscal_year)

    class IncomeStatement(BaseModel):

# =============================================================================
# UNITS / TUITION & FEES
# =============================================================================

        unit_multiplier: Optional[float] = Field(
            description=f"Numeric multiplier corresponding to the unit (e.g., 'in thousands', 'in millions') used in the "
                        f"{fy_label} fiscal year's Statement of Activities or Statement of Changes in Net Assets. "
                        "EXTRACT ONLY from financial statement table headers, column headers, or table footnotes. "
                        "DO NOT extract from narrative text or MD&A sections. "
                        "Return 1000 for 'in thousands', 1000000 for 'in millions', 1 if values are reported in dollars with no multiplier. "
                        "Look for unit indicators near the financial statement headers, column headers, or at the top/bottom of tables. "
                        "Ensure this is strictly from the {fy_label} period only; ignore units from incorrect years or sections."
        )

        gross_tuition_revenue: Optional[int] = Field(
            description=f"Gross tuition and fees revenue BEFORE any deductions for {fy_label}. "
                        "Extract ONLY from the primary Statement of Activities/Operations/Revenues pages; "
                        "IGNORE Notes/MD&A/supplementary schedules and do not combine across pages. "
                        "Use ONLY the current-year 'Without Donor Restrictions' column. "
                        "Look for labels including: 'Gross Tuition and Fees', 'Tuition and Fees – Gross', "
                        "'Total Student Tuition and Fees' (when explicitly gross), 'Tuition Revenue' (when before aid). "
                        "If gross tuition is not directly shown, calculate as net_tuition_revenue + financial_aid. "
                        "If net tuition includes a disclosed aid deduction (e.g., 'net of financial aid of $X'), "
                        "use $X as financial_aid and add to net_tuition_revenue. "
                        "Must be the amount BEFORE financial aid deductions. "
                        "Extract the raw numeric value only – ignore formatting symbols; distinguish dollar signs ($) from digit 5."
        )

        financial_aid: Optional[int] = Field(
            description=f"Institutional financial aid, scholarships, or tuition discounts for {fy_label}. "
                        "Extract ONLY from the primary Statement of Activities/Operations/Revenues pages; "
                        "IGNORE Notes/MD&A/supplementary schedules and do not combine across pages. "
                        "Use ONLY the current-year 'Without Donor Restrictions' column. "
                        "Can appear as direct expense line items, including: 'Financial Aid', 'Scholarships and Fellowships', "
                        "'Tuition Discount', 'Student Aid', 'Allowances', 'Scholarship Allowance'. "
                        "Can also appear as deductions from gross tuition (in parentheses) or as disclosed amounts in tuition notes, "
                        "such as 'Net of Allowance of $X' or 'net of financial aid of $X' — extract the disclosed allowance/aid amount. "
                        "Extract the raw numeric value only – ignore formatting symbols; distinguish dollar signs ($) from digit 5."
        )

        net_tuition_revenue: Optional[int] = Field(
            description=f"Net tuition and fees revenue AFTER financial aid deductions for {fy_label}. "
                        "Extract ONLY from the primary Statement of Activities/Operations/Revenues pages; "
                        "IGNORE Notes/MD&A/supplementary schedules and do not combine across pages. "
                        "Use ONLY the current-year 'Without Donor Restrictions' column. "
                        "Look for labels including: 'Tuition and Fees, Net', 'Net Tuition and Fees', "
                        "'Student Tuition and Fees' (when explicitly net), 'Tuition and Fees, net of financial aid of $X'. "
                        "Should equal gross_tuition_revenue minus financial_aid when both are available. "
                        "Extract the raw numeric value only – ignore formatting symbols; distinguish dollar signs ($) from digit 5."
        )

        # =============================================================================
        # GIFTS, GRANTS, CONTRACTS, APPROPRIATIONS & INVESTMENT INCOME (OPERATING)
        # =============================================================================

        government_grants_contracts_total: Optional[int] = Field(
            description=f"TOTAL Government grants & contracts (Federal + State/Local combined) for {fy_label}. "
                        "Extract ONLY from the current-year 'Without Donor Restrictions' column. "
                        "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
                        "SOURCE: Prefer the primary Statement of Activities/Operations table; notes allowed ONLY if all values in the gifts "
                        "section come from the SAME note/table within a ≤2-page range. "
                        "Look for labels including: 'Government Grants and Contracts', 'Government Contracts', 'Government Grants', "
                        "'Total Government Support', 'Government Revenue'. "
                        "If both Federal and State/Local numbers are listed, return their SUM here; if a single combined line exists, return it here. "
                        "If the report lists just 'Grants' (no qualifier) and it is not clearly private, default to GOVERNMENT and include it here. "
                        "STRICT RULE: Do NOT include appropriations. If 'Government Grants AND Appropriations' are combined and cannot be separated, "
                        "leave this field BLANK and include the combined amount only in total_gifts_contracts_other_support. "
                        "Return raw numeric value only."
        )

        private_gifts_grants_contracts: Optional[int] = Field(
            description=f"PRIVATE gifts, grants, contracts, and SUPPORT WITHOUT donor restrictions for {fy_label}. "
                        "Source: primary Statement of Activities/Operations (financial statement table), current-year 'Without Donor Restrictions' column. "
                        "INCLUDE any OPERATING line whose label contains 'Contribution' (case-insensitive), e.g., "
                        "'Contributions of cash and other financial assets', 'Contributions of nonfinancial assets', 'Private Contributions'; "
                        "also include 'Private Gifts and Grants', 'Private Support', 'Donations', 'Private Contracts'. "
                        "EXCLUDE Government grants/contracts and any investment or non-operating items. "
                        "If an explicit subtotal such as 'Private gifts, grants and contracts' or 'Private support' exists, use it; "
                        "otherwise SUM all qualifying 'Contribution' rows (cash + nonfinancial) and other private-support rows. "
                        "Return raw numeric value; preserve sign (parentheses = negative)."
        )

        total_gifts_contracts_other_support: Optional[int] = Field(
            description=f"TOTAL: All gifts, grants, contracts & support, including state appropriations, for {fy_label}. "
                        "If an explicit total line exists (e.g., 'Total Gifts, Grants & Contracts/Support'), return that. "
                        "Otherwise compute as: government_grants_contracts_total + state_appropriations + "
                        "private_gifts_grants_contracts + other contributions not already counted. "
                        "EXCEPTION: If only a combined 'Government Grants and Appropriations' is shown and cannot be split, "
                        "include that COMBINED value HERE and leave government_grants_contracts_total blank. "
                        "Explicitly exclude tuition/fees, investment income, auxiliary/enterprise revenue, and unrelated appropriations. "
                        "Avoid double-counting with subtotals/totals. Return raw numeric value only."
        )

        state_appropriations: Optional[int] = Field(
            description=f"State appropriations or base state funding for {fy_label}. "
                        "Extract ONLY from the current-year 'Without Donor Restrictions' column. "
                        "Prefer the primary Statement of Activities/Operations table; notes allowed ONLY if the gifts section values "
                        "come from the SAME note/table within a ≤2-page range. "
                        "INCLUDE any line that says 'Appropriations' (e.g., 'State Appropriations', 'Government Appropriations', 'Appropriations—State'); "
                        "also include 'State Funding', 'State Support – Appropriations'. "
                        "These are base funding/appropriation lines, not grants/contracts. If unsure, leave blank. "
                        "Return raw number; preserve sign; ignore formatting."
        )

        private_gifts_with_donor_restrictions: Optional[int] = Field(
            description=f"Private gifts and contributions WITH donor restrictions for {fy_label}. "
                        "Extract ONLY from the main Statement of Activities (financial statement tables). "
                        "DO NOT extract from narrative text, footnotes, notes, supplementary schedules, or explanatory paragraphs. "
                        "Look only for line item labels including: 'Private Gifts and Grants', 'Contributions', 'Private Contributions', "
                        "'Private Support', 'Donations', 'Private Contracts'. "
                        "Extract strictly from the 'With Donor Restrictions' column (current year). "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        # investment_income_operations: Optional[int] = Field(
        #     description=f"Investment income for OPERATIONS WITHOUT donor restrictions for {fy_label}. "
        #                 "Extract ONLY from the primary Statement of Activities/Operations/Revenues (primary FS pages). "
        #                 "IGNORE Notes, MD&A, Endowment rollforwards, Supplementary Schedules. "
        #                 "Use ONLY the current-year 'Without Donor Restrictions' column. "
        #                 "This represents the portion of investment return appropriated or designated for operations (i.e., the spending distribution or endowment payout used to fund annual expenses). "
        #                 "Match operating payout labels like: 'Endowment Income Designated for Operations', "
        #                 "'Net Investment Return Designated for Operations', 'Operating Investment Return for operations', 'Spending Distribution for operations'. "
        #                 "Do NOT combine data across pages. If a subtotal/total already includes components, use that only. "
        #                 "Return raw number only."
        # )
        investment_income_operations: Optional[int] = Field(
            description=f"Investment income/return REPORTED WITHIN THE OPERATING SECTION of the WITHOUT donor restrictions (WDR) column for {fy_label}. "
                        "Definition: the portion of investment return appropriated/designated for operations (spending distribution / payout used to fund annual expenses). "
                        "Primary sources: Statement of Activities / Statement of Operations, WDR column only. Ignore Notes/MD&A/rollforwards/supplementary schedules. "
                        "Recognize common labels/aliases for OPERATING amounts, including (case-insensitive): "
                        "  - 'Operating investment return' / 'Investment return appropriated (allocated) for operations' "
                        "  - 'Endowment income designated for operations' "
                        "  - 'Endowment distribution' / 'Endowment distribution to operations' / 'Endowment transfer (to operations)' "
                        "  - 'Interest earnings' / 'Other investment income' when clearly classified as operating "
                        "  - 'Net investment return designated for operations' / 'Amounts distributed for spending' "
                        "Equations (use ONLY if no explicit operating subtotal exists, and components are in WDR): "
                        "  (1) Operating investment return = Endowment (investment) return appropriated for spending + Other investment income (operating) "
                        "Precedence: prefer an explicit operating line/subtotal; otherwise compute from clearly labeled components without crossing pages/sections. "
                        "Do NOT net with non-operating remeasurement/appreciation; do NOT mix donor-restricted columns. "
                        'Return the raw number only (respecting signs/parentheses).'
        )

        # investment_income_total: Optional[int] = Field(
        #     description=f"TOTAL investment income/return WITHOUT donor restrictions for {fy_label}. "
        #                 "Extract ONLY from the primary Statement of Activities/Operations/Revenues pages; "
        #                 "IGNORE Notes/MD&A/supplementary schedules and do not combine across pages. "
        #                 "Use ONLY the current-year 'Without Donor Restrictions' column. "
        #                 "Target = operating investment return (WDR) + any OTHER investment return amounts (WDR) on the statement "
        #                 "(e.g., non-operating investment return/appreciation) — all within WDR. "
        #                 "Otherwise SUM relevant WDR lines with 'investment' in the label, including operating and non-operating, "
        #                 "but avoid double-counting when a subtotal/total already includes components. "
        #                 "If no non-operating WDR amounts are present, return the operating investment return (WDR). "
        #                 "Return the raw number only."
        # )

        investment_income_total: Optional[int] = Field(
            description=f"TOTAL net investment income/return in the WITHOUT donor restrictions (WDR) column for {fy_label}. "
                        "Primary sources: Statement of Activities / Operations (current FY), WDR column only. Ignore Notes/MD&A/rollforwards/supplementary schedules. "
                        "Recognize labels/aliases for TOTAL WDR amounts: "
                        "  - 'Total net investment return (Without donor restrictions)' "
                        "  - 'Net investment return — Without donor restrictions' "
                        "  - 'Investment return (WDR), total' "
                        "If an explicit TOTAL is absent, SAFE computations (WDR only): "
                        "      Total WDR = Endowment distribution for spending + Other investment income (operating) "
                        "      (Use this identity only if line labels clearly indicate these components and no subtotal already includes them.) "
                        "Precedence: use an explicit WDR total if present; otherwise sum clearly labeled WDR operating + WDR non-operating lines, avoiding double-counting if a subtotal already includes components. "
                        "If only an operating WDR amount exists and the statement indicates no other WDR investment return, set total = operating; otherwise leave blank. "
                        'Return the raw number only (respecting signs/parentheses).'
        )


        investment_income_with_donor_restrictions: Optional[int] = Field(
            description=f"OPERATING investment income WITH donor restrictions for {fy_label}. "
                        "Extract ONLY from the primary Statement of Activities/Operations/Revenues page(s); "
                        "IGNORE Notes/MD&A/supplementary pages and DO NOT combine across pages. "
                        "Use ONLY the current-year 'With Donor Restrictions' column (synonyms: 'Restricted', 'Temporarily Restricted'). "
                        "Match operating payout labels such as 'Investment Return – Operating', 'Investment Income for Operations', "
                        "'Endowment Distribution to Operations', 'Amounts Appropriated for Expenditure', 'Endowment transfer','Interest earnings'"
                        "'Net Investment Return Designated for Current Operations'. "
                        "Exclude non-operating sections and note rollforwards. "
                        "If both components and a subtotal/total exist, use the subtotal; otherwise SUM qualifying lines on the same table. "
                        "Return the raw number only."
        )

        # =============================================================================
        # OTHER OPERATING REVENUE
        # =============================================================================

        auxiliary_enterprise_revenue: Optional[int] = Field(
            description=f"Revenue from auxiliary enterprises for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
                        "Look for labels including: 'Auxiliary Enterprises', 'Auxiliary Services', 'Housing and Dining', "
                        "'Residence Halls', 'Food Service', 'Parking'. "
                        "Revenue from self-supporting activities like dormitories, dining, bookstores, parking. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        healthcare_clinical_revenue: Optional[int] = Field(
            description=f"Healthcare/clinical services REVENUE for {fy_label}. "
                        "PRECONDITION: Extract ONLY if the institution operates a hospital/medical center/clinic. "
                        "Before extracting, scan the document for any of these keywords (case-insensitive): "
                        "'hospital', 'medical center', 'health system', 'clinic', 'clinical services', 'patient care', "
                        "'healthcare', 'medical practice', 'physician group', 'health services revenue'. "
                        "If NONE of the keywords appear anywhere in the report, LEAVE BLANK. "
                        "SOURCE: Extract ONLY from financial statement TABLES (Statement of Activities/Operations) and ONLY from the "
                        "current-year 'Without Donor Restrictions' column. "
                        "Look for row labels such as: 'Medical Center Revenue', 'Clinical Services', 'Healthcare Revenue', "
                        "'Hospital Revenue', 'Patient Care Revenue'. "
                        "If multiple qualifying rows exist for the same category, return their SUM while avoiding double-count with any "
                        "displayed subtotal/total (prefer the category's explicit 'Total' line when present). "
                        "EXCLUDE student health fees/auxiliary charges, insurance recoveries, and any non-clinical operating revenue. "
                        "Return the raw numeric value only — ignore formatting symbols."
        )

        net_assets_released_from_restrictions: Optional[int] = Field(
            description=f"Net assets released from donor restrictions for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
                        "Look for labels including: 'Net Assets Released from Restrictions', 'Released from Restrictions', "
                        "'Restrictions Satisfied'. "
                        "Represents restricted funds that became available for use during the current year. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        other_operating_rev: Optional[int] = Field(
            description=f"Other operating revenues for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
                        "Look for labels including: 'Other Revenues', 'Other Income (Loss), Net', 'Miscellaneous Revenue', "
                        "'Other Operating Revenue'. "
                        "Include operating revenue line items not captured in the main categories above. "
                        "EXCLUDE net tuition, total gifts/grants, total investment income, auxiliary, healthcare, "
                        "and net assets released (counted elsewhere). "
                        "Extract the raw numeric value only – ignore formatting symbols. If not found, return NULL."
        )

        total_operating_revenue: Optional[int] = Field(
            description=f"Total operating revenues for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "DO NOT extract from narrative text, footnotes, or explanatory paragraphs. "
                        "Look for explicit total line items such as: 'Total Operating Revenues', 'Total Operating Revenue', 'Total Revenues'. "
                        "Should represent the sum of all operating revenue sources. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        # =============================================================================
        # FUNCTIONAL EXPENSES (PRIMARILY FROM FUNCTIONAL EXPENSES NOTE/TABLE)
        # =============================================================================

        instructional_expense: Optional[int] = Field(
            description=f"Instructional expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note, usually in the NOTES section "
                        "(tables titled 'Statement of Functional Expenses', 'Functional Expenses', or similar; verify 'functional expenses' "
                        "is explicitly mentioned). "
                        "Locate the 'Instruction'/'Instructional' category and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Instruction Total'). "
                        "DO NOT extract from the Statement of Activities at the beginning of the report. "
                        "DO NOT extract intermediate rows or subtotals. "
                        "If NO functional expenses table exists anywhere, then extract from the operating expenses section of the "
                        "Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        research_expense: Optional[int] = Field(
            description=f"Research expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note (see rules above). "
                        "Locate 'Research'/'Sponsored Research' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Research Total'). "
                        "DO NOT extract subtotals, intermediate amounts, or line-item details. "
                        "If NO functional expenses table exists, extract from the operating expenses section of the Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        instructional_research_expense: Optional[int] = Field(
            description=f"Combined INSTRUCTION + RESEARCH expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Prefer a combined 'Instruction and Research' column TOTAL (bottom line). "
                        "If NO combined column exists but separate 'Instruction' and 'Research' columns exist, "
                        "SUM their bottom-row totals. "
                        "DO NOT extract from the Statement of Activities; DO NOT use intermediate rows/subtotals. "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        auxiliary_enterprise_expense: Optional[int] = Field(
            description=f"Auxiliary enterprise expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Auxiliary Enterprises'/'Auxiliary' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Auxiliary Total'). "
                        "DO NOT extract from the Statement of Activities; do not take subtotals or line-item details. "
                        "If NO functional expenses table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        healthcare_clinical_expense: Optional[int] = Field(
            description=f"Healthcare/clinical services EXPENSES WITHOUT donor restrictions for {fy_label}. "
                        "PRECONDITION: Only if the institution operates a hospital/medical center/clinic. "
                        "Scan for keywords: 'hospital', 'medical center', 'health system', 'clinic', 'clinical services', 'patient care', "
                        "'healthcare', 'medical practice', 'physician group', 'health services expense'. "
                        "If NONE are found, LEAVE BLANK. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "DO NOT extract from the Statement of Activities; DO NOT take subtotals or intermediate components—take the category TOTAL only. "
                        "Look for labels including: 'Medical Center Expenses', 'Clinical Services Expenses', 'Healthcare Expenses', 'Hospital Operations'. "
                        "EXCLUDE depreciation/interest if presented separately from operating categories. "
                        "Return the raw numeric value only—ignore formatting symbols."
        )

        academic_support: Optional[int] = Field(
            description=f"Academic support expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Academic Support' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Academic Support Total'). "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Labels include: 'Academic Support', 'Library', 'Academic Services', 'Curriculum Development'. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        student_services: Optional[int] = Field(
            description=f"Student services expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Student Services' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Student Services Total'). "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Labels include: 'Student Services', 'Student Affairs', 'Student Support', 'Student Life'. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        institutional_support: Optional[int] = Field(
            description=f"Institutional support expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Institutional Support' / 'Management and General' / 'Administration' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit total). "
                        "If 'Fundraising' appears as a separate category, include it in this total. "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        public_service_expense: Optional[int] = Field(
            description=f"Public service expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Public Service' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit 'Public Service Total'). "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Labels include: 'Public Service', 'Community Service', 'Extension Services', 'Public Programs'. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        student_aid_expense: Optional[int] = Field(
            description=f"Student aid expenses WITHOUT donor restrictions for {fy_label}. "
                        "MANDATORY: Extract ONLY from the detailed Functional Expenses Note. "
                        "Locate 'Student Aid' / 'Scholarships and Fellowships' / 'Student Financial Aid' and extract the TOTAL amount "
                        "(bottom of column / rightmost value in row / explicit total). "
                        "If NO functional table exists, then extract from the operating expenses section of the Statement of Activities. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        total_operating_expense: Optional[int] = Field(
            description=f"Total operating expenses WITHOUT donor restrictions for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "Look for explicit total line items such as: 'Total Operating Expenses', 'Total Operating Expense', 'Total Expenses'. "
                        "VALIDATION: If both a Statement of Functional Expenses and Statement of Activities exist, "
                        "the amount should be identical in both statements; use as a cross-check. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        net_operating_income: Optional[int] = Field(
            description=f"Net operating income (operating revenues minus operating expenses) WITHOUT donor restrictions for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "Look for labels including: 'Change in Net Assets from Operations', 'Operating Income', "
                        "'Net Operating Income', 'Operating Surplus/Deficit'. "
                        "Should equal total_operating_revenue minus total_operating_expense. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        operation_maintenance_expense: Optional[int] = Field(
            description=f"Operation and maintenance of plant expenses WITHOUT donor restrictions for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "Look for labels including: 'Operation and Maintenance of Plant', 'Facilities Operations', "
                        "'Plant Operations', 'O&M'. "
                        "Costs to operate and maintain physical plant including utilities, repairs, custodial services. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        depreciation_amortization_expense: Optional[int] = Field(
            description=f"Depreciation and amortization expenses WITHOUT donor restrictions for {fy_label}. "
                        "EXTRACTION PRIORITY: "
                        "1) If Statement of Functional Expenses exists, extract 'Depreciation' from the TOTAL/bottom line of that statement; "
                        "2) If not, search NOTES for functional breakdown TABLES and extract 'Depreciation' total; "
                        "3) Otherwise extract from operating expenses section of Statement of Activities. "
                        "Look for: 'Depreciation and Amortization', 'Depreciation', 'Amortization', 'Depreciation Expense'. "
                        "Non-cash allocation of asset costs over useful lives. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )

        interest_expense: Optional[int] = Field(
            description=f"Interest expenses WITHOUT donor restrictions for {fy_label}. "
                        "Extract ONLY from financial statement tables and from the 'Without Donor Restrictions' column. "
                        "Look for labels including: 'Interest Expense', 'Interest on Debt', 'Debt Service Interest', 'Interest on Indebtedness'. "
                        "Interest payments on institutional debt and borrowings. "
                        "Extract the raw numeric value only – ignore formatting symbols."
        )


# =============================================================================
# NON-OPERATING: REALIZED INVESTMENT RESULTS
# =============================================================================

        # non_op_realized_investment_net_with_donor: Optional[int] = Field(
        #     description=f"Non–operating REALIZED investment result WITH donor restrictions for {{fy_label}}. "
        #                 "Extract ONLY from the primary Statement of Activities/Operations table; "
        #                 "IGNORE Notes/MD&A/liquidity/supplementary schedules. "
        #                 "Use ONLY the current-year 'With Donor Restrictions' column (not prior years, not 'Total'). "
        #                 "Primary target row (case-insensitive; allow punctuation/spacing variants): "
        #                 "'Investment return above/(in deficit to) amounts designated for current operations'. "
        #                 "If that row exists, use it directly. "
        #                 "Otherwise, capture clearly labeled non-operating realized investment rows (same patterns as WITHOUT donor). "
        #                 "EXCLUDE unrealized amounts, combined realized+unrealized totals, operating investment income, appropriations, "
        #                 "grants, transfers, reclassifications, and non-investment items. "
        #                 "If both component lines and a realized-only non-operating subtotal exist, use the subtotal only. "
        #                 "Preserve sign (parentheses = negative). "
        #                 "Respect scale headings (e.g., 'in thousands'). "
        #                 "Extract the raw numeric value only."
        # )

        non_op_realized_investment_net_with_donor: Optional[int] = Field(
            description=f"NON-OPERATING REALIZED investment result WITH donor restrictions for {fy_label}. "
                        "Definition: realized gains or losses from investment activities that are restricted by donors, "
                        "reported in the 'With Donor Restrictions' column of the primary Statement of Activities / Operations. "
                        "Represents the realized portion of total investment return related to restricted endowments, "
                        "excluding operating investment income and unrealized appreciation. "
                        "Typical labels include (case-insensitive): "
                        "  - 'Investment return above (in deficit to) amounts designated for current operations' "
                        "  - 'Non-operating realized investment return (with donor restrictions)' "
                        "  - 'Net realized gains (losses) — with donor restrictions' "
                        "  - 'Endowment return above spending distribution' "
                        "Primary extraction source: Statement of Activities / Operations, current-year 'With Donor Restrictions' column only. "
                        "IGNORE Notes, MD&A, liquidity disclosures, and supplementary schedules. "
                        "EXCLUDE unrealized gains/losses, combined realized+unrealized totals, operating investment income, appropriations, grants, or transfers. "
                        "If both component lines (realized gain and loss) and a subtotal exist, use the subtotal only. "
                        "When explicitly labeled totals exist (e.g., 'Total realized investment income (with donor restrictions)'), "
                        "prefer the subtotal rather than reconstructing it. "
                        "Maintain sign conventions (parentheses = negative) and respect scale indicators (e.g., 'in thousands'). "
                        "Return the raw numeric value only."
        )

        # non_op_realized_investment_net_without_donor: Optional[int] = Field(
        #     description=f"NET REALIZED investment activity under the Non–Operating section for {{fy_label}} from the "
        #                 "current-year 'Without Donor Restrictions' column. "
        #                 "Extract ONLY from the primary Statement of Activities/Operations table. "
        #                 "Include ALL non-operating rows that clearly relate to realized investment results (preserve signs). "
        #                 "Preferred pattern: if a block titled 'Net Investment Appreciation Less Return' appears, compute "
        #                 "NET_REALIZED = 'Designated for Current Operations' + 'Allocation of Endowment Income to Operations'. "
        #                 "If separate realized gain and loss lines exist, sum them with signs. "
        #                 "If a clearly labeled realized-only non-operating subtotal exists, use that subtotal instead of components. "
        #                 "EXCLUDE unrealized amounts, combined realized+unrealized totals, operating investment income, appropriations, "
        #                 "grants, transfers, reclassifications, and non-investment items. "
        #                 "Label hints (case-insensitive): 'Investment', 'Realized', 'Net Realized Gains (Losses) — Nonoperating', "
        #                 "'Net Investment Appreciation Less Return', 'Designated for Current Operations', "
        #                 "'Allocation of Endowment Income to Operations'. "
        #                 "Preserve sign (parentheses = negative). "
        #                 "Respect scale headings (e.g., 'in thousands'). "
        #                 "Extract the raw numeric value only."
        # )

        non_op_realized_investment_net_without_donor: Optional[int] = Field(
            description=f"NET REALIZED non-operating investment activity WITHOUT donor restrictions (WDR) for {fy_label}. "
                        "Definition: realized investment income, gains, or losses that occur in the non-operating section of the Statement of Activities, "
                        "excluding the portion appropriated for operations. "
                        "Reflects the realized component of total investment return for the unrestricted portion of the endowment and other investment pools. "
                        "Primary source: current-year 'Without Donor Restrictions' column of the Statement of Activities / Operations table. "
                        "Include all clearly labeled non-operating realized investment lines (e.g., 'Realized investment gain/loss — non-operating', "
                        "'Net realized gains (losses) — Without donor restrictions'). "
                        "Preferred extraction pattern: if a subtotal block titled 'Net Investment Appreciation Less Return' or similar appears, compute: "
                        "  NET_REALIZED = 'Designated for Current Operations' + 'Allocation of Endowment Income to Operations' (if both present). "
                        "Related terminology: 'Investment return', 'Endowment distribution', 'Amounts distributed for spending', 'Other investment income'. "
                        "Conceptually, total investment income equals: "
                        "  (Endowment investment return + Other investment income), "
                        "and the operating portion equals: "
                        "  (Endowment distribution to operations + Other investment income (operating)). "
                        "Thus, the non-operating realized component may be derived as: "
                        "  (Total WDR investment return − Endowment distribution for spending), "
                        "when explicit non-operating lines are missing but component structure is evident. "
                        "EXCLUDE unrealized changes, reclassifications, transfers, and operating amounts. "
                        "If separate realized gain and realized loss lines exist, sum with proper signs. "
                        "Use subtotal if clearly labeled 'realized only'. "
                        "Maintain sign conventions (parentheses = negative) and respect scale headings. "
                        "Return the raw numeric value only."
        )

        # =============================================================================
        # OTHER NON-OPERATING / SPECIAL ITEMS
        # =============================================================================

        extraordinary_gain_or_loss: Optional[int] = Field(
            description=f"Extraordinary or unusual gains/losses WITHOUT donor restrictions for {{fy_label}}. "
                        "Extract from the 'Without Donor Restrictions' column if multiple columns exist. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, MD&A, or explanatory paragraphs. "
                        "Look for labels such as: 'Extraordinary Items', 'Unusual Gains/Losses', 'Gain/Loss on Disposal', "
                        "'Non-recurring Items'. "
                        "Include one-time, unusual, or non-recurring gains/losses including asset disposals. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        net_assets_released_for_capital: Optional[int] = Field(
            description=f"Net assets released from restrictions for CAPITAL purposes for {{fy_label}}. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, MD&A, or supplementary schedules. "
                        "Look for labels including: 'Net Assets Released for Capital', 'Released for Capital Purposes', "
                        "'Capital Releases'. "
                        "Represents restricted funds released for capital projects/asset acquisitions. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        change_fair_value_derivatives: Optional[int] = Field(
            description=f"Change in fair value of financial derivative instruments WITHOUT donor restrictions for {{fy_label}}. "
                        "Extract from the 'Without Donor Restrictions' column if multiple columns exist. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, MD&A, or explanatory paragraphs. "
                        "Look for labels including: 'Swap Contract Gain', 'Change in Fair Value of Derivatives', "
                        "'Derivative Gains/Losses', 'Fair Value Adjustments'. "
                        "Typically UNREALIZED gains/losses on derivative instruments. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        capital_grants_gifts: Optional[int] = Field(
            description=f"Capital grants and gifts WITHOUT donor restrictions for {{fy_label}}. "
                        "Extract from the 'Without Donor Restrictions' column if multiple columns exist. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, MD&A, or supplementary schedules. "
                        "Look for labels including: 'Capital Grants and Gifts', 'Capital Contributions', 'Gifts for Capital', "
                        "'Capital Additions'. "
                        "Represents grants/donations designated for capital projects and asset acquisitions. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        # =============================================================================
        # CHANGES IN NET ASSETS
        # =============================================================================

        change_net_assets_without_donor_restrictions: Optional[int] = Field(
            description=f"Change in net assets WITHOUT donor restrictions for {{fy_label}}. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, or MD&A. "
                        "Look for labels including: 'Change in Net Assets Without Donor Restrictions', "
                        "'Change in Unrestricted Net Assets', 'Unrestricted — Change'. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        change_net_assets_with_donor_restrictions: Optional[int] = Field(
            description=f"Change in net assets WITH donor restrictions for {{fy_label}}. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "DO NOT extract from narrative text, footnotes, or MD&A. "
                        "Look for labels including: 'Change in Net Assets With Donor Restrictions', "
                        "'Change in Restricted Net Assets', 'Restricted — Change'. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )

        total_change_in_net_assets: Optional[int] = Field(
            description=f"TOTAL change in net assets for {{fy_label}}. "
                        "EXTRACT ONLY from financial statement tables (Statement of Activities; Statement of Changes in Net Assets). "
                        "Prefer explicit totals such as: 'Total Change in Net Assets', 'Change in Net Assets — Total', "
                        "'Net Assets — Total Change'. "
                        "If no explicit total exists, compute: "
                        "change_net_assets_without_donor_restrictions + change_net_assets_with_donor_restrictions. "
                        "Represents the bottom-line change in net assets for the fiscal year. "
                        "Preserve sign and respect scale headings. "
                        "Extract the raw numeric value only."
        )






    @model_validator(mode="after")
    def validate_consistency(self):
        """Validate logical consistency between related fields with detailed warnings"""
        tolerance = 1000  # Allow $1,000 tolerance for rounding differences

        # Check tuition consistency
        if (self.gross_tuition_revenue is not None and 
            self.financial_aid is not None and 
            self.net_tuition_revenue is not None):
            expected_net = self.gross_tuition_revenue - self.financial_aid
            if abs(expected_net - self.net_tuition_revenue) > tolerance:
                print(f"⚠️  TUITION INCONSISTENCY:")
                print(f"   Expected Net Tuition: ${expected_net:,} (Gross ${self.gross_tuition_revenue:,} - Aid ${self.financial_aid:,})")
                print(f"   Actual Net Tuition: ${self.net_tuition_revenue:,}")
                print(f"   Difference: ${abs(expected_net - self.net_tuition_revenue):,}")

        # Check government grants total consistency
        if (self.government_grants_contracts_total is not None and 
            self.federal_grants_contracts is not None and 
            self.state_local_grants_contracts is not None):
            expected_total = self.federal_grants_contracts + self.state_local_grants_contracts
            if abs(expected_total - self.government_grants_contracts_total) > tolerance:
                print(f"⚠️  GOVERNMENT GRANTS INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,} (Federal ${self.federal_grants_contracts:,} + State/Local ${self.state_local_grants_contracts:,})")
                print(f"   Actual Total: ${self.government_grants_contracts_total:,}")
                print(f"   Difference: ${abs(expected_total - self.government_grants_contracts_total):,}")

        # Check total gifts consistency
        if (self.government_grants_contracts_total is not None and 
            self.state_appropriations is not None and 
            self.private_gifts_grants_contracts is not None and 
            self.total_gifts_contracts_other_support is not None):
            expected_total = (self.government_grants_contracts_total + 
                            self.state_appropriations + 
                            self.private_gifts_grants_contracts)
            if abs(expected_total - self.total_gifts_contracts_other_support) > tolerance:
                print(f"⚠️  TOTAL GIFTS/GRANTS INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,}")
                print(f"   - Government Grants: ${self.government_grants_contracts_total:,}")
                print(f"   - State Appropriations: ${self.state_appropriations:,}")
                print(f"   - Private Gifts: ${self.private_gifts_grants_contracts:,}")
                print(f"   Actual Total: ${self.total_gifts_contracts_other_support:,}")
                print(f"   Difference: ${abs(expected_total - self.total_gifts_contracts_other_support):,}")

        # Check operating income consistency
        if (self.total_operating_revenue is not None and 
            self.total_operating_expense is not None and 
            self.net_operating_income is not None):
            expected_income = self.total_operating_revenue - self.total_operating_expense
            if abs(expected_income - self.net_operating_income) > tolerance:
                print(f"⚠️  OPERATING INCOME INCONSISTENCY:")
                print(f"   Expected Income: ${expected_income:,} (Revenue ${self.total_operating_revenue:,} - Expenses ${self.total_operating_expense:,})")
                print(f"   Actual Income: ${self.net_operating_income:,}")
                print(f"   Difference: ${abs(expected_income - self.net_operating_income):,}")

        # Check instruction and research consistency
        if (self.instructional_expense is not None and 
            self.research_expense is not None and 
            self.instructional_research_expense is not None):
            expected_combined = self.instructional_expense + self.research_expense
            if abs(expected_combined - self.instructional_research_expense) > tolerance:
                print(f"⚠️  INSTRUCTION + RESEARCH INCONSISTENCY:")
                print(f"   Expected Combined: ${expected_combined:,} (Instruction ${self.instructional_expense:,} + Research ${self.research_expense:,})")
                print(f"   Actual Combined: ${self.instructional_research_expense:,}")
                print(f"   Difference: ${abs(expected_combined - self.instructional_research_expense):,}")

        # Check total net assets change consistency
        if (self.change_net_assets_without_donor_restrictions is not None and 
            self.change_net_assets_with_donor_restrictions is not None and 
            self.total_change_in_net_assets is not None):
            expected_total = (self.change_net_assets_without_donor_restrictions + 
                            self.change_net_assets_with_donor_restrictions)
            if abs(expected_total - self.total_change_in_net_assets) > tolerance:
                print(f"⚠️  NET ASSETS CHANGE INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,}")
                print(f"   - Without Restrictions: ${self.change_net_assets_without_donor_restrictions:,}")
                print(f"   - With Restrictions: ${self.change_net_assets_with_donor_restrictions:,}")
                print(f"   Actual Total: ${self.total_change_in_net_assets:,}")
                print(f"   Difference: ${abs(expected_total - self.total_change_in_net_assets):,}")

        # Check investment income consistency if both operating and total are available
        if (self.investment_income_total is not None and 
            self.investment_income_operations is not None):
            non_operating_amount = self.investment_income_total - self.investment_income_operations
            if abs(non_operating_amount) > tolerance:
                if non_operating_amount > 0:
                    print(f"ℹ️  INVESTMENT INCOME ALLOCATION:")
                    print(f"   Total Investment Income: ${self.investment_income_total:,}")
                    print(f"   Operating Portion: ${self.investment_income_operations:,}")
                    print(f"   Non-Operating Portion: ${non_operating_amount:,}")
                else:
                    print(f"⚠️  UNUSUAL INVESTMENT ALLOCATION:")
                    print(f"   Operating investment income (${self.investment_income_operations:,}) exceeds total (${self.investment_income_total:,})")

        return self
    return IncomeStatement