import os
from easydict import EasyDict
# runner
from basicts.runners.AGCRN_runner import AGCRNRunner
from basicts.data.base_dataset import BaseDataset
from basicts.metrics.mae import masked_mae
from basicts.metrics.mape import masked_mape
from basicts.metrics.rmse import masked_rmse
from basicts.losses.losses import L1Loss

CFG = EasyDict()

# ================= general ================= #
CFG.DESCRIPTION = 'AGCRN model configuration'
CFG.RUNNER  = AGCRNRunner
CFG.DATASET_CLS   = BaseDataset
CFG.DATASET_NAME  = "PEMS08"
CFG.DATASET_TYPE  = 'Traffic flow'
CFG.GPU_NUM = 1
CFG.METRICS = {
    "MAE": masked_mae,
    "RMSE": masked_rmse,
    "MAPE": masked_mape
}

# ================= environment ================= #
CFG.ENV = EasyDict()
CFG.ENV.SEED    = 1
CFG.ENV.CUDNN = EasyDict()
CFG.ENV.CUDNN.ENABLED = True

# ================= model ================= #
CFG.MODEL = EasyDict()
CFG.MODEL.NAME  = 'AGCRN'
CFG.MODEL.PARAM = {
    "num_nodes" : 170, 
    "input_dim" : 1,
    "rnn_units" : 64,
    "output_dim": 1,
    "horizon"   : 12,
    "num_layers": 2,
    "default_graph": True,
    "embed_dim" : 2,
    "cheb_k"    : 2
}
CFG.MODEL.FROWARD_FEATURES = [0]            
CFG.MODEL.TARGET_FEATURES  = [0]                

# ================= optim ================= #
CFG.TRAIN = EasyDict()
CFG.TRAIN.LOSS = L1Loss
CFG.TRAIN.OPTIM = EasyDict()
CFG.TRAIN.OPTIM.TYPE = "Adam"
CFG.TRAIN.OPTIM.PARAM= {
    "lr":0.003,
}
# CFG.TRAIN.LR_SCHEDULER = EasyDict()
# CFG.TRAIN.LR_SCHEDULER.TYPE = "MultiStepLR"
# CFG.TRAIN.LR_SCHEDULER.PARAM= {
#     "milestones":[5, 20, 40, 70],
#     "gamma":0.3
# }

# ================= train ================= #
# CFG.TRAIN.CLIP_GRAD_PARAM = {
#     'max_norm': 5.0
# }
CFG.TRAIN.NUM_EPOCHS = 200
CFG.TRAIN.CKPT_SAVE_DIR = os.path.join(
    'checkpoints',
    '_'.join([CFG.MODEL.NAME, str(CFG.TRAIN.NUM_EPOCHS)])
)
# train data
CFG.TRAIN.DATA          = EasyDict()
CFG.TRAIN.NULL_VAL      = 0.0
## read data
CFG.TRAIN.DATA.DIR      = 'datasets/' + CFG.DATASET_NAME
## dataloader args, optional
CFG.TRAIN.DATA.BATCH_SIZE   = 64
CFG.TRAIN.DATA.PREFETCH     = False
CFG.TRAIN.DATA.SHUFFLE      = True
CFG.TRAIN.DATA.NUM_WORKERS  = 2
CFG.TRAIN.DATA.PIN_MEMORY   = False

# ================= validate ================= #
CFG.VAL = EasyDict()
CFG.VAL.INTERVAL = 1
# validating data
CFG.VAL.DATA = EasyDict()
## read data
CFG.VAL.DATA.DIR      = 'datasets/' + CFG.DATASET_NAME
## dataloader args, optional
CFG.VAL.DATA.BATCH_SIZE     = 64
CFG.VAL.DATA.PREFETCH       = False
CFG.VAL.DATA.SHUFFLE        = False
CFG.VAL.DATA.NUM_WORKERS    = 2
CFG.VAL.DATA.PIN_MEMORY     = False

# ================= test ================= #
CFG.TEST = EasyDict()
CFG.TEST.INTERVAL = 1
# validating data
CFG.TEST.DATA = EasyDict()
## read data
CFG.TEST.DATA.DIR      = 'datasets/' + CFG.DATASET_NAME
## dataloader args, optional
CFG.TEST.DATA.BATCH_SIZE    = 64
CFG.TEST.DATA.PREFETCH      = False
CFG.TEST.DATA.SHUFFLE       = False
CFG.TEST.DATA.NUM_WORKERS   = 2
CFG.TEST.DATA.PIN_MEMORY    = False
