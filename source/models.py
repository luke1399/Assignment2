# MODELS
from sklearn.dummy import DummyClassifier


def baseline_model(
    strategy, level_3_cat, train_df, columns_to_keep
):  # Da rivere i parametri una volta definito un dizionario per tutte le variabili(?)
    clf_list = [DummyClassifier(strategy=strategy) for _ in level_3_cat]
    [
        clf.fit(X=train_df[columns_to_keep[1:]], y=train_df[cat])
        for clf, cat in zip(clf_list, level_3_cat)
    ]
    return clf_list
