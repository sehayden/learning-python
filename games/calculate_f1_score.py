def calculate_precision(tp, fp):
    return tp/(tp+fp)

def calculate_recall(tp, fn):
    return tp/(tp+fn)

def validate_input(input):
    return type(input) == int and input >= 0

def calculate_f1(tp, fp, fn):
    params = {"tp": tp, "fp": fp, "fn": fn}
    for key, value in params.items():
        if not validate_input(value):
            print (key, 'must be a non negative int')
            return
    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    f1 = 2 * precision * recall / (precision + recall)
    print('precision is', precision)
    print('recall is', recall)
    print('f1 is', f1)

calculate_f1(0, 3, 4)