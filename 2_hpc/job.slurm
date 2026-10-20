#!/bin/bash
# Contoh batch job. Sesuaikan direktif akun/partisi dengan panduan klaster.
#SBATCH --job-name=contoh-lingkungan
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=2G
#SBATCH --output=hasil-%j.log

set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
python main.py --workers "${SLURM_CPUS_PER_TASK:-4}" --scenarios 10000
