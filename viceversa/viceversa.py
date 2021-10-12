from django.shortcuts import render

def vice_versa(request):
    return render(request, 'viceversa.html')

def reverse(request):
    user_text = request.GET['usertext']
    user_text_string = str(user_text)
    reverse_text = user_text[::-1]
    text_count = user_text_string.count(' ')
    text_count_2 = text_count+1
    return render(request, 'reverse.html', {'usertext' :user_text, 'reversedtext' :reverse_text , 'textcounter' :text_count_2})