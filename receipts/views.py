# receipts/views.py
from django.shortcuts import render
from .models import Receipt
from .forms import ReceiptForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipts/receipt_list.html', {'receipts': receipts})

@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    return render(request, 'receipts/receipt_detail.html', {'receipt': receipt})

@login_required
def receipt_form(request, pk=None):
    if pk:
        receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    else:
        receipt = Receipt(user=request.user)

    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm(instance=receipt)

    return render(request, 'receipts/receipt_form.html', {'form': form})
