from django.shortcuts import render
from django.http import HttpResponse
from . models import Popular_Destinations


# Create your views here.
def demo(request):
    obj=Popular_Destinations.objects.all()
    return render(request, 'index-2.html',{'result':obj})

#
# def result(request) :
#     num1 = float( request.GET ['num1'] )
#     num2 = float( request.GET ['num2'] )
#     addition_result = num1 + num2
#     subtraction_result = num1 - num2
#     multiplication_result = num1 * num2
#     division_result = num1 / num2
#     return render( request, 'result.html', {
#         'addition_result' : addition_result,
#         'subtraction_result' : subtraction_result,
#         'multiplication_result' : multiplication_result,
#         'division_result' : division_result})

# def about(request) :
#     return render( request, 'about.html' )
#
#
# def contact(request) :
#     return HttpResponse( "i am contact" )
