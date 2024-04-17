bash adc_setup.bash 
python3 read_all_regs.py > ./logs/log_read_all_regs_after_bash_adc_setup.log 
python3 write_all_regs.py
python3 read_all_regs.py > ./logs/log_read_all_regs_after_python_adc_setup.log
diff logs/log_read_all_regs_after_bash_adc_setup.log logs/log_read_all_regs_after_python_adc_setup.log
