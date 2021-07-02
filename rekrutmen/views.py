from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MemberSignUpForm, JobForm, JobListForm, DoTheTestForm
from .models import Job, JobList, Member, Test

def dashboard (request):
    job_list = Job.objects.all()
    usr_job_list_lst =""
    is_hdc = False
    is_pelamar = False
    try:
        usr_job_list = JobList.objects.filter(pelamar_id=request.user)
        print('user role adalah', str (request.user.member.role))
        usr_job_list_lst = [j.job for j in usr_job_list]
        # for i in job_list:
        #     if i in usr_job_list_lst:
        #         print (i)
        if str (request.user.member.role) == 'HDC':
            is_hdc = True
        if str (request.user.member.role) == 'Pelamar':
            is_pelamar = True
    except:
        is_hdc = False
        is_pelamar = False
    context = { 'is_hdc': is_hdc,
                'is_pelamar': is_pelamar,
                'job_list': job_list,
                'usr_job_list': usr_job_list_lst,
                'applied': False
                }
    return render (request, 'public/dashboard.html', context)

def login_page (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member = authenticate(request, username=username, password=password)
        if member is not None:
            login(request, member)
            # if str(member.member.role) == 'HDC':
            #     return redirect('dashboard')
            # else:
            return redirect ('dashboard')
    context ={}
    return render (request, 'public/login.html', context)

def register (request):
    form = MemberSignUpForm()
    if request.method == 'POST':
        form = MemberSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('dashboard')
    context = {'form': form}
    return render (request, 'public/register.html', context)

def logout_page (request):
    logout(request)
    return redirect('dashboard')

def hdc (request):
    dataset = Job.objects.filter(hdc_id=request.user)
    context = {'dataset':dataset}
    return render(request, 'hdc/hdc_dashboard.html', context)

def add_job (request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect ('dashboard')
    context = {'form':form}
    return render(request, 'hdc/add_job.html', context)

def edit_job (request, id):
    form = JobForm()
    obj = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        form = JobForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.update()
            return redirect ('hdc')
    context = {'form':form,
               'dataset': obj}
    return render(request, 'hdc/edit_job.html', context)

def lamar (request, id):
    dataset = Job.objects.get(pk = id)
    if request.method == 'POST':
        if JobList.objects.filter(job=dataset, pelamar_id=request.user).exists() == False:
            form = JobListForm()
            form.save(dataset, request.user)
            return redirect ('dashboard')
        else: 
            print ('user already applied')
    context = {'dataset':dataset}
    return render (request, 'pelamar/lamar.html', context)

def pelamar (request):
    dataset = JobList.objects.filter(pelamar_id=request.user)
    print (dataset)
    context = {'dataset':dataset}
    return render (request, 'pelamar/pelamar.html', context)

def detail_job (request, id):
    job = Job.objects.filter(pk=id)
    job_list = JobList.objects.filter(job=job[0])
    context = {'job_list':job_list,
                'job': job[0]}
    return render (request, 'hdc/detail_job.html', context)

def detail_pelamar (request, id, id2):
    job_list = JobList.objects.get(job=id, pelamar_id=id2)
    print (job_list)
    form = JobListForm()
    if request.method == 'POST':
        job_list.status =  str (request.POST['status'])
        job_list.save()
        return redirect ('/hdc/job/{id}'.format(id=id))
    context ={'job_list': job_list,
              'form':form,
              }
    return render (request, 'hdc/detail_pelamar.html', context)

def do_the_tests (request,id):
     test_list = Job.objects.get(pk=id)
     usr_tests = JobList.objects.get(pelamar_id=request.user, job=test_list)
     if request.method == 'POST':
         post_data = dict(request.POST)
         for test in post_data['tests']:
             usr_tests.tests.add(Test.objects.get(test_name=test))
         usr_tests.save()
         return redirect ('pelamar')
     context = { 'test_list': test_list,
                 'usr_tests': usr_tests
                }
     return render (request, 'pelamar/test.html', context)