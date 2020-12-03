from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
import math

from .forms import NameForm
from . import matrix
from . import inverse_matrix


def get_settings(request):
    # if this is a POST request we need to process the form data
    error_message = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        post_data = request.POST.dict()
        print(post_data)
        if "row-a-0-0" in request.POST.keys() and "row-b-0" in request.POST.keys():
            post_data = request.POST.dict()
            d = 1 + 4*(len(post_data)-1)  # b**2 - 4ac = 1 - 4c = 1+4*len()
            n = int((-1 + math.sqrt(d)) / 2)

            print(n)
            matrix_a = [[float(post_data[f"row-a-{i}-{j}"]) for j in range(n)] for i in range(n)]
            matrix_b = [float(post_data[f"row-b-{j}"]) for j in range(n)]
            matrix_all = list()
            for i in range(n):
                row = [i for i in matrix_a[i]]
                row.append(matrix_b[i])
                matrix_all.append(row)

            columnlines_ = "none " * (n-1)
            columnlines_ += "solid"
            print(matrix_a)
            print(matrix_b)
            solve = inverse_matrix.solve(matrix_a, matrix_b)
            try:
                det = matrix.find_det(matrix_a)
            except Exception:
                det = 0
            if solve:
                union_matrix = matrix.find_union_matrix(matrix_a)
                print(union_matrix)
                trans_matrix = matrix.transpose_matrix(union_matrix)
                inv_matrix = [[trans_matrix[i][j]/det for j in range(n)] for i in range(n)]
                return render(request, 'matrix/result.html', {
                    'matrix_a': matrix_a,
                    'matrix_b': matrix_b,
                    'matrix_all': matrix_all,
                    'columnlines_': columnlines_,
                    'det': det,
                    'union_matrix': union_matrix,
                    'trans_matrix': trans_matrix,
                    'inv_matrix': inv_matrix,
                    'solve': solve,
                })
            elif det == 0:
                error_message = "Determinant equals 0!"
            else:
                error_message = "Can't find solution!"

        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            try:
                matrix_size = int(form.data['matrix_size'])
            except Exception:
                error_message = "Size has to be integer"
            else:
                return render(request, 'matrix/thanks.html', {
                    'size': matrix_size,
                    'size0_array': range(matrix_size),
                    'size1_array': range(1, matrix_size + 1),
                })
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'matrix/get_settings.html', {
        'form': form,
        'error_message': error_message,
    })
