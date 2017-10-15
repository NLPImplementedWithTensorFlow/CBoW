import argparse
import os
from util import *
from model import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--itr", dest="itr", type=int, default=10000)
    parser.add_argument("--lr", dest="lr", type=float, default= 0.2) 
    parser.add_argument("--batch_size", dest="batch_size", type=int, default=5)
    parser.add_argument("--max_time_step", dest="max_time_step", type=int, default=7)
    parser.add_argument("--data_path", dest="data_path", type=str, default="data/training_text.txt")
    parser.add_argument("--dict_path", dest="dict_path", type=str, default="data/dict.txt")
    parser.add_argument("--train", dest="train", type=bool, default=True)
    args = parser.parse_args()

    if not os.path.exists(args.dict_path):
        dict_ = mk_dict(args.data_path)
        save_dict(dict_, args.dict_path)

    if not os.path.exists("saved"):
        os.mkdir("saved")

    model_ = model(args)
    if args.train:
        model_.train()

