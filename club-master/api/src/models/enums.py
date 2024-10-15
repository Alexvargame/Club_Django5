from django.db import models


class Status(models.TextChoices):
    OPEN = "OPEN", "Открыт"
    CLOSED = "CLOSED", "Закрыт"
    STARTED = "STARTED", "Стартовал"
    BACKLOG = "BACKLOG", "Backlog"


class Role(models.TextChoices):
    BACKEND = "BACKEND", "Backend"
    FRONTEND = "FRONTEND", "Frontend"
    FULLSTACK = "FULLSTACK", "Fullstack"
    DESIGN = "DESIGN", "Design"
    DEVOPS = "DEVOPS", "Devops"
    QA = "QA", "QA"
    PM = "PM", "PM"
    OTHER = "OTHER", "Other"

class Grade(models.TextChoices):
    INTERN = 'INTERN' , 'Стажер'
    JUNIOR = 'JUNIOR', 'Junior'
    JUNOIR_PLUS = 'JUNIOR_PLUS' , 'Junior+'
    MIDDLE = 'MIDDLE', 'Middle'
    MIDDLE_PLUS = 'MIDDLE_PLUS', 'Middle+'
    SENIOR = 'SENIOR', 'Senior'
    SENIOR_PLUS = 'SENIOR_PLUS' , 'Senior+'
