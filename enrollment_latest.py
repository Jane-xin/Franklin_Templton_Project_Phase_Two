from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class Enrollment2024_25(BaseModel):
    Year_Headcount: Optional[str] = Field(
        description=(
            "Collect the academic year or term (e.g., '2024–25','Fall 2024', 'AY 2024–2025') associated with the following fields:" 
            "Undergraduate Headcount, Graduate Headcount, Total Headcount, and Total full-time equivalent students (FTE)." 
            "If all of them refer to a year equivalent to 'Fall 2024', such as 'Fall 2024', 'AY 2024–2025','Academic Year 2024–2025', '2024-25', or 'AY 24–25',"
            "then convert it and return only the standardized value '2024–2025'."
            "Use the same equivalence logic for previous years as well,convert 'Fall 2023', 'AY 2023–2024', '2023–24' to'2023–2024'and so on."
            "Always convert when a clearly matching year or term is present." 
            "Do not infer or guess — only convert when the input explicitly matches a known academic year."
        )
    )
    Year_Fee: Optional[str] = Field(
        description=(
            "Collect the academic year or term (e.g.,'2024–25', 'Fall 2024', 'AY 2024–2025') associated with the following fields:" 
            "Tuition, Room & board cost (20-meal plan)." 
            "If all of them refer to a year equivalent to 'Fall 2024', such as 'Fall 2024', 'AY 2024–2025','Academic Year 2024–2025', '2024-25', or 'AY 24–25',"
            "then convert it and return only the standardized value '2024–2025'."
            "Use the same equivalence logic for previous years as well,convert 'Fall 2023', 'AY 2023–2024', '2023–24' to'2023–2024'and so on."
            "Always convert when a clearly matching year or term is present." 
            "Do not infer or guess — only convert when the input explicitly matches a known academic year."
        )
    )
    Year_Undergraduate_Headcount: Optional[str] = Field(
        description=(
            "Extract the academic year or term (e.g., 'Fall 2024', 'AY 2024–2025', '2024–25') that is associated with the Total undergraduate headcount" 
            "for the 2024-2025 academic year (Different than undergraduate FTE). "
            "Do not guess — only extract if both the value and term are shown."
        )
    )

    Undergraduate_Headcount: Optional[int] = Field(
        description=(
            "Total undergraduate headcount for most recent academic year available. "
            "(Different than undergraduate FTE. Sometimes you need to combine both full-time and part time). "
            "Search around the tables to locate what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'Fall 2023', 'AY 2024–25', '2024-25','2023', 'Fall 2023', 'Fall 2022'."
            "it's possible for a school to have multiple campuses, so combine all campuses' count or online and in-person count if applicable. "
            "If it didn't specify what kind of headcount it is, do not assume it's undergraduate headcount!!! "
            "Combine online and in-person if applicable. "
            "look around the table to see what type of data it is. "
            "Do not derive or hallucinate the data unless the field is actually in the document."

        )
    )
    Undergraduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Undergraduate full-time or FT headcount for the most recent academic year available. "
            "This is different from FTE (full-time equivalent). "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Combine across all campuses if the institution has multiple locations. "
            "Don't assume it's undergraduate full-time unless it explicitly says so in the data description. "
            "When there is no specification of what kind of full-time it is, it should be total full-time. "
        )
    )

    Undergraduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Undergraduate part-time (PT) headcount for the most recent academic year available. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Combine across all campuses if the institution has multiple locations. "
            "Don't assume it's undergraduate full-time unless it explicitly says so in the data description. "
            "When there is no specification of what kind of part-time it is, it should be total part-time."
        )
    )


    Year_Graduate_Headcount: Optional[str] = Field(
        description=(
        "Extract the Total graduate headcount for the 2024-2025 academic year and also include the academic year or term" 
        "(e.g., Fall 2024, AY 2024–2025) that this number belongs to."
        " Do not guess — only extract if both the value and term are shown."
        )
    )

    Graduate_Headcount: Optional[int] = Field(
        description=(
            "Total graduate headcount for the most recent academic year available. "
            "Post-baccalaureate is considered a graduate headcount. "
            "(Different than graduate FTE. Sometimes you need to combine both full-time and part-time). "
            "Combine enrollment across all graduate schools (e.g., Business, Education, etc.). "
            "If the graduate headcount includes both professional and graduate headcount, it's fine to include under graduate headcount. "
            "Combine online and in-person if applicable. "
            "Graduate headcount may be labeled as 'GR', 'Grad', or 'Graduate'. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts or online and in-person counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )


    Graduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Graduate full-time (FT) headcount for the most recent academic year available. "
            "Post-baccalaureate is considered a graduate headcount. "
            "This is different from FTE (full-time equivalent). "
            "Combine across all graduate schools. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Combine across campuses if needed. "
            "Don't assume it's graduate full-time unless it explicitly says so in the data description. "
            "When there is no specification of what kind of full-time it is, it should be total full-time. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Graduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Graduate part-time (PT) headcount for the most recent academic year available. "
            "Post-baccalaureate is considered a graduate headcount. "
            "Combine across all graduate schools. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Combine across campuses if needed. "
            "Don't assume it's graduate part-time unless it explicitly says so in the data description. "
            "When there is no specification of what kind of part-time it is, it should be total part-time. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Professional_Headcount: Optional[int] = Field(
        description=(
            "Combined professional school headcount (e.g., medicine, law) for the most recent academic year available. "
            "This is different from professional FTE. Sometimes you need to combine both full-time and part-time. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Non_Degree_Headcount: Optional[int] = Field(
        description=(
            "Non-degree headcount for the most recent academic year available. "
            "This is different from Non-Degree FTE. Sometimes you need to combine both full-time and part-time. "
            "Sometimes, Non-Degree is labeled as Non-Credit. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )


    Year_Total_Headcount: Optional[str] = Field(
        description=(
            "Extract the academic year or term (e.g., 'Fall 2024', 'AY 2024–2025', '2024–25') that is associated with the" 
            "overall student headcount for the 2024-2025 academic year." 
            "Do not guess — only extract if both the value and term are shown."

        )
    )

    Total_Headcount: Optional[int] = Field(
        description=(
            "Overall student headcount for the most recent academic year available. "
            "Do **not** compute it by adding Undergraduate, Graduate, Professional, etc. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Total_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Total full-time headcount for the most recent academic year available across all student categories. "
            "This is different from FTE (full-time equivalent). "
            "If not explicitly provided, sum Undergraduate_Headcount_Full_Time + Graduate_Headcount_Full_Time. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Do **not** derive it by summing individual full-time headcounts unless instructed. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "When there is no specification of what kind of full-time it is, it should be total full-time."
        )
    )

    Total_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Total part-time headcount for the most recent academic year available across all student categories. "
            "If not explicitly provided, sum Undergraduate_Headcount_Part_Time + Graduate_Headcount_Part_Time. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25', '2024-2025','Fall 2023', '2023', etc. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Do **not** derive it by summing individual part-time headcounts unless instructed. "
            "Do not derive or hallucinate the data unless the field is actually in the document. "
            "When there is no specification of what kind of part-time it is, it should be total part-time."
        )
    )

    Undergraduate_FTE: Optional[int] = Field(
        description=(
            "Undergraduate full-time equivalent (FTE) headcount for the most recent academic year available. "
            "FTE (full-time equivalent) is different from full-time or part-time. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Graduate_FTE: Optional[int] = Field(
        description=(
            "Graduate full-time equivalent (FTE) headcount for the most recent academic year available. "
            "Post-baccalaureate is considered a graduate headcount. "
            "FTE (full-time equivalent) is different from full-time. "
            "Combine enrollment across all graduate schools (e.g., Business, Education, etc.). "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Professional_FTE: Optional[int] = Field(
        description=(
            "Professional school full-time equivalent (FTE) headcount for the most recent academic year available. "
            "FTE (full-time equivalent) is different from full-time. "
            "Search around the tables to identify what type of enrollment information it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "It’s possible for a school to have multiple campuses — combine all campuses' counts if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Year_Total_Full_Time_Equivalent_Students: Optional[str] = Field(
        description=(
            "Extract the academic year or term (e.g., 'Fall 2024', 'AY 2024–2025', '2024–25') that is associated with the" 
            "total full-time equivalent headcount or FTE for the 2024-2025 academic year. FTE (full-time equivalent) is different than full-time, or FT.  "
            "Do not guess — only extract if both the value and term are shown."
        )
    )

    Total_Full_Time_Equivalent_Students: Optional[int] = Field(
        description=(
            "Total full-time equivalent (FTE) students for the most recent academic year available. "
            "FTE reflects enrollment intensity, and should not be confused with full-time enrollment. "
            "Search around the tables to identify what type of FTE data it is. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','Academic Year 2024-25','2024-2025','Fall 2023', '2023', etc. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "It’s possible for a school to have multiple campuses — combine across all campuses if applicable. "
            "Do **not** derive it by summing individual FTE fields. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )


    Undergraduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total undergraduate applications received for the most recent applications cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Graduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total graduate applications received for the most recent applications cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Transfer_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total transfer applications received for the most recent applications cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Undergraduate_Acceptances: Optional[int] = Field(
        description=(
            "Total undergraduate acceptances for the most recent admissions cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Graduate_Acceptances: Optional[int] = Field(
        description=(
            "Total graduate acceptances for the most recent admissions cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "If multiple years are present (e.g., '2023–24' and '2024–25'), always choose the one that represents the latest year."
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Transfer_Acceptances: Optional[int] = Field(
        description=(
            "Total transfer acceptances for the most recent admissions cycle. "
            "Search around the tables to identify the application cycle year, such as 'Fall 2024','2024-25','2024-2025,'2023-2024', 'Fall 2023', or '2023'. "
            "If multiple years are present (e.g., '2023–24' and '2024–25'), always choose the one that represents the latest year."
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Undergraduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of undergraduate students who matriculated in the most recent academic year. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Graduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of graduate students who matriculated in the most recent academic year. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Transfer_Matriculants: Optional[int] = Field(
        description=(
            "Number of transfer students who matriculated in the most recent academic year. "
            "Look for the latest academic year or term, such as 'Fall 2024', 'AY 2024–25','2024-25','2024-2025','Fall 2023', '2023', etc. "
            "Ignore older years or terms. "
            "Combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Retention_Rate: Optional[float] = Field(
        description=(
            "Retention rate (%) for the most recent entering cohort (e.g., Fall 2024, Fall 2023). "
            "Search around the tables to identify which cohort year the retention rate applies to. "
            "Ignore data outside this period. "
            "It’s possible for a school to have multiple campuses — combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Full_Time_Employee_Equivalents: Optional[int] = Field(
        description=(
            "Full-time employee equivalents (staff/faculty) for the most recent academic year available. "
            "Search around the tables to identify the latest year (e.g., Fall 2024, AY 2024–25, 2023-24,2023-2024, 2023,etc.). "
            "If multiple years are present (e.g., '2023–24' and '2024–25'), always choose the one that represents the latest year."
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore data outside this period. "
            "It’s possible for a school to have multiple campuses — combine across all campuses if applicable. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Year_Tuition: Optional[str] = Field(
        description=(
            "Extract the academic year or term (e.g., 'Fall 2024', 'AY 2024–2025', '2024–25') that is associated with the" 
            "Undergraduate tuition rate for the 2024-2025 academic year. This is different than revenue generated by" 
            "tuition or any financial accounting data.  Do not guess — only extract if both the value and term are shown."
        )
    )

    Tuition: Optional[int] = Field(
        description=(
            "Undergraduate tuition rate for the most recent academic year available. "
            "This is different from revenue generated by tuition or any financial accounting data. "
            "Search around the tables to identify the latest year or term, such as 'Fall 2024', 'AY 2024–25', '2024-25', '2024-2025' ,'Fall 2023', '2023-2024',or '2023'. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Ignore any data outside this period. "
            "If multiple campuses exist, average the tuition per student across campuses. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Year_Room_and_Board_20_meals: Optional[str] = Field(
        description=(
            "Extract the academic year or term (e.g., 'Fall 2024', 'AY 2024–2025', '2024–25') that is associated with the" 
            "Room & board cost (20-meal plan) for the 2024-2025 academic year." 
            "Do not guess — only extract if both the value and term are shown."
        )
    )
    
    Room_and_Board_20_meals: Optional[int] = Field(
        description=(
            "Room & board cost (20-meal plan) for the most recent academic year available. "
            "Search around the tables to identify the latest year or term, such as 'Fall 2024', 'AY 2024–25', '2024-2025','2024-25' ,'Fall 2023', '2023-2024',or '2023'. "
            "Ignore any data outside this period. "
            "If multiple campuses exist, combine values across all campuses if applicable. "
            "Compare all academic years present (e.g., '2023–24', '2024–25') and extract **only the value associated with the latest year**. "
            "For example, if both '2023–24' and '2024–25' appear, return the value for '2024–25' only." 
            "Do not extract values for earlier years. "
            "Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

