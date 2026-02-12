from django.shortcuts import render
import collections
import re

def home(request):
    context = {}
    
    # Check if the form was submitted via POST
    if request.method == 'POST':
        text = request.POST.get('fulltext', '')
        
        # 1. Count Characters
        char_count = len(text)
        
        # 2. Count Words
        word_list = text.split()
        word_count = len(word_list)
        
        # 3. Frequency Analysis (All Words)
        # Clean the text: lower case and remove non-alphanumeric characters
        clean_text = re.sub(r'[^\w\s]', '', text).lower()
        clean_word_list = clean_text.split()
        
        # Use Counter to find most common words
        word_frequency = collections.Counter(clean_word_list)
        
        # CHANGE: Empty parentheses gets ALL words, sorted by frequency
        all_words = word_frequency.most_common()
        
        # Prepare context to send back to HTML
        context = {
            'text': text, 
            'word_count': word_count,
            'char_count': char_count,
            'all_words': all_words, # Renamed from 'top_words'
            'analyzed': True 
        }

    return render(request, 'home.html', context)