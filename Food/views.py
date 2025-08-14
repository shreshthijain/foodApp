from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from Food.forms import AddItem
from .models import Item
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'Food/index.html')

def item_list(request):
    items = Item.objects.all()

    item_names = request.GET.get('search_item')

    if item_names != "" and item_names is not None:
        items = items.filter(item_name__icontains=item_names)

    paginator = Paginator(items, 2)  
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'items': items
    }
    return render(request, 'Food/item_list.html', context=context )

@login_required
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
        item.delete()
        return redirect('food:item_list')
    except Item.DoesNotExist:
        return redirect('food:item_list')
    
def item_details(request, id):
    item = Item.objects.get(id=id)
    print(item)
    return render(request, 'Food/details.html', {'item': item})

@login_required
def add_item(request):
    form = AddItem(request.POST or None, request.FILES)
    # form.fields['user'].initial = request.user.username

    if form.is_valid():
        item = form.save()
        item.user = request.user
        item.save()
        return redirect('food:item_list')
    return render(request, 'food/form.html', {'form': form})

@login_required
def update_item(request, id):
    item = Item.objects.get(id=id)
    form = AddItem(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:item_list')
    return render(request, 'food/form.html', {'form': form, 'item':item})



