#!/bin/bash
#SBATCH --job-name=isolate_blast
#SBATCH --mail-user=ajwing@umich.edu
#SBATCH --mail-type=BEGIN,END
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=64g 
#SBATCH --time=24:00:00
#SBATCH --account=duhaimem1
#SBATCH --partition=standard
#SBATCH --output=%x-%j.log
#SBATCH --array=1-12%11

# The application(s) to execute along with its input arguments and options:
module load Bioinformatics ncbi-blast
reads=$(sed -n "$SLURM_ARRAY_TASK_ID"p fastas.job.conf)
ref=genomes/combined.fa
sample=$(echo $reads | cut -f1 -d "/")
blastn -query $reads -subject $ref -perc_identity 0 -max_target_seqs 1 -outfmt "6 qseqid sseqid pident qlen slen length mismatch gapopen qstart qend sstart send evalue bitscore" -out ${sample}_best_hit_combined.blast

blastn -query $reads -subject $ref -perc_identity 0 -max_target_seqs 5000 -outfmt "6 qseqid sseqid pident qlen slen length mismatch gapopen qstart qend sstart send evalue bitscore" -out ${sample}_all_hits_combined.blast
