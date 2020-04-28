from django.contrib import admin
from .models import Question, Answers, Student, QuestionsAnswered

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Student)

# TASK:
# need custom admin template inside admin that shows
#       all questions assigned to user
#       filter option sort by user

# TASK:
# Create test template which shows inside admin
#       1. question
#           - INLINE options - 2 answers (4 options max)
#       2. question
#           - INLINE options - 2 answers (4 options max)
#       Submit
# On submit save to QuestionsAnswered
