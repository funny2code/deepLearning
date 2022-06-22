"""# pytorch-loss
Docs::


    Also tried to implement swish, hard-swish(hswish) and mish activation functions.

    Additionally, cuda based one-hot function is added (support label smooth).

    Newly add an "Exponential Moving Average(EMA)" operator.

    Add convolution ops, such as coord-conv2d, and dynamic-conv2d(dy-conv2d).

    Some operators are implemented with pytorch cuda extension, so you need to compile it first:


    After installing, now you can pick up what you need and use the losses or ops like one of thes:
    ```python
    from losses import SwishV1, SwishV2, SwishV3
    from losses import HSwishV1, HSwishV2, HSwishV3
    from losses import MishV1, MishV2, MishV3
    from losses import convert_to_one_hot, convert_to_one_hot_cu, OnehotEncoder
    from losses import EMA

    from losses import TripletLoss
    from losses import SoftDiceLossV1, SoftDiceLossV2, SoftDiceLossV3
    from losses import PCSoftmaxCrossEntropyV1, PCSoftmaxCrossEntropyV2
    from losses import LargeMarginSoftmaxV1, LargeMarginSoftmaxV2, LargeMarginSoftmaxV3
    from losses import LabelSmoothSoftmaxCEV1, LabelSmoothSoftmaxCEV2, LabelSmoothSoftmaxCEV3
    from losses import generalized_iou_loss
    from losses import FocalLossV1, FocalLossV2, FocalLossV3
    from losses import Dual_Focal_loss
    from losses import GeneralizedSoftDiceLoss, BatchSoftDiceLoss
    from losses import AMSoftmax
    from losses import AffinityFieldLoss, AffinityLoss
    from losses import OhemCELoss, OhemLargeMarginLoss
    from losses import LovaszSoftmaxV1, LovaszSoftmaxV3
    from losses import TaylorCrossEntropyLossV1, TaylorCrossEntropyLossV3
    from losses import InfoNceDist
    from losses import PartialFCAMSoftmax

    from losses import TaylorSoftmaxV1, TaylorSoftmaxV3
    from losses import LogTaylorSoftmaxV1, LogTaylorSoftmaxV3

    from losses import CoordConv2d, DY_Conv2d
    ```
    Note that some losses or ops have 3 versions, like `LabelSmoothSoftmaxCEV1`, `LabelSmoothSoftmaxCEV2`, `LabelSmoothSoftmaxCEV3`, here `V1` means the implementation with pure pytorch ops and use `torch.autograd` for backward computation, `V2` means implementation with pure pytorch ops but use self-derived formula for backward computation, and `V3` means implementation with cuda extension. Generally speaking, the `V3` ops are faster and more memory efficient, since I have tried to squeeze everything in one cuda kernel function, which in most cases brings less overhead than a combination of pytorch ops.


    For those who happen to find this repo, if you see errors in my code, feel free to open an issue to correct me.



"""
from .swish import SwishV1, SwishV2, SwishV3
from .hswish import HSwishV1, HSwishV2, HSwishV3
from .frelu import FReLU
from .mish import MishV1, MishV2, MishV3
from .one_hot import convert_to_one_hot, convert_to_one_hot_cu, OnehotEncoder
from .ema import EMA

from .triplet_loss import TripletLoss
from .soft_dice_loss import SoftDiceLossV1, SoftDiceLossV2, SoftDiceLossV3
from .pc_softmax import PCSoftmaxCrossEntropyV1, PCSoftmaxCrossEntropyV2
from .large_margin_softmax import LargeMarginSoftmaxV1, LargeMarginSoftmaxV2, LargeMarginSoftmaxV3
from .label_smooth import LabelSmoothSoftmaxCEV1, LabelSmoothSoftmaxCEV2, LabelSmoothSoftmaxCEV3
from .generalized_iou_loss import generalized_iou_loss
from .focal_loss import FocalLossV1, FocalLossV2, FocalLossV3
from .dual_focal_loss import Dual_Focal_loss
from .dice_loss import GeneralizedSoftDiceLoss, BatchSoftDiceLoss
from .amsoftmax import AMSoftmax
from .affinity_loss import AffinityFieldLoss, AffinityLoss
from .ohem_loss import OhemCELoss, OhemLargeMarginLoss
from .conv_ops import CoordConv2d, DY_Conv2d
from .lovasz_softmax import LovaszSoftmaxV1, LovaszSoftmaxV3
from .taylor_softmax import TaylorSoftmaxV1, TaylorSoftmaxV3, LogTaylorSoftmaxV1, LogTaylorSoftmaxV3, TaylorCrossEntropyLossV1, TaylorCrossEntropyLossV3
from .info_nce_dist import InfoNceDist
from .partial_fc_amsoftmax import PartialFCAMSoftmax

from .layer_norm import LayerNormV1, LayerNormV2, LayerNormV3
