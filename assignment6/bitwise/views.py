from django.shortcuts import render
from .forms import NumberForm
from pymongo import MongoClient

def process_numbers(request):
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [form.cleaned_data[f] for f in ['a', 'b', 'c', 'd', 'e']]
            average = sum(nums) / len(nums)
            positives = sum(1 for n in nums if n > 0)
            even_odd = ['Even' if n & 1 == 0 else 'Odd' for n in nums]
            filtered_sorted = sorted([n for n in nums if n > 10])
            
            result = {
                'original': nums,
                'sorted_gt10': filtered_sorted,
                'average': average,
                'positives': positives,
                'even_odd': even_odd,
            }

            client = MongoClient("mongodb://cctb1:cctb2025@<54.166.53.193>:27017/")
            db = client['assignment6']
            db.results.insert_one({'input': nums, 'result': result})
    else:
        form = NumberForm()

    return render(request, 'bitwise/result.html', {'form': form, 'result': result})
