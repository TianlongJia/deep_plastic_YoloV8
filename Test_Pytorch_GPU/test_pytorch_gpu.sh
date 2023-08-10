#!/bin/bash
#SBATCH --job-name="Test_Pytorch_GPU"
#SBATCH --partition=gpu
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-task=1
#SBATCH --mem-per-cpu=8G
#SBATCH --account=research-ceg-wm

# Load modules:
module load 2022r2 openmpi py-torch
# module load 2022r2
# module load openmpi
# module load miniconda3
# module load py-torch


# Set conda env:
# unset CONDA_SHLVL
# source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate conda, run job, deactivate conda
previous=$(/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/tail -n '+2')

# conda activate DP_YoloV8_conda
srun python test_pytorch_gpu.py

/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/grep -v -F "$previous"

# conda deactivate