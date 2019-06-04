rm -rf output_new
rm -rf input
python generate_data_vv.py
hadoop fs -mkdir input
hadoop fs -put input.txt ./input
chmod +x vv_mapper.py
chmod +x vv_reducer.py
mapred streaming -input ./input -output ./output_new -mapper ./vv_mapper.py -reducer ./vv_reducer.py