from django.http import JsonResponse

def detail_view(request, item_id: int):
    query = request.GET.get("q")
    return JsonResponse({
        "id": item_id,
        "query": query
    })
