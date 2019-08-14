from dataclasses import dataclass


@dataclass
class AboutMe:
    first_name: str
    last_name: str
    street_address: str
    city_state: str

    phone_number: str
    email_address: str
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class EducationItem:
    school: str
    program: str
    start_date: str
    end_date: str


@dataclass
class ExperienceItem:
    company: str
    position: str
    start_date: str
    end_date: str


### Begin defining fields
subject = AboutMe(
    first_name="Aaron", last_name="Rogers",
    street_address="820 Bennett Ave", city_state="Colorado Springs, CO 80909",
    email_address="aaron.kyle.rogers@gmail.com",
    phone_number="(719) 452-0578"
)


social_links = [
    ("fa-github", "https://github.com/kyrogon"),
    ("fa-linkedin-in", "https://linkedin.com/in/aaron-rogers-370bb654/"),
]


skill_icons = ["fa-linux", "fa-python", "fa-html5", "fa-css3-alt"]


skillset = [
    "Linux Installation and Support",
    "SSH, Screen, Tmux, Vim",
    "Python Datatypes, Numpy, Pandas",
]

experience = [
    ExperienceItem(
        company="Lowe's Home Improvement", 
        position="Delivery Driver", 
        start_date="March 2017", end_date="Present"
    ),
    ExperienceItem(
        company="American Furniture Warehouse", 
        position="Delivery Driver", 
        start_date="October 2013", end_date="March 2017"
    ),
    ExperienceItem(
        company="7-Eleven", 
        position="Clerk", 
        start_date="August 2012", end_date="October 2013"
    ),
]


education = [
    EducationItem(
        school="St Petersburg College", 
        program="General Studies", 
        start_date="August 2010", end_date="May 2011",
    ),
    EducationItem(
        school="Dunedin High School", 
        program="HS Diploma", 
        start_date="August 2006", end_date="May 2010",
    ),
]
