from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
# Create your views here.
import logging
import re

from .forms import ItemForm

logger = logging.getLogger(__name__)

def item_list(request):
    qs = Item.objects.all() #아이템모델 전체를 가져온다

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    
    logger.debug('query : {}'.format(q))
    return render(request, 'shop/item_list.html',{
        'item_list':qs, #템플릿은 참조하겠다
        'q':q, 
    })


def item_detail(request,pk): #pk를 인자로 받는다
    item = get_object_or_404(Item,pk=pk) #item객체를 만들어 404함수를 쓴다
    return render(request, 'shop/item_detail.html',{
        'item':item,  #해당 아이템 객체를 사용하게 된다
        
    })


def item_new(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES ,instance=item)
        if form.is_valid():
            item = form.save() #ModelForm에서 제공
            return redirect(item)
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_new.html', {
        'form' : form,
    })

def item_edit(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request,item)
