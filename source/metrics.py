from sklearn import f1_score


def f1_baseline(prediction, labels, data):
    ### Evaluate F1 overall
    f1_overall = f1_score(y_true=data[labels], y_pred=prediction, average="macro")

    ### Evaluate F1 per category
    f1_per_cat = [
        f1_score(y_true=data[cat], y_pred=prediction[:, i])
        for i, cat in enumerate(labels)
    ]

    return f1_overall, f1_per_cat
