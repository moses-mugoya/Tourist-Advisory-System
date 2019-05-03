from django.shortcuts import render, get_object_or_404
from .models import Destinations
from .forms import QuestionForm, ExpenseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'tourism/indexe.html')


def destination(request):
    destinations = Destinations.objects.all()
    return render(request, 'tourism/destination.html', {'destinations': destinations})


def detail(request, id, slug):
    destination = get_object_or_404(Destinations, id=id, slug=slug)
    return render(request, 'tourism/detail.html', {'destination': destination})


@login_required
def question(request):
    suggestions = []
    tsavo = Destinations.objects.get(name='Tsavo National Reserve')
    long = Destinations.objects.get(name='Mount Longonot')
    samburu = Destinations.objects.get(name='Samburu Buffalo Springs')
    nakuru = Destinations.objects.get(name='Lake Nakuru')
    bogoria = Destinations.objects.get(name='Lake Bogoria')
    gedi = Destinations.objects.get(name='Gedi Ruins')
    naivasha = Destinations.objects.get(name='Lake Naivasha')
    hells = Destinations.objects.get(name='Hell\'s Gate National Park')
    nairobi = Destinations.objects.get(name='Nairobi National Museum')
    mount = Destinations.objects.get(name='Mount Kenya National Park')
    mombasa = Destinations.objects.get(name='Mombasa Fort Jesus')
    maasai = Destinations.objects.get(name='Maasai Mara National Reserve')
    malindi = Destinations.objects.get(name='Malindi')
    amboseli = Destinations.objects.get(name='Amboseli')
    lamu = Destinations.objects.get(name='Lamu Island')
    pejeta = Destinations.objects.get(name='Ol pejeta Conservancy')

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        if question_form.is_valid():
            if question_form.cleaned_data['reason'] == 'fun':
                suggestions.append(hells)
                suggestions.append(nakuru)
                suggestions.append(malindi)
                suggestions.append(naivasha)
                suggestions.append(amboseli)
                suggestions.append(lamu)
                suggestions.append(pejeta)
                suggestions.append(maasai)
                suggestions.append(mombasa)
                suggestions.append(mount)
                suggestions.append(nairobi)
                suggestions.append(gedi)
                suggestions.append(tsavo)
                suggestions.append(bogoria)
                suggestions.append(samburu)
                suggestions.append(long)
                
            elif question_form.cleaned_data['reason'] == 'honeymoon':
                suggestions.append(hells)
                suggestions.append(nakuru)
                suggestions.append(malindi)
                suggestions.append(naivasha)
                suggestions.append(amboseli)
                suggestions.append(lamu)
                suggestions.append(pejeta)
                suggestions.append(maasai)
                suggestions.append(mombasa)
                suggestions.append(mount)
                suggestions.append(nairobi)
                suggestions.append(gedi)
                suggestions.append(tsavo)
                suggestions.append(bogoria)
                suggestions.append(samburu)
                suggestions.append(long)
            else:
                suggestions.append(hells)
                suggestions.append(nakuru)
                suggestions.append(malindi)
                suggestions.append(naivasha)
                suggestions.append(amboseli)
                suggestions.append(lamu)
                suggestions.append(pejeta)
                suggestions.append(maasai)
                suggestions.append(mombasa)
                suggestions.append(mount)
                suggestions.append(nairobi)
                suggestions.append(gedi)
                suggestions.append(tsavo)
                suggestions.append(bogoria)
                suggestions.append(samburu)
                suggestions.append(long)
            if question_form.cleaned_data['phobia'] == 'height':
                if long in suggestions:
                    suggestions.remove(long)
            elif question_form.cleaned_data['phobia'] == 'water':
                if naivasha in suggestions:
                    suggestions.remove(naivasha)
                if nakuru in suggestions:
                    suggestions.remove(nakuru)
                if bogoria in suggestions:
                    suggestions.remove(bogoria)
                if malindi in suggestions:
                    suggestions.remove(malindi)
                if lamu in suggestions:
                    suggestions.remove(lamu)
                if mombasa in suggestions:
                    suggestions.remove(mombasa)
            elif question_form.cleaned_data['phobia'] == 'animal':
                if tsavo in suggestions:
                    suggestions.remove(tsavo)
                if maasai in suggestions:
                    suggestions.remove(maasai)
                if amboseli in suggestions:
                    suggestions.remove(amboseli)
                if nakuru in suggestions:
                    suggestions.remove(nakuru)
                if samburu in suggestions:
                    suggestions.remove(samburu)
                if hells in suggestions:
                    suggestions.remove(hells)
                if mount in suggestions:
                    suggestions.remove(mount)
                if nairobi in suggestions:
                    suggestions.remove(nairobi)
                if pejeta in suggestions:
                    suggestions.remove(pejeta)
                
            if question_form.cleaned_data['activity'] == 'hiking':
                if long not in suggestions:
                    messages.error(request, "You chose height phobia, consider choosing another option")
                    suggestions.clear()
            if question_form.cleaned_data['activity'] == 'swimming':
                if malindi not in suggestions:
                    messages.error(request, "You chose water phobia, consider choosing another option")
                    suggestions.clear()
                if naivasha in suggestions:
                    suggestions.remove(naivasha)
                if nakuru in suggestions:
                    suggestions.remove(nakuru)
                if bogoria in suggestions:
                    suggestions.remove(bogoria)
                if lamu in suggestions:
                    suggestions.remove(lamu)
                if tsavo in suggestions:
                    suggestions.remove(tsavo)
                if maasai in suggestions:
                    suggestions.remove(maasai)
                if amboseli in suggestions:
                    suggestions.remove(amboseli)
                if nakuru in suggestions:
                    suggestions.remove(nakuru)
                if mount in suggestions:
                    suggestions.remove(mount)
                if samburu in suggestions:
                    suggestions.remove(samburu)
                if mombasa in suggestions:
                    suggestions.remove(mombasa)
                if pejeta in suggestions:
                    suggestions.remove(pejeta)
                if gedi in suggestions:
                    suggestions.remove(gedi)
                if hells in suggestions:
                    suggestions.remove(hells)
                if nairobi in suggestions:
                    suggestions.remove(nairobi)
            if question_form.cleaned_data['activity'] == 'Sight seeing':
                print(suggestions)

    else:
        question_form = QuestionForm()
    return render(request, 'tourism/suggest.html', {'suggestions': suggestions, 'question_form': question_form})


@login_required
def get_expense(request, id):
    destination = get_object_or_404(Destinations, id=id)

    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)

        if expense_form.is_valid():
            new_expense_form = expense_form.save(commit=False)
            new_expense_form.destination = destination
            new_expense_form.user = request.user
            new_expense_form.save()
            messages.success(request, 'Your data has successfully been submitted. Visit your dashboard to see your generated travel schedule and expense')
    else:
        expense_form = ExpenseForm()
    return render(request, 'tourism/expense.html', {'expense_form': expense_form})



