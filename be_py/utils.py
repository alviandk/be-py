from random import sample


def sample_from_models(Model, count):
    all_ids = Model.objects.filter(show=True).values_list('id', flat=True)
    count_all_ids = all_ids.count()
    if count > count_all_ids:
        count = count_all_ids
    return sample(list(all_ids), k=count)