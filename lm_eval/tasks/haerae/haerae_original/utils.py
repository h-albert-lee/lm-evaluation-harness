def doc_to_choice(doc):
    if type(doc["e"]) is str:
        return [doc["a"],doc["b"],doc["c"],doc["d"],doc["e"]]
    else:
        return [doc["a"],doc["b"],doc["c"],doc["d"]]

def doc_to_target(doc):
    answer = doc["answer"]
    aidx = {"a":0,"b":1,"c":2,"d":3,"e":4}[answer]
    if type(doc["e"]) is str:
        return [doc["a"],doc["b"],doc["c"],doc["d"],doc["e"]][aidx]
    else:
        return [doc["a"],doc["b"],doc["c"],doc["d"]][aidx]
