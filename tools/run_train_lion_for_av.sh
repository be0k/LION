#! /bin/bash

# mamba like waymo
# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_av/av.yaml \
# --extra_tag av-intensitye \
# --batch_size 4  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn


# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_av/av.yaml \
# --extra_tag perpect \
# --batch_size 2  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn


#best

CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
--nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
--cfg_file ./cfgs/custom_av/av.yaml \
--extra_tag low_lr \
--batch_size 4  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn



# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_av/av_last.yaml \
# --extra_tag last \
# --batch_size 4  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn

