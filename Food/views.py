from django.shortcuts import redirect, render

from Food.forms import AddItem
# import django.http as HttpResponse

from .models import Item
# Create your views here.
def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'Food/item_list.html', context=context )

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

def add_item(request):
    form = AddItem(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('food:item_list')
    return render(request, 'food/form.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = AddItem(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:item_list')
    return render(request, 'food/form.html', {'form': form, 'item':item})



