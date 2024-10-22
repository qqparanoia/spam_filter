class BinaryConfusionMatrix():
    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.dictionary = {
            "tp": 0,
            "tn": 0,
            "fp": 0,
            "fn": 0,
        }

    def as_dict(self):
        return self.dictionary

    def update(self, truth, prediction):
        if truth == self.pos_tag and prediction == self.pos_tag:
            self.dictionary["tp"] += 1
        elif truth == self.neg_tag and prediction == self.neg_tag:
            self.dictionary["tn"] +=1
        elif truth == self.neg_tag and prediction == self.pos_tag:
            self.dictionary["fp"] += 1
        elif truth == self.pos_tag and prediction == self.neg_tag:
            self.dictionary["fn"] += 1
        else:
            raise ValueError("Invalid truth or prediction value")


    def compute_from_dicts(self, truth_dict, pred_dict):
        for key in truth_dict:
            self.update(truth_dict[key], pred_dict[key])





