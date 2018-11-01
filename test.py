from utils.coco.coco import COCO
from utils.vocabulary import Vocabulary
from config import Config
import json
from tqdm import tqdm
import time

test = [1,2,3,4,5,6,7,8,9,0]

for number in tqdm(test):
    time.sleep(1)