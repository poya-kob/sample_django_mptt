from django.shortcuts import render, HttpResponse

from .models import Products, Categories


def search(request):
    Categories.objects.rebuild()
    cat = Categories.objects.all()

    # print(cat.first().get_root())
    # print(cat.first().get_children())
    # print(cat.first().get_descendants(include_self=False))
    # print(cat.first().get_family())
    # print(cat.first().get_next_sibling())
    # print(cat.first().get_previous_sibling())
    # print(cat.first().get_siblings(include_self=False))
    # print(cat.last().is_child_node())
    # print(cat.last().is_leaf_node())
    # print(cat.last().is_root_node())
    # print(cat.last().get_ancestors())
    cat_return = []
    if request.method == 'POST':
        cat_id = request.POST.get('id')
        selected_cat = Categories.objects.get(id=cat_id)

        for category in selected_cat.get_family():
            if category.is_leaf_node():
                cat_return.append(category)
        print(cat_return)
    return render(request, 'products.html', {'cat': cat,
                                             'product': Products.objects.first(),
                                             'model': Categories,
                                             'selected_cat': cat_return})
