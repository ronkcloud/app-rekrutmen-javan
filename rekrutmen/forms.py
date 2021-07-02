from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import JobList, Role, Member, User, Job, Test
from django.db import transaction

class MemberSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    role = forms.ModelChoiceField(
        queryset=Role.objects.all()
        )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()

        Member.objects.create(
            user=user, 
            name=self.cleaned_data.get('name'),
            role=self.cleaned_data.get('role'),
            )
            
        return user

class JobForm(forms.ModelForm):
    tests = forms.ModelMultipleChoiceField(
        queryset=Test.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Job
        fields = [
            'job_name',
            'description',
            'tests',
        ]

    @transaction.atomic
    def save(self,hdc):
        tests = self.cleaned_data.get('tests')
        for test in tests:
            print (Test.objects.get(test_name=test))
        job = Job.objects.create(
            job_name=self.cleaned_data.get('job_name'),
            description=self.cleaned_data.get('description'),
            hdc_id=hdc,
                )
        for test in tests:
            job.tests.add(Test.objects.get(test_name=test))
    
    def update(self):
        user = super().save()
        user.save()

class JobListForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ['status']

    @transaction.atomic
    def save(self, job, pelamar):
        JobList.objects.create(
            job=job,
            pelamar_id=pelamar,
            )
    
    def update(self):
        user = super().save()
        user.save()

class DoTheTestForm(forms.ModelForm):
    tests = forms.ModelMultipleChoiceField(
        queryset=Test.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Member
        fields = ['tests']
    