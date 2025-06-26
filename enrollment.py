from typing import Optional
from pydantic import BaseModel, Field

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
