# -- Script genérico para ejecución de GEM5 --
# -- Dirección donde GEM5 fue construı́do --
export GEM5_DIR=/home/fabelifer2797/Documents/GEM5/gem5
export OPT=$GEM5_DIR/build/X86/gem5.opt
export PY=$GEM5_DIR/configs/example/se.py
export BENCHMARK=./src/swaptions
export ARGUMENT=./
# -- Ejecución del ambiente --
time $OPT -d m5out/ $PY -c $BENCHMARK -o $ARGUMENT
