import subprocess
import os.path
import pandas as pd 

selected_attrs = pd.read_csv('selected_attrs.csv')

pos_neg_vals = [(10, 5), (5, 20), (20, 40), (50, 50), (200, 400), (400, 400), (800, 1600)]
num_samples = 50
memory = 24  # number of GB

for (pos_seeds, neg_seeds) in pos_neg_vals:
    for (attr, attr_type) in zip(selected_attrs['attribute'], selected_attrs['attributeType']):
        if (selected_attrs[(selected_attrs['attribute'] == attr) & (selected_attrs['attributeType'] == attr_type)]['freq'].iloc[0] >= 2 * pos_seeds):
            safe_attr = '_'.join(attr.split())
            subprocess.check_call(['time', 'python3', '-u', 'test_gplus.py', '-a', str(attr), '-t', str(attr_type), '-p', str(pos_seeds), '-n', str(neg_seeds), '-S', str(num_samples), '-v', '--path', 'gplus0_lcc'])
            #cmd = "time python3 -u test_gplus.py -a '%s' -t '%s' -p %d -n %d -S %d -v --path gplus0_lcc" % (attr, attr_type, pos_seeds, neg_seeds, num_samples)
            #print(cmd)
            #subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
