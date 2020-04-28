from django.contrib import admin
from .models import Question, Answers, Student, QuestionsAnswered

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Student)

# TASK:
# Create test template which shows inside admin
#       1. question
#           - INLINE options - 2 answers (4 options max)
#       2. question
#           - INLINE options - 2 answers (4 options max)
#       Submit
# On submit save to QuestionsAnswered
