from sklearn.metrics import r2_score

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return r2_score(y_test, y_pred)