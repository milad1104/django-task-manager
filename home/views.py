from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
import jdatetime
from .models import Profile, Task
from .forms import ProfileForm, UserForm, TaskForm


class IndexView(View):
    template_name = 'home/index.html'

    def get(self, request):
        task_form = TaskForm()

        filter_type = request.GET.get('filter', 'all')

        if filter_type == 'active':
            tasks = Task.objects.filter(user=request.user.profile, status=False)
        elif filter_type == "complete":
            tasks = Task.objects.filter(user=request.user.profile, status=True)
        else:
            tasks = Task.objects.filter(user=request.user.profile)
            
        for task in tasks:
            task.jalali_date = jdatetime.datetime.fromgregorian(
                datetime=task.published
            ).strftime('%Y/%m/%d')

        task_count = tasks.count()
        return render(request, self.template_name, {'task_form': task_form, 'tasks': tasks, 'task_count': task_count})

    def post(self, request):
        task_form = TaskForm(request.POST)
        tasks = Task.objects.filter(user=request.user.profile)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user.profile
            task.save()
            return redirect('home:index')

        return render(request, self.template_name, {'task_form': task_form, 'tasks': tasks})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'home/profile.html'

    def get(self, request):
        profile = request.user.profile

        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

        return render(request, self.template_name, {
            'profile_form': profile_form,
            'user_form': user_form,
            'profile': profile,
        })

    def post(self, request):
        profile = request.user.profile

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()

            return redirect('home:profile')

        return render(request, self.template_name, {
            'profile_form': profile_form,
            'user_form': user_form,
            'profile': profile,
        })


class TaskCompleteView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id, user=request.user.profile)
        task.status = True
        task.save()

        return redirect('home:index')


class DeleteTaskView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id, user=request.user.profile)
        task.delete()
        return redirect('home:index')
