from pydantic import BaseModel, Field
from typing import Optional, Type

from pydantic import BaseModel, Field
from typing import Optional, Type

def make_StatementOfFinancialPosition_model(year: int) -> Type[BaseModel]:
    """
    Dynamically constructs and returns a Pydantic model class named
    'StatementOfFinancialPosition_{year}', whose Field descriptions
    all mention the given year and explicitly instruct to focus only
    on the full Statement of Financial Position (Balance Sheet). Do not
    look at any condensed or net presentations, and do not perform any
    calculations—just capture the numbers exactly as they appear.
    """

    y_str = str(year)
    date_label = f"as of June 30, {year}"

    base_instruction_bs_notes = (
        f"Prefer extracting from the page with header 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
        "If the amount is not explicitly listed there, you may extract it from accompanying 'Notes to Financial Statements' (or 'Notes to Consolidated Financial Statements'), or footnotes. "
        "Do not extract from the page with header 'Cash Flow Statement' or the 'Statement of Cash Flows'."
    )

    base_instruction = (
        f"Only extract from the full 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}; "
        f"do not use condensed or net financial position tables. "
    )

    base_instruction_only_bs = (
        f"Extract ONLY from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
        f"Do NOT extract this information from any page or section with headings such as 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, or 'Footnotes'."
        f"MANDATORY: SKIP information from any page or section if the page or any nearby page contains headings or labels like "
        f"'Note X' (where X is a number) or 'X.' (where X is a numbered note reference); you must leave the field blank and do not use that information. "
        f"Only rely on the face of the balance sheet itself."
    )

    base_instruction_only_notes = (
        f"Extract ONLY from the page or section with a heading such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, or Footnotes. "
        f"Do not extract this information from any page or section with headings such as 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, or 'Statement of Functional Expenses' {year}, 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}."
    )

    base_leave_blank = (
        "Leave the value blank if no match keywords in the mentioned documents."
    )

    base_nocalc = (
        "Do not perform any calculations—capture the number exactly as shown. "
    )

    fields = {
    # =============================================================
    # ============ ***** Cash & Cash Equiv ***** ==================
    # =============================================================
    "cash_and_short_term_investments_unrestricted": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs
              +f"Sum the amounts from asset line items in the 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} that include keywords like 'Cash and cash equivalents' or 'Short-term investments'."
              +f"For cash, include both restricted and unrestricted cash (could be labeled 'Cash whose use is limited'). For non-cash assets, include unrestricted investments only. For example, do not include 'limited use assets'."
              +f"Do NOT include 'Deposit with Trustee'"
              ))
    ),
    "cash_and_short_term_investments_restricted": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs
              +f"Sum the amounts from asset line items in the 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} that include keywords like 'Cash and cash equivalents' or 'Short-term investments'."
              +f"For cash, include both restricted and unrestricted cash (could be labeled 'Cash whose use is limited'). For non-cash assets, include unrestricted investments only. For example, do not include 'limited use assets'."
              +f"Do NOT include 'Deposit with Trustee'"
              ))
    ),

    # =============================================================
    # ================= ***** Receivables ***** ===================
    # =============================================================
    "accounts_receivable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs 
            + f"Match labels: 'Accounts receivable', 'Student accounts receivable', 'Trade receivables'. If multiple, use the most general line item. Exclude pledges, loans, and grants."
            + base_leave_blank))
    ),
    "pledges_receivable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs 
            + f"Match labels: 'Pledges receivable', 'Contributions receivable'. Priority: if both appear, prefer 'Pledges'." 
            + base_leave_blank))
    ),
    "government_grants_and_other_receivables": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs 
            + f"Match labels: 'Government grants receivable', 'Other receivables'. MUST contain the word 'receivable'. Do not include loans or pledges."
            + f"If found item is in 'Notes to Financial Statements', ignore it."
            + base_leave_blank))
    ),
    "loans_receivable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs 
            + f"Match labels: 'Loans receivable', 'Student loans receivable', 'Long-term loans to students'. MUST contain 'receivable'."
            + base_leave_blank))
    ),
    "all_receivables": (
        Optional[int],
        Field(
            None,
            description=(base_instruction_only_bs +
            f"Extract the total amount of all asset line items that contain the word 'receivable' in the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + f"Include any of the following if they appear as separate lines within the 'Assets' section of the 'Statement of Financial Position':"
              f"'Accounts receivable','Accounts and notes receivable, net', 'Student accounts receivable', 'Student loans receivable', 'Pledges receivable', 'Contributions receivable', 'Grants and contracts receivable', 'Government grants and other receivables', 'Interest receivable', or other similar items explicitly containing the word 'receivable' or 'receivables' or 'receivable, net'. "
              f"Include 'Contributions receivable'."
              f"Include both current and non-current receivables."
              f"The extraction scope should begin after the heading 'Assets' and end at 'Total assets' or 'Liabilities and Net Assets'. Sum all qualifying amounts to get "
              f"the total receivables balance for the institution. "
            + base_leave_blank
        )) 
    ),

    # =============================================================
    # ============ Accumulated Depreciation 4 items ===============
    # =============================================================
    "accumulated_depreciation_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + 
            f"Extract the value labeled 'Total accumulated depreciation', 'accumulated depreciation'. "
            # + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "accumulated_amortization_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"Extract the value labeled 'Total accumulated amortization' or 'accumulated amortization'. "
            # + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "accumulated_depreciation_notes": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes
                + f"In the page or section with a heading such as 'Notes to Financial Statements' or "
                f"'Notes to Consolidated Financial Statements' {year} that describes 'Property, Plant, and Equipment' "
                f"or 'Plant Assets', extract all line items labeled 'Accumulated Depreciation' or any line beginning with 'Less accumulated depreciation'. "
                f"Include the total accumulated depreciation amount even if it appears in parentheses or is shown as a negative number. "
                f"Sum all 'Accumulated Depreciation' values across asset categories (e.g., 'Buildings', 'Equipment', 'Library Books') and return the combined total as a positive integer. "
                f"Do not extract any net asset values (e.g., 'Plant assets, net') or unrelated notes. "
                + base_leave_blank
            ),
        ),
    ),
    "accumulated_amortization_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes +
            f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year} related to leases, extract the value labeled 'Total accumulated amortization'. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============ ROU Finance Lease Assets 2 items ===============
    # =============================================================
    "rou_assets_finance_lease_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"Extract the amount from asset line items labeled with terms like 'Finance leases', 'Right of Use Assets – Finance Leases', 'ROU Assets – Finance Leases', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "rou_assets_finance_lease_notes": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes
                + f"Locate the breakdown of 'Land, Buildings, and Equipment' (or similar PP&E note). "
                f"Extract the amount reported for items labeled with terms such as "
                f"'Finance leases', 'Right of Use Assets – Finance Leases', 'ROU – Finance Leases', or similar wording. "
                f"Some institutions report this as a separate line alongside 'Land', 'Buildings', 'Equipment', or 'Construction in progress'. "
                f"Extract the balance as presented (gross or net, depending on the table format). "
                f"Do not confuse with operating lease ROU assets, which are disclosed separately. "
                f"Do not extract from high-level balance sheets or summary tables. "
                + base_leave_blank
            ),
        ),
    ),

    # =============================================================
    # ============ ***** Net Fixed Assests ***** ==================
    # =============================================================
    "net_fixed_assets_raw": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, sum the amounts of asset line items related to long-term physical assets, including keywords like 'Land', 'Buildings', 'Equipment', 'Property', or 'Plant'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ======== ***** ROU Operating Lease Assets  ***** ============
    # =============================================================
    "rou_assets_operating_lease_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount from asset line items labeled with terms like 'Right of Use Assets – Operating Leases', 'ROU Assets – Operating Leases', 'lease right-of-use assets, net', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "rou_assets_operating_lease_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the amount of items labeled with terms like 'Right of Use Assets – Operating Leases', 'ROU Assets – Operating Leases', 'Lease right-of-use assets, net', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============ ***** Long-term Investments ***** ==============
    # =============================================================
    "long_term_investments": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Long-term investments', 'Investments', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + f"Do not perform any calculations — capture the number exactly as shown. "
            + base_leave_blank
        ))
    ),
    "cash_surrender_value_life_insurance": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"Extract the amount labeled 'Cash surrender value of donated life insurance policy' or a similar term. Only extract values from a page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    # =============================================================
    # ================= TOTAL Assets ==============================
    # =============================================================
    "total_assets": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + 
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the value labeled 'Total Assets {year}'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============== ***** Short-term Debts ***** =================
    # =============================================================
    "short_term_debt": (
        Optional[int],
        Field(None, description=(base_instruction + base_nocalc +
            f"Short-Term Debt {year} or obligations due on demand or within 12 months. Example includes 'commercial paper', 'loans payable', 'Outstanding checks in excess of bank balance' or similar."
            # + f"Skip the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}."
            # + f"Look for 'Debt and Other Obligations' or similar note sections from page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============== ***** Accounts Payable ***** =================
    # =============================================================
    "accounts_payable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount for 'Accounts Payable'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============== ***** Deferred Revenues ***** ================
    # =============================================================
    "all_deferred_revenue": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_bs
                + f"Extract the total amount of deferred revenue and similar liabilities. "
                f"Include any line items labeled or described as 'Deferred revenue', 'Unearned revenue', 'Deferred tuition revenue', 'Student tuition and other deposits', "
                f"'Student deposits', 'Student credit balances and deposits', 'Sponsored program advances', or any other equivalent terms indicating payments received "
                f"in advance of providing goods or services. "
                f"Sum both short-term and long-term deferred revenue amounts if they appear separately. "
                f"Exclude unrelated liabilities such as 'Accounts payable', 'Accrued expenses', or 'Deposits with trustee'. "
                + base_leave_blank
            ),
        ),
    ),
    "def_rev_mixed": (
        Optional[int],
        Field(None, description=(
                base_instruction_only_bs
              +f"Locate the liability line item labeled 'Deferred revenue', 'Deferred revenue and deposits', or any similar term. "
              f"If the label includes additional components such as 'deposits', 'obligations', 'advances', or any other combined category, return the value 1. "
              f"If the line item represents deferred revenue only (no other descriptors), return the value 0. "
              f"This field is an indicator and should not contain the deferred revenue amount itself."
            ),
        ),
    ),
    "asset_retirement_obligations": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes
                + f"Extract the amount labeled 'Asset retirement obligations', 'ARO', or other similar terms "
                f"from the notes to the financial statements {year}, if the notes explicitly mention that certain deposits or liabilities are included as part of deferred revenue, include those amounts as well. "
                f"Do not extract unrelated liabilities such as pension obligations unless they are explicitly described as part of the deferred revenue disclosure. "
                + base_leave_blank
            ),
        ),
    ),

    # =============================================================
    # ================= Finance Lease Liability ===================
    # =============================================================
    "finance_lease_liability_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the total amount of lines labeled 'Finance Lease liabilities' or 'Finance Lease obligations' or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + f"Do not extract from text."
            + base_leave_blank
        ))
    ),
    "finance_lease_liability_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the total amount of lines labeled 'Finance Lease liabilities' or 'Finance Lease obligations' or similar. "
            + f"search for a table shows 'Present value of lease liabilities' or detailed lease payment schedules. "
            + f"Extract the amount of lease obligations for finance leases."
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + f"Do not extract from text."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # =============== ***** Long-Term Debt ***** ==================
    # =============================================================
    "long_term_debt_labeled": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_bs
                + f"Extract the amount corresponding to all long-term borrowing obligations in the "
                f"'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
                f"This includes any line labeled 'Long-term debt', 'Notes payable', 'Bonds payable', "
                f"'Long-term borrowings', 'Mortgage payable', or other similar terms that clearly represent long-term financing obligations. "
                f"Include both secured and unsecured debt if presented together. "
                f"If multiple long-term debt categories appear (e.g., 'Bonds payable' and 'Notes payable'), "
                f"sum their amounts. Do not include current portions of long-term debt (those due within one year) or short-term borrowings. "
                + base_leave_blank
            ),
        ),
    ),
    "other_long_term_debt_obligations": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract amounts labeled with other terms that clearly indicate long-term borrowing or financing obligations (excluding lease liabilities). "
            "Examples may include 'Notes payable', 'Term loans', or other long-term financial obligations not already captured in 'Long-Term Debt' or 'Bonds payable'. "
            "Leave blank if only umbrella 'Long-term debt' is shown. "
            + base_leave_blank
        ))
    ),

    "backup_total_long_term_debt": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_bs
                + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} "
                f"or 'Statement of Financial Position' {year}, locate the line labeled 'Debt and other obligations' or 'Long term debt, net'"
                f"(or substantially similar wording), which is a total amount. Extract this total. "
                f"Do not confuse with lease liabilities or accrued benefit obligations. "
                + base_leave_blank
            ),
        ),
    ),

    # =============================================================
    # ========= ***** Operating Lease Liability ***** =============
    # =============================================================
    "operating_lease_liability_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the total amount of 'Operating Lease liabilities' or 'Operating Lease obligations' or similar in noncurrent and current liability. "
            + base_leave_blank
        ))
    ),
    "operating_lease_liability_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the total amount of lines labeled 'Operating Lease liabilities' or 'Operating Lease obligations' or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ============== ***** Pension and OPEB ***** =================
    # =============================================================
    "pension_liability": (
        Optional[int],
        Field(None, description=(
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, leave empty if none of keywords is like 'Pension Liability'."
            + base_instruction_only_bs 
            + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year},"
            + f"Do NOT extract from Notes or Revenues. "
            + f"Match labels: 'Pension liability', 'Pension obligations', 'Post-retirement and pension obligations', 'Defined benefit pension plan obligation', 'Retirement obligations' for {year}."
            + base_leave_blank
        ))
    ),

    "opeb_liability": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'OPEB Liability'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),

    "pension_and_opeb_liability": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Pension & OPEB Liability'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    # =============================================================
    # ========================== MISC =============================
    # =============================================================
    "year": (
        int,
        Field(..., description=base_instruction + f"The fiscal year for all line‐items: {year}.")
    ),

    "current_portion_finance_lease": (
        Optional[int],
        Field(None, description=base_instruction + f"Current Portion of Finance Lease {date_label}.")
    ),
    "current_portion_long_term_debt": (
        Optional[int],
        Field(None, description=base_instruction + f"Current Portion of Long-Term Debt {date_label}.")
    ),
    "current_portion_operating_lease": (
        Optional[int],
        Field(None, description=base_instruction + f"Current Portion of Operating Lease {date_label}.")
    ),

    "swap_obligation_fmv": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount for Swap Obligation (FMV). "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),

    # =============================================================
    # ================= Total Liability ===========================
    # =============================================================
    "total_liabilities": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Total Liabilities {year}.")
    ),

    # =============================================================
    # ====================== Net Assets ===========================
    # =============================================================

    "net_assets_without_donor_restrictions": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Net Assets without Donor Restrictions {year}.")
    ),

    "perpetual_net_assets_with_donor_restrictions": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes
                + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, "
                f"extract the total for perpetual net assets with donor restrictions. "
                f"This corresponds to investment in perpetuity where only the income is available to support activities (e.g., scholarships, annuities, research/academic support, property/equipment). "
                f"Return the summed amount as an integer. "
                f"Do not extract this information from balance sheets or summary tables. "
                + base_leave_blank
            ),
        ),
    ),
    "net_assets_with_donor_restrictions": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Total Net Assets with Donor Restrictions {year}.")
    ),
    "noncontrolling_interest": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Noncontrolling Interest {year}.")
    ),
    "total_net_assets": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Total Net Assets {year}.")
    ),
    "total_liabilities_and_net_assets": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Total Liabilities & Net Assets {year}.")
    ),

    "units_multiplier": (
        Optional[int],
        Field(
            None,
            description=(
                "Extract the **numeric multiplier** that applies to values in the full Statement of Financial Position "
                f"{year}. Return:\n"
                "- 1000 if values are labeled as 'in thousands'\n"
                "- 1000000 if labeled as 'in millions'\n"
                "- 1 if no multiplier is stated (i.e., raw dollar amounts or just 'USD').\n"
                "This is an exception: it may be found in headers or footnotes."
            )
        )
    ),
    # "contribution_type": (
    #     Optional[str],
    #     Field(
    #         None,
    #         description=(
    #             base_instruction_only_notes +
    #             f"In the page or section with a heading such as 'Notes to Financial Statements', 'Notes to Consolidated Financial Statements' {year}, or Footnotes, "
    #             "identify whether the institution participates in a **Defined Benefit Plan**, a **Defined Contribution Plan**, or **both**. "
    #             "Look specifically in sections with titles such as:\n"
    #             "- 'Employee Retirement Benefits'\n"
    #             "- 'Retirement Plan'\n"
    #             "- 'Deferred Benefits'\n"
    #             "- 'Pension and Postretirement Plans'\n"
    #             "- 'Employee Benefit Plans'\n\n"
    #             "Search the content in those sections for keywords or phrases like 'defined benefit', 'defined contribution', '403(b)', '401(k)', or 'multiemployer pension plan'. "
    #             "Return one of the following values exactly:\n"
    #             "- `'defined benefit'`\n"
    #             "- `'defined contribution'`\n"
    #             "- `'both'`\n\n"
    #             "Do not infer from unrelated sections. Leave the field blank if none of the expected terms are found."
    #         )
    #     )
    # )
    }

    class_name = f"StatementOfFinancialPosition_{year}"
    namespace = {"__annotations__": {k: t for k, (t, _) in fields.items()}}
    for field_name, (_, field_def) in fields.items():
        namespace[field_name] = field_def

    return type(class_name, (BaseModel,), namespace)


