export GEM5_DIR=/home/isaacpope/Documents/GEM5/gem5
export OPT=$GEM5_DIR/build/X86/gem5.opt
export PY=$GEM5_DIR/configs/example/se.py
export BENCHMARK=./src/blackscholes
export ARGUMENT=./inputs/input_test/in_4.txt
time $OPT -d m5out/ $PY -c $BENCHMARK -o $ARGUMENT -I 100000000 --cpu-type=TimingSimpleCPU --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=128kB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=2 --cacheline_size=32 --bp-type=LocalBP
