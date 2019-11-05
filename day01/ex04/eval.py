class Evaluator():
    def zip_evaluate(words, coefs):
        if len(coefs) != len(words):
            return -1
        return sum(i * len(j) for i, j in zip(coefs, words))

    def enumerate_evaluate(words, coefs):
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(w) for i, w in enumerate(words))
