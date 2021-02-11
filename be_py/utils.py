from random import sample


def sample_from_models(Model, count):
    all_ids = Model.objects.all().values_list('id', flat=True)
    count_all_ids = all_ids.count()
    if count > count_all_ids:
        count = count_all_ids
    return sample(list(all_ids), k=count)