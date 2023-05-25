from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect

from .forms import nudge_form
from .models import nudge_model
import uuid
def welcome_screen_view(request):
	print(request.headers)
	return render(request,"nudges/welcome.html",{})

def add_event_view(request):
	print(request.headers)
	return render(request,"nudges/create_event.html",{})


from django.core.paginator import Paginator

def all_events(request):
    events = nudge_model.objects.all()
    paginator = Paginator(events, 2)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "nudges/all_events.html", {'page_obj': page_obj})




@csrf_protect
def add_event(request):
	if request.method == 'POST':
		form = nudge_form(request.POST, request.FILES)
		if form.is_valid():
			uid = str(uuid.uuid4())
			name = form.cleaned_data[ 'name']
			image = form.cleaned_data['image']
			tagline = form.cleaned_data['tagline']
			schedule = form.cleaned_data['schedule']
			description = form.cleaned_data['description']
			moderator = form.cleaned_data['moderator']
			category = form.cleaned_data['category']
			sub_category = form.cleaned_data['sub_category']
			rigor_rank = form.cleaned_data['rigor_rank']

			nudge_model = form.save(commit=False)
			nudge_model.uid = uid
			nudge_model.save()
			# return render(request, 'account/tempview.html', {'classes': classes})
			return redirect('all_events')
		else:
			form = add_class_form(request.POST)
			print(form.errors)
			return redirect('add_event_view')
	else:
		form = add_class_form()
	return render(request, 'nudges/add_event.html', {'form': form})



def delete_event(request,event):
	event_to_delete = nudge_model.objects.get(pk=event)
	event_to_delete.delete()
	return redirect('all_events')



def event(request):
    if 'uuid' in request.GET:
        uuid = request.GET['uuid']
        try:
            event = nudge_model.objects.get(uid=uuid)
            return render(request, 'nudges/search_result.html', {'event': event})
        except nudge_model.DoesNotExist:
            return render(request, 'nudges/search_result.html', {'event': None})

    return render(request, 'nudges/search_event.html')