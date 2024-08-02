from django.shortcuts import render
from django.http import JsonResponse
import hashlib
import json

def cracker(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            hash_text = data.get('text', '').strip()
            hash_type = data.get('hash_type', 'md5')

            result = generate_hash(hash_text, hash_type)
            return JsonResponse({'result': result})
        except json.JSONDecodeError:
            return JsonResponse({'result': "Invalid input data."}, status=400)

    return render(request, 'password_cracker/templates/cracker.html')


def generate_hash(hash_text, hash_type):
    hash_algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s
    }

    try:
        hash_func = hash_algorithms[hash_type]
        hashed_text = hash_func(hash_text.encode()).hexdigest()
        return f"{hashed_text}"
    except KeyError:
        return "Invalid hash type specified."