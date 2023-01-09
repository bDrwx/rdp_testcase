def qsort(array):
    """Реализация алгоритма быстрой сортировки с одной опорной чочкой

    Args:
        array (Array): Не сортированный массив

    Returns:
        Array: Сортированный масив
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)
