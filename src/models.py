from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Publication:
    title: str
    year: Optional[int] = None
    url: Optional[str] = None


@dataclass
class ResearcherProfile:
    name: str
    institution: str
    department: Optional[str] = None
    title: Optional[str] = None

    research_interests: List[str] = field(default_factory=list)
    research_description: str = ""
    projects: List[str] = field(default_factory=list)
    publications: List[Publication] = field(default_factory=list)

    faculty_url: Optional[str] = None
    lab_url: Optional[str] = None

    source_text: str = ""