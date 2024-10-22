import confmat, utils, os

def quality_score(tp,tn,fp,fn):
    return (tp+tn)/(tp+tn+10*fp+fn)

def compute_quality_for_corpus(corpus_dir):
    quality = confmat.BinaryConfusionMatrix("SPAM","OK")

    truth = utils.read_classification_from_file(corpus_dir + "/!truth.txt")
    prediction = utils.read_classification_from_file(corpus_dir+ "/!prediction.txt")

    for key in truth.keys():
        quality.update(truth[key],prediction[key])

    dictionary = quality.as_dict()
    tp = dictionary["tp"]
    tn = dictionary["tn"]
    fp = dictionary["fp"]
    fn = dictionary["fn"]

    return quality_score(tp,tn,fp,fn)

