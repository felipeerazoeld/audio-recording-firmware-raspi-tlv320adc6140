bash adc_setup.bash 
python3 ../python/read_all_regs.py > ../log/log_read_all_regs_after_bash_adc_setup.log 
python3 ../python/write_all_regs.py
python3 ../python/read_all_regs.py > ../log/log_read_all_regs_after_python_adc_setup.log
diff ../log/log_read_all_regs_after_bash_adc_setup.log ../log/log_read_all_regs_after_python_adc_setup.log
