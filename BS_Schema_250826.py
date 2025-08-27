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
        "do not use condensed or net financial position tables. "
    )

    base_instruction_only_bs = (
        f"Extract **only** from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
        f"Do not extract this information from any page or section with headings such as 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, or 'Footnotes'."
    )

    base_instruction_only_notes = (
        f"Extract **only** from the page or section with a heading such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, or Footnotes. "
        f"Do not extract this information from any page or section with headings such as 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, or 'Statement of Functional Expenses' {year}."
    )

    base_leave_blank = (
        "Leave the value blank is no match keywords in the mentioned documents."
    )

    base_nocalc = (
        "Do not perform any calculations—capture the number exactly as shown. "
    )

    fields = {
    "cash_and_short_term_investments_unrestricted_and_restricted": (
        Optional[int],
        Field(None, description=base_instruction_only_bs + f"Sum the amounts from asset line items in the 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} that include keywords like 'Cash and cash equivalents' or 'Short-term investments'. Include both unrestricted and restricted components.")
    ),
    "accounts_receivable": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} the amount labeled 'Accounts receivable', 'Student accounts receivable', or similar terms." + base_leave_blank))
    ),
    "pledges_receivable": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Pledges receivable', 'Contributions', 'Contributions receivable', or similar terms." + base_leave_blank))
    ),
    "government_grants_and_other_receivables": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} the amount labeled 'Government grants and other receivables' or similar terms." + base_leave_blank))
    ),
    "loans_receivable": (
        Optional[int],
        Field(None, description=(base_instruction_only_bs + f"Extract from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} the amount labeled 'Loans receivable', 'Student loans receivable', 'Grants and other accounts receivable', 'Long-term loans to students', or similar terms." + base_leave_blank))
    ),
    "receivables_leftover": (
        Optional[int],
        Field(
            None,
            description=(base_instruction_only_bs +
                f"Extract the total amount of all asset line items in the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} that contain the word 'receivable' but are not already captured in the following subcategories: "
                "'Accounts receivable', 'Student accounts receivable', 'Pledges receivable', 'Contributions receivable', 'Government grants and other receivables', "
                "'Student loans receivable', 'Loans receivable', 'Grants and other accounts receivable', or 'Long-term loans to students'. "
                "Use this as a fallback or catch-all for any remaining receivable-related line items." +
                base_leave_blank
        ))
    ),
    "all_receivables": (
        Optional[int],
        Field(
            None,
            description=(base_instruction_only_bs +
            f"Extract the total amount of all asset line items in the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year} that contain the word 'receivable'. "
            + base_leave_blank
        ))
    ),
    "accumulated_depreciation_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + 
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the value labeled 'Total accumulated depreciation'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "accumulated_amortization_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the value labeled 'Total accumulated amortization'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "rou_assets_finance_lease_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount from asset line items labeled with terms like 'Right of Use Assets – Finance Leases', 'ROU Assets – Finance Leases', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "net_fixed_assets_raw": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, sum the amounts of asset line items related to long-term physical assets, including keywords like 'Land', 'Buildings', 'Equipment', 'Property', or 'Plant'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "rou_assets_operating_lease_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount from asset line items labeled with terms like 'Right of Use Assets – Operating Leases', 'ROU Assets – Operating Leases', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
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
    "deferred_revenue_raw": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"Extract the amount labeled 'Deferred Revenue' or similar terms. Only extract values from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "student_tuition_and_deposits": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"Extract the amount labeled 'Student tuition and other deposits' or similar terms from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + base_leave_blank
        ))
    ),
    "student_credit_balances_and_deposits": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"Extract the amount labeled 'Student credit balances and deposits' or similar terms from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + base_leave_blank
        ))
    ),
    "finance_lease_liability_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the total amount of lines labeled 'Finance Lease liabilities' or 'Finance Lease obligations' or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "long_term_debt_labeled": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Long-Term Debt' or similar terms. "
            + base_leave_blank
        ))
    ),
    "bonds_payable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Bonds payable' or similar terms. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "other_long_term_debt_obligations": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs +
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract amounts labeled with other terms that clearly indicate long-term borrowing or financing obligations (excluding lease liabilities). "
            "Examples may include 'Notes payable', 'Term loans', or other long-term financial obligations not already captured in 'Long-Term Debt' or 'Bonds payable'. "
            + base_leave_blank
        ))
    ),
    "operating_lease_liability_bs": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the total amount of 'Operating Lease liabilities' or 'Operating Lease obligations' or similar in noncurrent and current liability. "
            + base_leave_blank
        ))
    ),
    # UPDATED
    "pension_liability": (
        Optional[int],
        Field(None, description=(
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, leave empty if none of keywords is like 'Pension Liability'."
            + base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount labeled 'Pension Liability' {year}."
            + f"Take only from the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. Leave empty if none of such keywords in the 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}. "
            + base_leave_blank
        ))
    ),
    "swap_obligation_fmv": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount for Swap Obligation (FMV). "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
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
    "other_liabilities": (
        Optional[int],
        Field(None, description=base_instruction_only_bs + f"Other Liabilities {year}.")
    ),
    "accumulated_depreciation_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + 
            f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year} related to leases, extract the value labeled 'Total accumulated depreciation'. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
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
    "rou_assets_finance_lease_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the **net amount (after subtracting accumulated amortization)** of items labeled with terms like 'Right of Use Assets – Finance Leases', 'ROU Assets – Finance Leases', or similar. This corresponds to the total or net book value, not the gross balance before amortization. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
    ),
    "rou_assets_operating_lease_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the amount of items labeled with terms like 'Right of Use Assets – Operating Leases', 'ROU Assets – Operating Leases', or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
            + base_leave_blank
        ))
    ),
    "finance_lease_liability_notes": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_notes + f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the total amount of lines labeled 'Finance Lease liabilities' or 'Finance Lease obligations' or similar. "
            + f"Do not extract this information from any page or section with headings such as 'Consolidated Balance Sheet' {year}, 'Statement of Financial Position' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}."
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
    "year": (
        int,
        Field(..., description=base_instruction + f"The fiscal year for all line‐items: {year}.")
    ),
    "other_assets": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Other Assets {year}.")
    ),
    "total_assets": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + 
            f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the value labeled 'Total Assets {year}'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "current_portion_finance_lease_raw": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Current Portion of Finance Lease {year}.")
    ),
    "current_portion_finance_lease_notes_due_next_year": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes +
                f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year}, extract the amount of Finance Lease payments due in the year following {year} (i.e., due in {year + 1}). "
                f"Look specifically for finance lease payment schedules or tables where the first year's payment matches {year + 1}. "
                f"This should only be used when no current portion is clearly reported in the 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}."
                + base_leave_blank
            )
        )
    ),
    "current_portion_long_term_debt_raw": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Current Portion of Long-Term Debt {year}.")
    ),
    "current_portion_long_term_debt_notes_due_next_year": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes +
                f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year} or Footnotes, extract the portion of long-term debt (including any 'Bonds Payable') that is scheduled to mature in the year following {year} (i.e., due in {year + 1}) "
                f"Look for debt maturity schedules or payment tables. Use only the amount that corresponds to {year + 1}. "
                f"Include line items labeled 'Long-term debt', 'Debt obligations', or 'Bonds payable'."
                + base_leave_blank
            )
        )
    ),
    "current_portion_operating_lease_raw": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Current Portion of Operating Lease {year}.")
    ),
    "current_portion_operating_lease_notes_due_next_year": (
        Optional[int],
        Field(
            None,
            description=(
                base_instruction_only_notes +
                f"In the page or section with a heading such as 'Notes to Financial Statements' or 'Notes to Consolidated Financial Statements' {year} or Footnotes, extract the amount of 'Operating Lease payments' due in the year following {year} (i.e., due in {year + 1}). "
                f"Look specifically for 'operating lease payment' schedules or tables where the first year's payment matches {year + 1}. "
                f"This should only be used when no current portion is clearly reported in the 'Consolidated Balance Sheet'."
                + base_leave_blank
            )
        )
    ),
    "short_term_debt": (
        Optional[int],
        Field(None, description=(base_instruction + base_nocalc +
            f"Short-Term Debt {year} and include keyword like 'Outstanding checks in excess of bank balance' or similar."
            + base_leave_blank
        ))
    ),
    "accounts_payable": (
        Optional[int],
        Field(None, description=(
            base_instruction_only_bs + f"In the page or section with a heading such as 'Consolidated Balance Sheet' {year} or 'Statement of Financial Position' {year}, extract the amount for 'Accounts Payable'. "
            + f"Do not extract this information from any page or section with headings such as 'Notes to Financial Statements' {year}, 'Notes to Consolidated Financial Statements' {year}, 'Cash Flow Statement' {year}, 'Statement of Cash Flows' {year}, 'Statements of Activities' {year}, 'Statement of Functional Expenses' {year}, or Footnotes."
            + base_leave_blank
        ))
    ),
    "total_liabilities": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Total Liabilities {year}.")
    ),
    "net_assets": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Net Assets {year}.")
    ),
    "net_assets_without_donor_restrictions": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Net Assets without Donor Restrictions {year}.")
    ),
    "expendable_net_assets_with_donor_restrictions": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Expendable Net Assets with Donor Restrictions {year}.")
    ),
    "perpetual_net_assets_with_donor_restrictions": (
        Optional[int],
        Field(None, description=base_instruction + base_nocalc + f"Perpetual Net Assets with Donor Restrictions {year}.")
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
    "contribution_type": (
        Optional[str],
        Field(
            None,
            description=(
                base_instruction_only_notes +
                f"In the page or section with a heading such as 'Notes to Financial Statements', 'Notes to Consolidated Financial Statements' {year}, or Footnotes, "
                "identify whether the institution participates in a **Defined Benefit Plan**, a **Defined Contribution Plan**, or **both**. "
                "Look specifically in sections with titles such as:\n"
                "- 'Employee Retirement Benefits'\n"
                "- 'Retirement Plan'\n"
                "- 'Deferred Benefits'\n"
                "- 'Pension and Postretirement Plans'\n"
                "- 'Employee Benefit Plans'\n\n"
                "Search the content in those sections for keywords or phrases like 'defined benefit', 'defined contribution', '403(b)', '401(k)', or 'multiemployer pension plan'. "
                "Return one of the following values exactly:\n"
                "- `'defined benefit'`\n"
                "- `'defined contribution'`\n"
                "- `'both'`\n\n"
                "Do not infer from unrelated sections. Leave the field blank if none of the expected terms are found."
            )
        )
    )
    }

    class_name = f"StatementOfFinancialPosition_{year}"
    namespace = {"__annotations__": {k: t for k, (t, _) in fields.items()}}
    for field_name, (_, field_def) in fields.items():
        namespace[field_name] = field_def

    return type(class_name, (BaseModel,), namespace)


