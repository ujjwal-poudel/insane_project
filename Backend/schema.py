from enum import Enum

class ModelChoice(str, Enum):
    model_a = "model_a"
    model_b = "model_b"
    model_c = "model_c"

class StudentData(BaseModel):
    model_choice: ModelChoice
    first_term_gpa: float
    second_term_gpa: float
    first_language: int
    funding: int
    school: int
    fast_track: int
    coop: int
    residency: int
    gender: int
    prev_education: int
    age_group: int
    hs_average: float
    math_score: float
    english_grade: int
