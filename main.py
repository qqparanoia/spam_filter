from corpus import Corpus
from simplefilters import RandomFilter, NaiveFilter, ParanoidFilter
from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix
import quality, os

DIR = "./1"

if __name__ == '__main__':

    rndm = RandomFilter()
    rndm.test(DIR)
    score = quality.compute_quality_for_corpus(DIR)
    print(score)
    os.remove(DIR+"/!prediction.txt")

