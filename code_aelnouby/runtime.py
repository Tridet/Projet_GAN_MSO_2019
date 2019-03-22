from trainer import Trainer
from tester import Tester
import argparse
from PIL import Image
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("--type", default='gan')
parser.add_argument("--lr", default=0.0002, type=float)
parser.add_argument("--l1_coef", default=50, type=float)
parser.add_argument("--l2_coef", default=100, type=float)
parser.add_argument("--diter", default=5, type=int)
parser.add_argument("--cls", default=False, action='store_true')
parser.add_argument("--vis_screen", default='gan')
parser.add_argument("--save_path", default=time.strftime("%Y_%m_%H_%M_%S"))
parser.add_argument("--inference", default=True, action='store_true')
parser.add_argument('--pre_trained_disc', default="C:/Users/Theo/Documents/GitHub/Text-to-Image-Synthesis/checkpoints/checkpoints_birds_infer_embed/disc_190.pth") #défaut : None
parser.add_argument('--pre_trained_gen', default="C:/Users/Theo/Documents/GitHub/Text-to-Image-Synthesis/checkpoints/checkpoints_birds_infer_embed/gen_190.pth") #défaut : None
parser.add_argument('--dataset', default='birds')
parser.add_argument('--split', default=0, type=int)
parser.add_argument('--batch_size', default=32, type=int) #défaut : 64
parser.add_argument('--num_workers', default=0, type=int) #défaut : 8 (mettre à 0 pour désactiver le multiprocessing)
parser.add_argument('--epochs', default=10, type=int) #defaut : 200
args = parser.parse_args()



if not args.inference:
    trainer = Trainer(type=args.type,
                    dataset=args.dataset,
                    split=args.split,
                    lr=args.lr,
                    diter=args.diter,
                    vis_screen=args.vis_screen,
                    save_path=args.save_path,
                    l1_coef=args.l1_coef,
                    l2_coef=args.l2_coef,
                    pre_trained_disc=args.pre_trained_disc,
                    pre_trained_gen=args.pre_trained_gen,
                    batch_size=args.batch_size,
                    num_workers=args.num_workers,
                    epochs=args.epochs
                    )
    trainer.train(args.cls)
else:
    tester = Tester(type=args.type,
                    dataset=args.dataset,
                    save_path=args.save_path,
                    pre_trained_disc=args.pre_trained_disc,
                    pre_trained_gen=args.pre_trained_gen
                    )
    tester.predict(txt=["the medium sized bird has a dark grey color", "the bird has green feathers and a dark tail"])

