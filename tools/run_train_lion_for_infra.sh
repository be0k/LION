#! /bin/bash

## mamba infra
# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_models/infra.yaml \
# --extra_tag infra \
# --batch_size 10  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn

#baseline infra
# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_models/infra_base.yaml \
# --extra_tag infra_base \
# --batch_size 10  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn


# mamba like waymo
# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_models/infra2.yaml \
# --extra_tag infra2 \
# --batch_size 10  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn

#weight decay 0.05 -> 0.01
# CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
# --nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
# --cfg_file ./cfgs/custom_models/infra3.yaml \
# --extra_tag infra3 --pretrained_model ../output/cfgs/custom_models/infra2/infra2/ckpt/latest_model.pth \
# --batch_size 10  --epochs 10 --max_ckpt_save_num 4 --workers 0 --sync_bn

#best
CUDA_VISIBLE_DEVICES=0,1 TORCH_USE_CUDA_DSA=1 python -m torch.distributed.launch \
--nproc_per_node=2 --master_port=29988 train.py  --tcp_port 29988  --launcher pytorch  \
--cfg_file ./cfgs/custom_models/infra_later.yaml \
--extra_tag infra_later \
--batch_size 10  --epochs 40 --max_ckpt_save_num 4 --workers 0 --sync_bn